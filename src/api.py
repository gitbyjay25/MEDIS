"""
API interface for the MEDIS system.
Provides REST endpoints for disease prediction and symptom suggestions.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from models.predictor import predict_diseases, get_suggested_symptoms
from models.disease_profiles import AGE_GROUPS, SEASONS

app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Endpoint for disease prediction.
    
    Expected JSON payload:
    {
        "symptoms": ["symptom1", "symptom2", ...],
        "age_group": "ADULT",  # optional
        "season": "SUMMER"     # optional
    }
    """
    data = request.get_json()
    
    if not data or 'symptoms' not in data:
        return jsonify({
            'error': 'Invalid request. Must provide symptoms list.'
        }), 400
    
    symptoms = data['symptoms']
    age_group = data.get('age_group')
    season = data.get('season')
    
    # Validate age_group if provided
    if age_group and age_group not in AGE_GROUPS:
        return jsonify({
            'error': f'Invalid age_group. Must be one of: {list(AGE_GROUPS.keys())}'
        }), 400
    
    # Validate season if provided
    if season and season not in SEASONS:
        return jsonify({
            'error': f'Invalid season. Must be one of: {list(SEASONS.keys())}'
        }), 400
    
    predictions = predict_diseases(symptoms, age_group, season)
    
    return jsonify({
        'predictions': predictions,
        'count': len(predictions)
    })

@app.route('/api/suggest-symptoms', methods=['POST'])
def suggest_symptoms():
    """
    Endpoint for symptom suggestions.
    
    Expected JSON payload:
    {
        "current_symptoms": ["symptom1", "symptom2", ...],
        "age_group": "ADULT"  # optional
    }
    """
    data = request.get_json()
    
    if not data or 'current_symptoms' not in data:
        return jsonify({
            'error': 'Invalid request. Must provide current_symptoms list.'
        }), 400
    
    current_symptoms = data['current_symptoms']
    age_group = data.get('age_group')
    
    # Validate age_group if provided
    if age_group and age_group not in AGE_GROUPS:
        return jsonify({
            'error': f'Invalid age_group. Must be one of: {list(AGE_GROUPS.keys())}'
        }), 400
    
    suggested = get_suggested_symptoms(current_symptoms, age_group)
    
    return jsonify({
        'suggested_symptoms': suggested,
        'count': len(suggested)
    })

@app.route('/api/info', methods=['GET'])
def get_info():
    """
    Endpoint to get system information.
    Returns available age groups and seasons.
    """
    return jsonify({
        'age_groups': AGE_GROUPS,
        'seasons': SEASONS
    })

if __name__ == '__main__':
    app.run(debug=True) 