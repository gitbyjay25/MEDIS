import requests
import json

# Test cases for different diseases with specific symptoms
test_cases = [
    {
        "name": "Malaria-like symptoms",
        "data": {
            "symptoms": [
                "high_fever",
                "chills",
                "sweating",
                "headache",
                "nausea",
                "muscle_pain",
                "fatigue"
            ],
            "age_group": "ADULT",
            "season": "MONSOON"
        }
    },
    {
        "name": "Typhoid-like symptoms",
        "data": {
            "symptoms": [
                "high_fever",
                "fatigue",
                "headache",
                "abdominal_pain",
                "constipation",
                "diarrhea",
                "nausea"
            ],
            "age_group": "ADULT",
            "season": "SUMMER"
        }
    },
    {
        "name": "Jaundice-like symptoms",
        "data": {
            "symptoms": [
                "yellowing_skin",
                "dark_urine",
                "fatigue",
                "nausea",
                "vomiting",
                "abdominal_pain",
                "loss_of_appetite"
            ],
            "age_group": "ADULT",
            "season": "MONSOON"
        }
    }
]

def test_prediction(test_case):
    print(f"\nTesting {test_case['name']}:")
    print("=" * 50)
    print("Symptoms:", ", ".join(test_case['data']['symptoms']))
    
    try:
        response = requests.post(
            "http://localhost:5001/predict",
            json=test_case['data'],
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("\nPredicted Diseases:")
            print("-" * 30)
            for prediction in result.get("predictions", []):
                print(f"Disease: {prediction.get('disease', 'Unknown')}")
                print(f"Confidence: {prediction.get('confidence', 0):.2f}")
                print("-" * 30)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    
    except Exception as e:
        print(f"Error making request: {e}")

# Run tests for each case
for test_case in test_cases:
    test_prediction(test_case) 