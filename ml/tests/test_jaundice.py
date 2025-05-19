import requests
import json
import time

def test_jaundice():
    """Test different combinations of jaundice symptoms to ensure detection works"""
    url = "http://localhost:5001/predict"
    
    # Define test cases with different variations of jaundice symptoms
    test_cases = [
        {
            "name": "Basic Jaundice Test",
            "symptoms": ["yellow skin", "yellow eyes"]
        },
        {
            "name": "Jaundice with Dark Urine",
            "symptoms": ["yellow skin", "dark urine"]
        },
        {
            "name": "Jaundice with Single Symptom 1",
            "symptoms": ["yellowing skin"]
        },
        {
            "name": "Jaundice with Single Symptom 2",
            "symptoms": ["yellow eyes"]
        },
        {
            "name": "Jaundice with Single Symptom 3",
            "symptoms": ["jaundice"]
        },
        {
            "name": "Jaundice with Alternative Names",
            "symptoms": ["yellowish skin", "yellowing of eyes"]
        },
        {
            "name": "Jaundice with Alt Names",
            "symptoms": ["yellowing of skin", "eye yellowing"]
        },
        {
            "name": "Jaundice with Stool Symptom",
            "symptoms": ["clay colored stools", "fatigue"]
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
                
                # Check if the prediction matches expected disease
                if result['predictions'] and result['predictions'][0]['disease'] == 'Jaundice':
                    print(f"✅ SUCCESS: Got Jaundice diagnosis")
                else:
                    primary_prediction = "No disease" if not result['predictions'] else result['predictions'][0]['disease']
                    print(f"❌ ERROR: Expected Jaundice but got {primary_prediction}")
            else:
                print(f"Error: {response.status_code}")
                print(response.text)
                
            # Add a short delay between tests
            time.sleep(1)
                
        except Exception as e:
            print(f"Error during test: {e}")

if __name__ == "__main__":
    test_jaundice() 