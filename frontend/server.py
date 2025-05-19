import sys
import os
import subprocess
import requests
import time
import pandas as pd
import threading
import google.generativeai as genai
from flask import Flask, send_from_directory, render_template, redirect, url_for, request, session, jsonify, Response, flash
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import json
import logging

# Add parent directory to system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.models import User, LoginHistory, get_session
from datetime import datetime, date

app = Flask(__name__, static_folder='static')

# Enable CORS properly for local development
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

app.secret_key = os.getenv('SECRET_KEY', 'medis_default_secret_key')

# Backend process as global variable
backend_process = None
BACKEND_PORT = int(os.getenv('BACKEND_PORT', 5001))

# Configure Gemini API key directly
genai.configure(api_key='AIzaSyBxpdGmZflrGJOEQSMSL6BqEUg57FCjNoo')

logger = logging.getLogger(__name__)

def start_backend():
    backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app.py'))
    print(f"Starting backend server from: {backend_path}")
    
    if not os.path.exists(backend_path):
        print(f"Error: Backend file not found at {backend_path}")
        return None
        
    try:
        # Start the backend process with output redirection
        process = subprocess.Popen(
            [sys.executable, backend_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1  # Line buffered
        )
        
        # Start a thread to monitor backend output
        def monitor_output(pipe, prefix):
            for line in pipe:
                print(f"{prefix}: {line.strip()}")
                
        threading.Thread(target=monitor_output, args=(process.stdout, "Backend stdout"), daemon=True).start()
        threading.Thread(target=monitor_output, args=(process.stderr, "Backend stderr"), daemon=True).start()
        
        # Give the backend a moment to start
        time.sleep(2)
        
        # Check if the process is still running
        if process.poll() is not None:
            print(f"Backend process failed to start (exit code: {process.returncode})")
            return None
            
        # Try to connect to the backend
        try:
            response = requests.get(f'http://127.0.0.1:{BACKEND_PORT}/health')
            if response.status_code == 200:
                print("Backend server started successfully!")
            else:
                print(f"Backend health check failed with status code: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("Could not connect to backend server")
            return None
            
        return process
    except Exception as e:
        print(f"Error starting backend server: {str(e)}")
        return None

# Serve static files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Serve CSS file
@app.route('/styles.css')
def serve_css():
    return send_from_directory('.', 'styles.css')

# Serve JavaScript file
@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')

# Home page (always accessible)
@app.route('/')
def home():
    return render_template('index.html')

# Prediction page
@app.route('/prediction')
def prediction():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('prediction.html')

# Login page
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Please provide both email and password', 'error')
            return render_template('auth/login.html')
        
        db = get_session()
        try:
            user = db.query(User).filter(User.email == email).first()
            
            if user and check_password_hash(user.hashed_password, password):
                session['user_id'] = user.id
                
                # Record login history
                login_record = LoginHistory(
                    user_id=user.id,
                    ip_address=request.remote_addr
                )
                db.add(login_record)
                db.commit()
                
                return redirect(url_for('prediction'))
            else:
                flash('Invalid email or password', 'error')
        finally:
            db.close()
            
    return render_template('auth/login.html')

# Register page
@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        gender = request.form.get('gender')
        date_of_birth = request.form.get('date_of_birth')
        
        if not all([name, email, password, confirm_password, gender, date_of_birth]):
            flash('Please fill in all fields', 'error')
            return render_template('auth/register.html')
            
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth/register.html')
        
        db = get_session()
        try:
            # Check if user already exists
            if db.query(User).filter(User.email == email).first():
                flash('Email already registered', 'error')
                return render_template('auth/register.html')
            
            # Create new user with additional fields
            new_user = User(
                name=name,
                email=email,
                hashed_password=generate_password_hash(password),
                gender=gender,
                date_of_birth=datetime.strptime(date_of_birth, '%Y-%m-%d').date()
            )
            db.add(new_user)
            db.commit()
            
            # Log the user in
            session['user_id'] = new_user.id
            return redirect(url_for('prediction'))
        finally:
            db.close()
            
    return render_template('auth/register.html')

# Logout
@app.route('/auth/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

def calculate_age(birthdate):
    if not birthdate:
        return None
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Profile page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    db = get_session()
    try:
        # Fetch user from database
        user = db.query(User).filter(User.id == session['user_id']).first()
        if not user:
            session.pop('user_id', None)
            return redirect(url_for('login'))
        
        if request.method == 'POST':
            # Update user info
            user.name = request.form.get('name', user.name)
            user.email = request.form.get('email', user.email)
            user.gender = request.form.get('gender', user.gender)
            
            # Update date of birth if provided
            new_dob = request.form.get('date_of_birth')
            if new_dob:
                try:
                    user.date_of_birth = datetime.strptime(new_dob, '%Y-%m-%d').date()
                except ValueError:
                    flash('Invalid date format', 'error')
            
            try:
                db.commit()
                flash('Profile updated successfully!', 'success')
            except Exception as e:
                db.rollback()
                flash('Error updating profile', 'error')
            
            return redirect(url_for('profile'))
        
        # Get login history
        login_history = (db.query(LoginHistory)
                        .filter(LoginHistory.user_id == user.id)
                        .order_by(LoginHistory.login_time.desc())
                        .limit(5)
                        .all())
        
        # Prepare user data for template
        user_data = {
            'name': user.name,
            'email': user.email,
            'gender': user.gender,
            'date_of_birth': user.date_of_birth.strftime('%Y-%m-%d') if user.date_of_birth else '',
            'age': calculate_age(user.date_of_birth)
        }
        
        return render_template('profile.html', 
                             user=user_data, 
                             login_history=login_history)
    finally:
        db.close()

# Nearby page
@app.route('/nearby')
def nearby():
    return render_template('nearby.html')

# Nearby hospitals API
@app.route('/api/nainital-hospitals', methods=['GET'])
def nainital_hospitals():
    df = pd.read_csv('data/nainital_hospitals.csv')
    hospitals = []
    for _, row in df.iterrows():
        hospitals.append({
            'name': row['Name'],
            'lat': float(row['Latitude']) if row['Latitude'] else None,
            'lng': float(row['Longitude']) if row['Longitude'] else None,
            'address': row['Address'],
            'contact': row['Contact'],
            'verified': True
        })
    return jsonify({'hospitals': hospitals})

# OpenRouteService Nearby Healthcare API
@app.route('/api/nearby-healthcare-ors', methods=['POST'])
def nearby_healthcare_ors():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    ORS_API_KEY = "5b3ce3597851110001cf62480b4c7f467e6045d299996beaf374a83f"
    url = "https://api.openrouteservice.org/pois"
    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "request": "pois",
        "geometry": {
            "bbox": [[lng-0.05, lat-0.05], [lng+0.05, lat+0.05]],
            "geojson": {
                "type": "Point",
                "coordinates": [lng, lat]
            },
            "buffer": 3000
        },
        "filters": {
            "categories": ["healthcare.hospital", "healthcare.clinic", "healthcare.pharmacy"]
        }
    }
    resp = requests.post(url, headers=headers, json=body)
    pois = resp.json().get('features', [])
    hospitals = []
    for poi in pois:
        props = poi['properties']
        coords = poi['geometry']['coordinates']
        hospitals.append({
            'name': props.get('name', 'Unknown'),
            'lat': coords[1],
            'lng': coords[0],
            'address': props.get('address', ''),
            'type': props.get('category', ''),
            'verified': True
        })
    return jsonify({'hospitals': hospitals})

def geocode(address):
    url = f"https://nominatim.openstreetmap.org/search"
    params = {
        "q": address + ", Nainital, Uttarakhand, India",
        "format": "json",
        "limit": 1
    }
    try:
        resp = requests.get(url, params=params, headers={"User-Agent": "medis/1.0"})
        data = resp.json()
        if data:
            return data[0]['lat'], data[0]['lon']
    except Exception as e:
        print(f"Geocoding error for {address}: {e}")
    return "", ""

@app.route('/api/nearby-pois', methods=['POST'])
def nearby_pois():
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    category = data.get('category', 'healthcare.hospital')  # default to hospital
    ORS_API_KEY = "YOUR_ORS_API_KEY"
    url = "https://api.openrouteservice.org/pois"
    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "request": "pois",
        "geometry": {
            "bbox": [[lng-0.05, lat-0.05], [lng+0.05, lat+0.05]],
            "geojson": {
                "type": "Point",
                "coordinates": [lng, lat]
            },
            "buffer": 5000
        },
        "filters": {
            "categories": [category]
        }
    }
    resp = requests.post(url, headers=headers, json=body)
    pois = resp.json().get('features', [])
    results = []
    for poi in pois:
        props = poi['properties']
        coords = poi['geometry']['coordinates']
        results.append({
            'name': props.get('name', 'Unknown'),
            'lat': coords[1],
            'lng': coords[0],
            'address': props.get('address', ''),
            'type': props.get('category', ''),
            'verified': True
        })
    return jsonify({'results': results})

@app.route('/predict', methods=['POST'])
def proxy_predict():
    backend_url = f'http://127.0.0.1:{BACKEND_PORT}/predict'
    try:
        # Log the request
        request_data = request.get_json()
        logger.info(f"Sending prediction request to backend: {request_data}")
        
        # Send request to backend
        resp = requests.post(backend_url, json=request_data, timeout=10)
        
        # Log the response
        logger.info(f"Backend response status: {resp.status_code}")
        logger.info(f"Backend response: {resp.text[:200]}...")  # Log first 200 chars
        
        if resp.status_code != 200:
            logger.error(f"Backend error: {resp.text}")
            return jsonify({
                "error": "Backend processing error",
                "details": resp.text
            }), resp.status_code
            
        # Parse response to ensure it's valid JSON
        try:
            response_data = resp.json()
            if not response_data.get('predictions'):
                logger.warning("No predictions in response")
                return jsonify({
                    "error": "No predictions available for the given symptoms. Please try with different symptoms."
                }), 404
            return jsonify(response_data)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON from backend: {e}")
            return jsonify({
                "error": "Invalid response from backend server"
            }), 500
            
    except requests.exceptions.ConnectionError:
        logger.error("Backend server connection failed")
        return jsonify({
            "error": "Backend server is not responding. Please try again later."
        }), 503
    except requests.exceptions.Timeout:
        logger.error("Backend request timed out")
        return jsonify({
            "error": "Request timed out. Please try again."
        }), 504
    except Exception as e:
        logger.error(f"Unexpected error in proxy_predict: {str(e)}")
        return jsonify({
            "error": "An unexpected error occurred"
        }), 500

# Test route for Gemini API
@app.route('/test-gemini')
def test_gemini():
    try:
        # Configure the API
        genai.configure(api_key='AIzaSyBxpdGmZflrGJOEQSMSL6BqEUg57FCjNoo')
        
        # Create a simple model
        model = genai.GenerativeModel('gemini-pro')
        
        # Try a simple prompt
        response = model.generate_content('Say "Hello! I am working!"')
        
        if response and hasattr(response, 'text'):
            return jsonify({
                'status': 'success',
                'message': 'API is working',
                'response': response.text
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Invalid response structure',
                'response': str(response)
            }), 500
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e),
            'type': type(e).__name__
        }), 500

