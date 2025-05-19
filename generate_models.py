import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Create comprehensive symptom list with standardized names
symptoms = [
    # Pain related
    'headache', 'body_pain', 'muscle_pain', 'joint_pain', 'neck_pain',
    'back_pain', 'chest_pain', 'stomach_pain', 'abdominal_pain',
    'throat_pain', 'ear_pain', 'throbbing_headache',
    
    # Respiratory related
    'cough', 'dry_cough', 'productive_cough', 'wheezing', 'shortness_of_breath',
    'breathlessness', 'difficulty_breathing', 'rapid_breathing', 'shallow_breathing',
    'labored_breathing', 'sneezing', 'runny_nose', 'stuffy_nose', 'sore_throat',
    
    # Digestive related
    'nausea', 'vomiting', 'diarrhea', 'constipation', 'bloating',
    'indigestion', 'heartburn', 'acid_reflux', 'loss_of_appetite',
    'increased_appetite', 'difficulty_swallowing',
    
    # Temperature related
    'fever', 'high_fever', 'mild_fever', 'chills', 'night_sweats',
    'hot_flashes', 'cold_sweats',
    
    # Neurological related
    'dizziness', 'lightheadedness', 'fainting', 'confusion',
    'memory_problems', 'difficulty_concentrating', 'seizures',
    'tremors', 'numbness', 'tingling', 'weakness', 'paralysis',
    
    # Skin related
    'rash', 'itching', 'hives', 'swelling', 'redness',
    'bruising', 'dry_skin', 'excessive_sweating', 'pale_skin',
    'yellowing_skin', 'bluish_skin',
    
    # Vision related
    'blurred_vision', 'double_vision', 'vision_loss',
    'eye_pain', 'eye_redness', 'sensitivity_to_light',
    'watery_eyes', 'dry_eyes',
    
    # Hearing related
    'hearing_loss', 'ringing_in_ears', 'ear_pain',
    'ear_discharge', 'vertigo', 'sensitivity_to_sound',
    
    # Mental health related
    'anxiety', 'depression', 'mood_swings', 'irritability',
    'agitation', 'sleep_problems', 'insomnia', 'fatigue',
    'restlessness', 'lethargy',
    
    # Cardiovascular related
    'palpitations', 'irregular_heartbeat', 'rapid_heartbeat',
    'slow_heartbeat', 'chest_tightness', 'chest_pressure',
    'swelling_extremities',
    
    # Urinary related
    'frequent_urination', 'painful_urination', 'blood_in_urine',
    'dark_urine', 'foamy_urine', 'urinary_urgency',
    
    # Musculoskeletal related
    'muscle_weakness', 'muscle_stiffness', 'joint_stiffness',
    'joint_swelling', 'limited_mobility', 'coordination_problems',
    
    # General symptoms
    'weight_loss', 'weight_gain', 'excessive_thirst',
    'dehydration', 'malaise', 'weakness', 'dizziness',
    'sweating', 'fatigue', 'tiredness',
    
    # Cognitive related
    'confusion', 'disorientation', 'memory_loss',
    'difficulty_speaking', 'slurred_speech',
    
    # Respiratory sounds
    'wheezing', 'crackling', 'stridor',
    
    # Additional symptoms
    'loss_of_smell', 'loss_of_taste', 'metallic_taste',
    'excessive_salivation', 'dry_mouth', 'bad_breath',
    'hoarseness', 'voice_changes', 'difficulty_speaking',
    'swallowing_problems', 'neck_stiffness', 'jaw_pain',
    'tooth_pain', 'bleeding_gums', 'mouth_sores'
]

# Remove duplicates while preserving order
symptoms = list(dict.fromkeys(symptoms))

# Ensure exactly 132 symptoms
if len(symptoms) > 132:
    symptoms = symptoms[:132]
elif len(symptoms) < 132:
    # Add numbered placeholder symptoms if needed
    for i in range(len(symptoms), 132):
        symptoms.append(f'symptom_{i+1}')

print(f"Number of symptoms: {len(symptoms)}")

diseases = [
    'Common Cold', 'Flu', 'Migraine', 'COVID-19', 'Bronchitis', 
    'Gastritis', 'Sinusitis', 'Pneumonia', 'Heart Attack', 'Asthma',
    'GERD', 'Hypertension', 'Diabetes', 'Arthritis', 'Depression',
    'Anxiety', 'UTI', 'Food Poisoning', 'Allergies', 'Anemia'
]

