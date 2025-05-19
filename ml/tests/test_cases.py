import requests
import json

# Test cases with expected diseases
test_cases = [
    {
        "name": "Migraine Test",
        "symptoms": ["headache", "nausea", "sensitivity to light", "vomiting", "visual disturbances"],
        "expected": "Migraine"
    },
    {
        "name": "Common Cold Test",
        "symptoms": ["runny nose", "sneezing", "cough", "sore throat", "fatigue"],
        "expected": "Common Cold"
    },
    {
        "name": "Flu Test",
        "symptoms": ["fever", "body pain", "fatigue", "cough", "headache", "chills"],
        "expected": "Flu"
    },
    {
        "name": "Bronchitis Test",
        "symptoms": ["cough", "chest pain", "fatigue", "shortness of breath", "fever"],
        "expected": "Bronchitis"
    },
    {
        "name": "Gastritis Test",
        "symptoms": ["stomach pain", "nausea", "vomiting", "loss of appetite"],
        "expected": "Gastritis"
    },
    {
        "name": "Pneumonia Test",
        "symptoms": ["fever", "cough", "chest pain", "shortness of breath", "fatigue", "sweating"],
        "expected": "Pneumonia"
    },
    {
        "name": "COVID-19 Test",
        "symptoms": ["fever", "cough", "fatigue", "loss of appetite", "shortness of breath"],
        "expected": "COVID-19"
    },
    {
        "name": "Sinusitis Test",
        "symptoms": ["headache", "runny nose", "cough", "fatigue", "fever"],
        "expected": "Sinusitis"
    },
    {
        "name": "Mixed Symptoms Test 1",
        "symptoms": ["headache", "fever", "cough", "fatigue"],
        "expected": None  # Multiple possibilities
    },
    {
        "name": "Mixed Symptoms Test 2",
        "symptoms": ["nausea", "vomiting", "dizziness", "fatigue"],
        "expected": None  # Multiple possibilities
    }
]

def run_test_cases():
    total_cases = len(test_cases)
    correct_predictions = 0
    total_confidence = 0
    
    print("\n=== Starting Disease Prediction Tests ===\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case['name']}")
        print("Symptoms:", ", ".join(test_case['symptoms']))
        
        try:
            # Make prediction request
            response = requests.post(
                'http://127.0.0.1:5000/predict',
                json={'symptoms': test_case['symptoms']}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                if result.get('top_prediction'):
                    predicted_disease = result['top_prediction']['disease']
                    confidence = result['top_prediction']['confidence']
                    model_prob = result['top_prediction']['model_probability']
                    symptom_score = result['top_prediction']['symptom_match_score']
                    
                    print(f"Predicted Disease: {predicted_disease}")
                    print(f"Confidence: {confidence*100:.2f}%")
                    print(f"Model Probability: {model_prob*100:.2f}%")
                    print(f"Symptom Match Score: {symptom_score*100:.2f}%")
                    
                    # Check if prediction matches expected disease
                    if test_case['expected']:
                        if predicted_disease == test_case['expected']:
                            print("✅ Prediction matches expected disease")
                            correct_predictions += 1
                        else:
                            print(f"❌ Expected {test_case['expected']}")
                    else:
                        print("ℹ️ Mixed symptoms case - no specific expected disease")
                        
                    total_confidence += confidence
                    
                    # Show other predictions
                    if result.get('other_predictions'):
                        print("\nOther possible diseases:")
                        for pred in result['other_predictions']:
                            print(f"- {pred['disease']} ({pred['confidence']*100:.2f}%)")
                    
                    # Show suggested symptoms
                    if result.get('suggested_symptoms'):
                        print("\nSuggested additional symptoms to check:")
                        print(", ".join(result['suggested_symptoms']))
                else:
                    print("❌ No prediction received")
            else:
                print(f"❌ Error: {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("-" * 50)
    
    # Calculate and show statistics
    accuracy = (correct_predictions / total_cases) * 100
    avg_confidence = (total_confidence / total_cases) * 100
    
    print("\n=== Test Results Summary ===")
    print(f"Total Test Cases: {total_cases}")
    print(f"Correct Predictions: {correct_predictions}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Average Confidence: {avg_confidence:.2f}%")

if __name__ == "__main__":
    run_test_cases() 