# Simplified chat route with better error handling
@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
            
        message = data['message']
        
        try:
            # Configure API
            genai.configure(api_key='AIzaSyBxpdGmZflrGJOEQSMSL6BqEUg57FCjNoo')
            
            # List available models first
            available_models = genai.list_models()
            print("Available models:", [model.name for model in available_models])
            
            # Try to find a suitable model
            model_names = ['gemini-1.0-pro', 'gemini-pro', 'chat-bison-001']
            
            last_error = None
            for model_name in model_names:
                try:
                    model = genai.GenerativeModel(model_name)
                    
                    # Create a proper medical assistant prompt
                    prompt = f"""You are MEDIS Assistant, a medical AI helper specialized in healthcare. 
                    You should:
                    - Provide clear, accurate medical information
                    - Ask clarifying questions when needed
                    - Suggest seeking professional medical help for serious concerns
                    - Keep responses focused on health and medical topics
                    - Be empathetic but professional
                    
                    User: {message}
                    Assistant:"""
                    
                    response = model.generate_content(prompt)
                    
                    if response and hasattr(response, 'text'):
                        return jsonify({'response': response.text.strip()})
                    
                except Exception as e:
                    print(f"Error with model {model_name}: {str(e)}")
                    last_error = str(e)
                    continue
            
            # If we get here, all models failed
            return jsonify({
                'error': f'Unable to generate response: {last_error}'
            }), 500
                
        except Exception as e:
            print(f"API Error: {str(e)}")
            if "quota" in str(e).lower():
                return jsonify({
                    'error': 'The chat service is temporarily unavailable due to high demand. Please try again in a few minutes.'
                }), 429
            else:
                return jsonify({
                    'error': f'API Error: {str(e)}'
                }), 500
            
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({
            'error': 'An unexpected error occurred. Please try again.'
        }), 500

if __name__ == '__main__':
    try:
        # Start the backend first
        backend_process = start_backend()
        if not backend_process:
            print("Failed to start backend server. Please check the logs above.")
            sys.exit(1)
        
        # Then start the frontend server with debug mode and proper host/port
        app.run(
            host='0.0.0.0',
            port=3000,
            debug=True,
            use_reloader=False  # Important when running with subprocess
        )
    except Exception as e:
        print(f"Server error: {str(e)}")
    finally:
        if 'backend_process' in locals() and backend_process:
            print("Shutting down backend server...")
            backend_process.terminate()
            try:
                backend_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                backend_process.kill() 



                