# Create disease-symptom mapping
disease_symptom_map = {
    'Common Cold': ['headache', 'cough', 'sneezing', 'fatigue', 'sore_throat', 'runny_nose', 'congestion'],
    'Flu': ['fever', 'body_pain', 'fatigue', 'cough', 'headache', 'muscle_pain', 'chills'],
    'Migraine': ['throbbing_headache', 'sensitivity_to_light', 'sensitivity_to_sound', 'nausea', 'vomiting'],
    'COVID-19': ['fever', 'cough', 'fatigue', 'loss_of_smell', 'loss_of_taste', 'shortness_of_breath'],
    'Bronchitis': ['cough', 'chest_pain', 'fatigue', 'shortness_of_breath', 'wheezing'],
    'Gastritis': ['stomach_pain', 'nausea', 'vomiting', 'bloating', 'loss_of_appetite'],
    'Sinusitis': ['headache', 'nasal_congestion', 'facial_pain', 'loss_of_smell', 'cough'],
    'Pneumonia': ['fever', 'cough', 'shortness_of_breath', 'chest_pain', 'fatigue'],
    'Heart Attack': ['chest_pain', 'shortness_of_breath', 'sweating', 'nausea', 'anxiety'],
    'Asthma': ['wheezing', 'shortness_of_breath', 'chest_tightness', 'cough', 'fatigue'],
    'GERD': ['heartburn', 'chest_pain', 'difficulty_swallowing', 'regurgitation', 'nausea'],
    'Hypertension': ['headache', 'dizziness', 'vision_problems', 'chest_pain', 'fatigue'],
    'Diabetes': ['excessive_thirst', 'frequent_urination', 'fatigue', 'blurred_vision', 'weight_loss'],
    'Arthritis': ['joint_pain', 'joint_stiffness', 'swelling', 'limited_mobility', 'fatigue'],
    'Depression': ['fatigue', 'sleep_problems', 'loss_of_appetite', 'difficulty_concentrating', 'mood_changes'],
    'Anxiety': ['restlessness', 'rapid_heartbeat', 'sweating', 'difficulty_concentrating', 'sleep_problems'],
    'UTI': ['frequent_urination', 'painful_urination', 'urgency', 'cloudy_urine', 'pelvic_pain'],
    'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'stomach_pain', 'fever'],
    'Allergies': ['sneezing', 'runny_nose', 'itchy_eyes', 'rash', 'difficulty_breathing'],
    'Anemia': ['fatigue', 'weakness', 'pale_skin', 'shortness_of_breath', 'dizziness']
}

# Create training data
n_samples = 5000  # Increased number of samples
X = np.zeros((n_samples, len(symptoms)))
y = []

for i in range(n_samples):
    # Randomly select a disease
    disease = np.random.choice(diseases)
    y.append(disease)
    
    # Add its common symptoms with high probability
    disease_symptoms = disease_symptom_map[disease]
    for symptom in disease_symptoms:
        if symptom in symptoms:  # Make sure symptom is in our feature list
            if np.random.random() > 0.2:  # 80% chance of having each typical symptom
                X[i, symptoms.index(symptom)] = 1
    
    # Add some random symptoms (noise)
    for j in range(len(symptoms)):
        if X[i, j] == 0 and np.random.random() < 0.1:  # 10% chance of random symptoms
            X[i, j] = 1

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Create label encoder
le = LabelEncoder()
le.fit(diseases)

# Save all required files
joblib.dump(model, 'models/disease_prediction_model.pkl')
joblib.dump(symptoms, 'models/symptom_columns.pkl')
joblib.dump(le, 'models/label_encoder.pkl')
joblib.dump(disease_symptom_map, 'models/disease_symptom_map.pkl')

print("Model files generated successfully!")
print(f"Number of symptoms (features): {len(symptoms)}")
print(f"Number of diseases (classes): {len(diseases)}")
print(f"Training samples: {n_samples}")
print("\nSymptom list preview:")
for i, symptom in enumerate(symptoms[:10], 1):
    print(f"{i}. {symptom}")
print("...") 