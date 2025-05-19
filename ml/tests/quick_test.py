import os
import sys
import subprocess
import time
import requests
import json

def start_server():
    """Start the Flask server"""
    print("Starting server...")
    server_process = subprocess.Popen(
        ["python", "backend/app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)  # Wait for server to start
    return server_process

def test_api(test_cases):
    """Test the API endpoints"""
    url = "http://localhost:5000/predict"
    
    for test in test_cases:
        try:
            print(f"\nTesting: {test['description']}")
            print(f"Symptoms: {test['symptoms']}")
            print(f"Age: {test['age']}, Gender: {test['gender']}")
            
            response = requests.post(url, json={
                "symptoms": test["symptoms"],
                "age": test["age"],
                "gender": test["gender"]
            })
            
            result = response.json()
            print("\nPredictions:")
            for pred in result["predictions"]:
                print(f"\nDisease: {pred['disease']}")
                print(f"Confidence: {pred['confidence']:.2f}")
                print(f"Severity: {pred['severity']}")
                if pred['medicine_recommendations']:
                    print("Medicines:")
                    for med in pred['medicine_recommendations']:
                        print(f"- {med['medicine']} ({med['dosage']})")
            print("\n" + "="*50)
            
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Test cases
    test_cases = [
        {
            "description": "Adult Male with Cold Symptoms",
            "symptoms": ["fever", "cough", "sore throat"],
            "age": 25,
            "gender": "male"
        },
        {
            "description": "Child with Fever",
            "symptoms": ["high temperature", "irritability", "loss of appetite"],
            "age": 8,
            "gender": "male"
        },
        {
            "description": "Elderly Female with Joint Pain",
            "symptoms": ["joint pain", "stiffness", "swelling"],
            "age": 65,
            "gender": "female"
        },
        {
            "description": "Adult Female with Pregnancy Symptoms",
            "symptoms": ["nausea", "fatigue", "back pain"],
            "age": 28,
            "gender": "female"
        },
        {
            "description": "Adult Female with Migraine",
            "symptoms": ["severe headache", "nausea", "sensitivity to light"],
            "age": 35,
            "gender": "female"
        }
    ]
    
    # Start server
    server = start_server()
    
    try:
        # Run tests
        test_api(test_cases)
    finally:
        # Cleanup
        server.terminate()
        print("\nServer stopped.") 