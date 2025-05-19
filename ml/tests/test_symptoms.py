import joblib
import numpy as np
import os
from disease_prediction_v2 import predict_diseases, get_suggested_symptoms, AGE_GROUPS, SEASONS

def test_symptoms(symptoms):
    # Load the model and required files
    model = joblib.load("models/disease_prediction_model.pkl")
    symptom_columns = joblib.load("models/symptom_columns.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    
    # Create input vector
    input_vector = np.zeros(len(symptom_columns))
    
    # Set 1 for present symptoms
    for symptom in symptoms:
        symptom = symptom.lower().replace(' ', '_')
        if symptom in symptom_columns:
            input_vector[symptom_columns.index(symptom)] = 1
    
    # Get predictions with probabilities
    predictions = model.predict_proba([input_vector])[0]
    
    # Get top 3 predictions
    top_3_indices = predictions.argsort()[-3:][::-1]
    
    print("\nTop 3 possible diseases based on symptoms:")
    print("----------------------------------------")
    for idx in top_3_indices:
        disease = label_encoder.inverse_transform([idx])[0]
        probability = predictions[idx] * 100
        print(f"{disease}: {probability:.1f}%")

def test_specific_symptoms():
    # Test with malaria symptoms
    symptoms = [
        "periodic_fever",
        "chills",
        "sweating",
        "severe_headache",
        "nausea",
        "body_ache",
        "fatigue",
        "vomiting"
    ]
    
    print("\n=== Testing Specific Symptoms ===")
    print("\nSymptoms being tested:", ", ".join(symptoms))
    
    predictions = predict_diseases(symptoms)
    
    print("\nDisease Predictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print(f"Description: {pred['description']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
        
    suggested = get_suggested_symptoms(symptoms)
    if suggested:
        print("\nSuggested additional symptoms to check:", ", ".join(suggested))

def test_multiple_cases():
    test_cases = [
        {
            "name": "Tuberculosis Symptoms",
            "symptoms": [
                "persistent_cough",
                "coughing_blood",
                "chest_pain",
                "night_sweats",
                "fatigue",
                "fever",
                "weight_loss"
            ]
        },
        {
            "name": "Jaundice Symptoms",
            "symptoms": [
                "yellowing_skin",
                "yellowing_eyes",
                "dark_urine",
                "abdominal_pain",
                "fatigue",
                "nausea"
            ]
        },
        {
            "name": "Common Cold Symptoms",
            "symptoms": [
                "runny_nose",
                "sore_throat",
                "congestion",
                "cough",
                "mild_fever",
                "sneezing"
            ]
        }
    ]
    
    print("\n=== MEDIS Disease Prediction System V2.0 ===")
    
    for test_case in test_cases:
        print(f"\nTest Case - {test_case['name']}:")
        print("Symptoms:", ", ".join(test_case['symptoms']))
        
        predictions = predict_diseases(test_case['symptoms'])
        
        print("\nPredictions:")
        for pred in predictions:
            print(f"\nDisease: {pred['disease']}")
            print(f"Confidence: {pred['confidence']}%")
            print(f"Danger Level: {pred['danger_level']}")
            print(f"Description: {pred['description']}")
            print("Matching Symptoms:")
            print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
            print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
        
        suggested = get_suggested_symptoms(test_case['symptoms'])
        if suggested:
            print("\nSuggested additional symptoms to check:", ", ".join(suggested))
        
        print("\n" + "="*50)

def test_typhoid():
    print("\n=== MEDIS Disease Prediction System V2.0 ===")
    print("\nTesting for Typhoid Symptoms")
    print("=" * 40)

    # Typhoid symptoms
    typhoid_symptoms = [
        "high_fever",          # Critical
        "weakness",           # Critical
        "abdominal_pain",     # Critical
        "headache",           # High Priority
        "loss_of_appetite",   # High Priority
        "diarrhea",          # High Priority
        "fatigue",           # Medium Priority
        "nausea"             # Medium Priority
    ]
    
    print("\nSymptoms being tested:", ", ".join(typhoid_symptoms))
    predictions = predict_diseases(typhoid_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print(f"Description: {pred['description']}")
        print("\nMatching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
        
    suggested = get_suggested_symptoms(typhoid_symptoms)
    if suggested:
        print("\nSuggested additional symptoms to check:", ", ".join(suggested))

def test_advanced_prediction():
    print("\n=== MEDIS Disease Prediction System V2.0 (Advanced) ===")
    print("=" * 50)

    # Test cases with different scenarios
    test_cases = [
        {
            "name": "Adult Typhoid Case (Summer)",
            "symptoms": [
                "high_fever",
                "weakness",
                "abdominal_pain",
                "headache",
                "loss_of_appetite",
                "diarrhea",
                "fatigue",
                "nausea",
                "rose_spots",  # Adult-specific symptom
                "enlarged_spleen"  # Adult-specific symptom
            ],
            "age_group": "ADULT",
            "season": "SUMMER"
        },
        {
            "name": "Child Malaria Case (Monsoon)",
            "symptoms": [
                "periodic_fever",
                "chills",
                "sweating",
                "severe_headache",
                "nausea",
                "body_ache",
                "fatigue",
                "severe_anemia",  # Child-specific symptom
                "rapid_breathing"  # Child-specific symptom
            ],
            "age_group": "CHILD",
            "season": "MONSOON"
        }
    ]
    
    for case in test_cases:
        print(f"\nTest Case: {case['name']}")
        print(f"Age Group: {case['age_group']} ({AGE_GROUPS[case['age_group']]} years)")
        print(f"Season: {case['season']}")
        print(f"Symptoms: {', '.join(case['symptoms'])}")
        
        predictions = predict_diseases(
            case['symptoms'],
            age_group=case['age_group'],
            season=case['season']
        )
        
        print("\nPredictions:")
        for pred in predictions:
            print(f"\nDisease: {pred['disease']}")
            print(f"Confidence: {pred['confidence']}%")
            print(f"Danger Level: {pred['danger_level']}")
            print(f"Description: {pred['description']}")
            
            if pred.get("seasonal_match"):
                print("\nSeasonal Factors:")
                for factor in pred["seasonal_factors"]:
                    print(f"- {factor}")
            
            if "age_specific_symptoms" in pred:
                print(f"\nAge-Specific Symptoms for {case['age_group']}:")
                for symptom in pred["age_specific_symptoms"]:
                    print(f"- {symptom}")
            
            print("\nMatching Symptoms:")
            print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
            print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
            
            print("\nPossible Complications:")
            for comp in pred['complications']:
                print(f"- {comp}")
            
            print("\nTreatment Recommendations:")
            if 'medications' in pred['treatment_recommendations']:
                print("\nMedications:")
                for med in pred['treatment_recommendations']['medications']:
                    print(f"- {med['name']} (Duration: {med['duration']})")
            
            if 'lifestyle' in pred['treatment_recommendations']:
                print("\nLifestyle Changes:")
                for change in pred['treatment_recommendations']['lifestyle']:
                    print(f"- {change}")
            
            if 'prevention' in pred['treatment_recommendations']:
                print("\nPreventive Measures:")
                for measure in pred['treatment_recommendations']['prevention']:
                    print(f"- {measure}")
            
            print("\nTypical Duration:")
            duration = pred['symptom_duration']
            print(f"- Onset Period: {duration['onset_period']}")
            print(f"- Critical Period: {duration['critical_period']}")
            print(f"- Recovery Period: {duration['recovery_period']}")
        
        suggested = get_suggested_symptoms(case['symptoms'], case['age_group'])
        if suggested:
            print("\nSuggested additional symptoms to check:", ", ".join(suggested))
        
        print("\n" + "="*50)

def test_skin_conditions():
    print("\n=== Testing Skin Condition Symptoms ===")
    print("=" * 40)

    skin_symptoms = [
        "skin_rash",
        "pus_filled_pimples",
        "scurring"
    ]
    
    print("\nSymptoms being tested:", ", ".join(skin_symptoms))
    predictions = predict_diseases(skin_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print(f"Description: {pred['description']}")
        print("\nMatching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
        
        if 'complications' in pred:
            print("\nPossible Complications:")
            for comp in pred['complications']:
                print(f"- {comp}")
            
        if 'treatment_recommendations' in pred:
            print("\nTreatment Recommendations:")
            if 'medications' in pred['treatment_recommendations']:
                print("\nMedications:")
                for med in pred['treatment_recommendations']['medications']:
                    print(f"- {med['name']} (Duration: {med['duration']})")
            
            if 'lifestyle' in pred['treatment_recommendations']:
                print("\nLifestyle Changes:")
                for change in pred['treatment_recommendations']['lifestyle']:
                    print(f"- {change}")
        
    suggested = get_suggested_symptoms(skin_symptoms)
    if suggested:
        print("\nSuggested additional symptoms to check:", ", ".join(suggested))

def test_multiple_conditions():
    print("\n=== Testing Multiple Conditions ===")
    print("=" * 50)
    
    test_cases = [
        {
            "name": "Jaundice Test",
            "symptoms": [
                "yellowing_skin",
                "yellowing_eyes",
                "dark_urine",
                "abdominal_pain",
                "fatigue",
                "nausea",
                "loss_of_appetite"
            ]
        },
        {
            "name": "Tuberculosis Test",
            "symptoms": [
                "persistent_cough",
                "coughing_blood",
                "chest_pain",
                "weight_loss",
                "night_sweats",
                "fatigue",
                "fever"
            ]
        },
        {
            "name": "Arthritis Test",
            "symptoms": [
                "joint_pain",
                "joint_stiffness",
                "joint_swelling",
                "reduced_joint_mobility",
                "morning_stiffness",
                "muscle_weakness",
                "fatigue"
            ]
        },
        {
            "name": "AIDS Test",
            "symptoms": [
                "severe_weight_loss",
                "recurring_fever",
                "extreme_fatigue",
                "swollen_lymph_nodes",
                "night_sweats",
                "skin_lesions",
                "frequent_infections"
            ]
        }
    ]
    
    for case in test_cases:
        print(f"\n{case['name']}:")
        print("-" * len(case['name']))
        print("Symptoms:", ", ".join(case['symptoms']))
        
        predictions = predict_diseases(case['symptoms'])
        
        print("\nPredictions:")
        for pred in predictions:
            print(f"\nDisease: {pred['disease']}")
            print(f"Confidence: {pred['confidence']}%")
            print(f"Danger Level: {pred['danger_level']}")
            print(f"Description: {pred['description']}")
            
            print("\nMatching Symptoms:")
            print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
            print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
            
            if 'complications' in pred:
                print("\nPossible Complications:")
                for comp in pred['complications']:
                    print(f"- {comp}")
            
            if 'treatment_recommendations' in pred:
                print("\nTreatment Recommendations:")
                if 'medications' in pred['treatment_recommendations']:
                    print("\nMedications:")
                    for med in pred['treatment_recommendations']['medications']:
                        print(f"- {med['name']} ({med['duration']})")
                
                if 'lifestyle' in pred['treatment_recommendations']:
                    print("\nLifestyle Changes:")
                    for change in pred['treatment_recommendations']['lifestyle']:
                        print(f"- {change}")
                        
                if 'prevention' in pred['treatment_recommendations']:
                    print("\nPreventive Measures:")
                    for measure in pred['treatment_recommendations']['prevention']:
                        print(f"- {measure}")
            
            if 'symptom_duration' in pred:
                print("\nTypical Duration:")
                duration = pred['symptom_duration']
                print(f"- Onset Period: {duration['onset_period']}")
                print(f"- Critical Period: {duration['critical_period']}")
                print(f"- Recovery Period: {duration['recovery_period']}")
        
        print("\n" + "="*50)

def test_chicken_pox():
    print("\n=== Testing Chicken Pox Symptoms ===")
    print("=" * 40)

    # Chicken Pox symptoms
    chicken_pox_symptoms = [
        "skin_rash",          # Critical
        "red_spots",          # Critical
        "itching",            # Critical
        "mild_fever",         # High Priority
        "fatigue",            # High Priority
        "swelled_lymph_nodes" # High Priority
    ]
    
    print("\nSymptoms being tested:", ", ".join(chicken_pox_symptoms))
    predictions = predict_diseases(chicken_pox_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print(f"Description: {pred['description']}")
        print("\nMatching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))
        
    suggested = get_suggested_symptoms(chicken_pox_symptoms)
    if suggested:
        print("\nSuggested additional symptoms to check:", ", ".join(suggested))

if __name__ == "__main__":
    test_multiple_cases()
    test_typhoid()
    test_advanced_prediction()
    test_skin_conditions()
    test_multiple_conditions()
    test_chicken_pox() 