import requests
import json

def test_api():
    url = "http://localhost:5001/predict"
    
    # Test cases
    test_cases = [
        {
            "description": "Test Case 1: Common Cold Symptoms",
            "symptoms": ["fever", "cough", "sore throat"],
            "age": 25,
            "gender": "male"
        },
        {
            "description": "Test Case 2: Flu Symptoms",
            "symptoms": ["high fever", "body ache", "fatigue"],
            "age": 30,
            "gender": "female"
        },
        {
            "description": "Test Case 3: Stomach Issues",
            "symptoms": ["nausea", "vomiting", "stomach pain"],
            "age": 45,
            "gender": "male"
        }
    ]
    
    for test in test_cases:
        print(f"\nTesting: {test['description']}")
        print(f"Symptoms: {test['symptoms']}")
        print(f"Age: {test['age']}, Gender: {test['gender']}")
        
        try:
            response = requests.post(url, json={
                "symptoms": test["symptoms"],
                "age": test["age"],
                "gender": test["gender"]
            })
            
            if response.status_code == 200:
                result = response.json()
                print("\nPredictions:")
                for pred in result["predictions"]:
                    print(f"\nDisease: {pred['disease']}")
                    print(f"Confidence: {pred['confidence']:.2f}")
                    print(f"Severity: {pred['severity']}")
                    
                    if 'medicine_recommendations' in pred:
                        print("\nMedicine Recommendations:")
                        for med in pred['medicine_recommendations']:
                            print(f"- {med['medicine']} ({med['dosage']})")
                    
                    if 'food_preferences' in pred:
                        print("\nFood Preferences:")
                        for food in pred['food_preferences']:
                            print(f"- {food}")
                    
                    if 'exercises' in pred:
                        print("\nExercises:")
                        for exercise in pred['exercises']:
                            print(f"- {exercise}")
                    
                    print("\nPrecautions:")
                    for precaution in pred['precautions']:
                        print(f"- {precaution}")
                    
                    print("\n" + "="*50)
            else:
                print(f"Error: {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"Error: {str(e)}")

def test_chicken_pox_issue():
    url = "http://localhost:5001/predict"
    
    # Symptoms that should trigger Chicken Pox, not Depression
    payload = {
        "symptoms": [
            "fever", 
            "fatigue",
            "itchy rash",
            "blisters",
            "loss of appetite"
        ]
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        
        print("API Response:")
        print(json.dumps(result, indent=2))
        
        # Check if we got predictions
        if 'predictions' in result:
            predictions = result['predictions']
            if predictions:
                top_disease = predictions[0]['disease']
                confidence = predictions[0]['confidence']
                
                print(f"\nTop prediction: {top_disease} with confidence {confidence}")
                
                # Print all fields in the prediction
                print("\nAll fields in prediction:")
                for key, value in predictions[0].items():
                    print(f"{key}: {value}")
                
                # Verify Depression is not in the predictions
                has_depression = False
                for p in predictions:
                    if p['disease'] == 'Depression':
                        has_depression = True
                        break
                
                if not has_depression:
                    print("Test PASSED: Depression not found in predictions")
                else:
                    print("Test FAILED: Depression should not be predicted for skin conditions")
                
                # Verify Chicken Pox is in the predictions
                has_chicken_pox = False
                for p in predictions:
                    if p['disease'] == 'Chicken Pox':
                        has_chicken_pox = True
                        break
                
                if has_chicken_pox:
                    print("Test PASSED: Chicken Pox found in predictions") 
                else:
                    print("Test FAILED: Chicken Pox should be predicted for these symptoms")
                
            else:
                print("No predictions returned")
        else:
            print("No predictions in API response")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
    test_chicken_pox_issue() 