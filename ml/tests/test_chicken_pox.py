import requests
import json

def test_chicken_pox():
    url = "http://localhost:5001/predict"
    
    # Symptoms that should trigger Chicken Pox, not Depression
    payload = {
        "symptoms": [
            "fever", 
            "fatigue",
            "itchy rash",
            "blisters",
            "loss of appetite"
        ],
        "age": 10,
        "gender": "male"
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        print("Sending request to predict chicken pox symptoms...")
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
                
                # Check if recommendations are available
                if 'medicines' in predictions[0]:
                    print("\n✅ Medicines recommendations available")
                    for med in predictions[0]['medicines']:
                        print(f"  - {med['name']}: {med['dosage']} ({med['purpose']})")
                else:
                    print("\n❌ No medicine recommendations available")
                    
                if 'diet' in predictions[0]:
                    print("\n✅ Diet recommendations available")
                    for item in predictions[0]['diet']:
                        print(f"  - {item}")
                else:
                    print("\n❌ No diet recommendations available")
                    
                if 'exercise' in predictions[0]:
                    print("\n✅ Exercise recommendations available")
                    for item in predictions[0]['exercise']:
                        print(f"  - {item}")
                else:
                    print("\n❌ No exercise recommendations available")
                
                # Verify Depression is not in the predictions
                has_depression = False
                for p in predictions:
                    if p['disease'] == 'Depression':
                        has_depression = True
                        break
                
                if not has_depression:
                    print("\n✅ Test PASSED: Depression not found in predictions")
                else:
                    print("\n❌ Test FAILED: Depression should not be predicted for skin conditions")
                
                # Verify Chicken Pox is in the predictions
                has_chicken_pox = False
                for p in predictions:
                    if p['disease'] == 'Chicken Pox':
                        has_chicken_pox = True
                        break
                
                if has_chicken_pox:
                    print("\n✅ Test PASSED: Chicken Pox found in predictions") 
                else:
                    print("\n❌ Test FAILED: Chicken Pox should be predicted for these symptoms")
                
            else:
                print("No predictions returned")
        else:
            print("No predictions in API response")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_chicken_pox() 