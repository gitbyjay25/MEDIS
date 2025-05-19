import requests
import json
import traceback
import time

def test_random_disease():
    """Test that recommendations are present even for less common diseases"""
    url = "http://localhost:5001/predict"
    
    # Define test cases for all problematic diseases
    test_cases = [
        {
            "name": "Jaundice Test",
            "symptoms": [
                "yellowing skin", 
                "yellowing eyes",
                "dark urine",
                "pale stools",
                "fatigue",
                "itching", 
                "jaundice"
            ]
        },
        {
            "name": "Hepatitis Test",
            "symptoms": [
                "yellowish skin", 
                "yellowing eyes",
                "dark urine",
                "right upper abdominal pain",
                "fatigue",
                "loss of appetite",
                "nausea",
                "jaundice"
            ]
        },
        {
            "name": "Food Poisoning Test",
            "symptoms": [
                "nausea", 
                "vomiting",
                "diarrhea",
                "stomach pain",
                "weakness",
                "fever"
            ]
        }
    ]

    # Process each test case
    for test in test_cases:
        try:
            print(f"\n\n===== Testing {test['name']} =====")
            print(f"Symptoms: {', '.join(test['symptoms'])}")
            
            payload = {"symptoms": test["symptoms"]}
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                print(f"Predictions for {test['name']}:")
                for pred in result['predictions']:
                    print(f"  - {pred['disease']} (Confidence: {pred['confidence']:.2f})")
                
                # Check if the prediction matches the expected disease
                expected_disease = test['name'].split()[0]
                primary_prediction = result['predictions'][0]['disease']
                
                if expected_disease in primary_prediction:
                    print(f"✅ SUCCESS: Got expected disease {primary_prediction}")
                else:
                    print(f"❌ ERROR: Expected {expected_disease} but got {primary_prediction}")
                    
            else:
                print(f"Error: {response.status_code}")
                print(response.text)
                
            # Add a short delay between tests
            time.sleep(1)
                
        except Exception as e:
            print(f"Error during test: {e}")
            traceback.print_exc()

if __name__ == "__main__":
    test_random_disease() 