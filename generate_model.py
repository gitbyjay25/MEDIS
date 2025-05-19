import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Define the diseases and their symptoms
disease_data = {
    'Heart Attack': ['chest pain', 'sweating', 'vomiting', 'breathlessness', 'anxiety', 'fatigue', 'arm pain', 'dizziness'],
    'GERD': ['chest pain', 'stomach pain', 'acid reflux', 'heartburn', 'nausea', 'difficulty swallowing'],
    'Hypoglycemia': ['anxiety', 'sweating', 'hunger', 'dizziness', 'confusion', 'weakness'],
    'Migraine': ['headache', 'nausea', 'sensitivity to light', 'sensitivity to sound', 'visual aura', 'vomiting'],
    'Bronchitis': ['cough', 'mucus', 'fatigue', 'chest discomfort', 'shortness of breath', 'fever'],
    'UTI': ['frequent urination', 'burning sensation', 'pelvic pain', 'cloudy urine', 'strong odor', 'urgency'],
    'Gastritis': ['stomach pain', 'nausea', 'bloating', 'indigestion', 'loss of appetite', 'vomiting'],
    'Asthma': ['wheezing', 'coughing', 'shortness of breath', 'chest tightness', 'difficulty breathing', 'anxiety'],
    'Sinusitis': ['nasal congestion', 'facial pain', 'headache', 'cough', 'loss of smell', 'fatigue'],
    'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'stomach cramps', 'fever', 'weakness'],
    'Ear Infection': ['ear pain', 'hearing problems', 'fever', 'ear discharge', 'balance problems', 'headache'],
    'Conjunctivitis': ['red eyes', 'itching', 'discharge', 'tearing', 'burning sensation', 'sensitivity to light'],
    'Pneumonia': ['cough', 'fever', 'difficulty breathing', 'chest pain', 'fatigue', 'confusion'],
    'Diabetes': ['frequent urination', 'excessive thirst', 'hunger', 'fatigue', 'blurred vision', 'slow healing'],
    'Hypertension': ['headache', 'dizziness', 'chest pain', 'shortness of breath', 'nosebleeds', 'anxiety']
}

# Create a list of all unique symptoms
all_symptoms = set()
for symptoms in disease_data.values():
    all_symptoms.update(symptoms)

# Convert to sorted list for consistency
all_symptoms = sorted(list(all_symptoms))

# Create a mapping of diseases to their symptom vectors
disease_symptom_map = {}
for disease, symptoms in disease_data.items():
    # Create a binary vector for symptoms
    symptom_vector = np.zeros(len(all_symptoms))
    for symptom in symptoms:
        symptom_vector[all_symptoms.index(symptom)] = 1
    disease_symptom_map[disease] = symptom_vector

# Save the disease symptom map and symptom list
os.makedirs('models', exist_ok=True)
joblib.dump(disease_symptom_map, 'models/disease_symptom_map.pkl')
joblib.dump(all_symptoms, 'models/symptoms_list.pkl')

print("Model files generated successfully!")
print(f"Total diseases: {len(disease_data)}")
print(f"Total unique symptoms: {len(all_symptoms)}") 