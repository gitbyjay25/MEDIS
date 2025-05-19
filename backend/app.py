"""
MEDIS backend server.
"""

import os
import sys
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import traceback
from routes.nearby import nearby_bp
from datetime import datetime
import json
import critical_diseases
from critical_diseases import check_critical_diseases
from disease_recommendations import get_recommendations

# Add parent directory to Python path for model imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Set default secret key if not in environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'medis_default_secret_key')

# Register blueprints
app.register_blueprint(nearby_bp)

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Load model and required files at startup
try:
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load model and required files
    model_path = os.path.join(parent_dir, "models/disease_prediction_model.pkl")
    symptom_columns_path = os.path.join(parent_dir, "models/symptom_columns.pkl")
    label_encoder_path = os.path.join(parent_dir, "models/label_encoder.pkl")
    disease_map_path = os.path.join(parent_dir, "models/disease_symptom_map.pkl")
    
    model = joblib.load(model_path)
    symptom_columns = joblib.load(symptom_columns_path)
    label_encoder = joblib.load(label_encoder_path)
    disease_symptom_map = joblib.load(disease_map_path)
    
    logger.info(f"Model loaded successfully")
    logger.info(f"Number of symptom features: {len(symptom_columns)}")
    logger.info(f"Symptom columns: {symptom_columns}")
    logger.info(f"Number of disease classes: {len(label_encoder.classes_)}")
    
except Exception as e:
    logger.error(f"Error loading model files: {e}")
    logger.error(traceback.format_exc())
    raise

# Define comprehensive symptom mapping
symptom_mapping = {
    # Pain related
    'body pain': 'body_pain',
    'body ache': 'body_pain',
    'muscle pain': 'muscle_pain',
    'joint pain': 'joint_pain',
    'headache': 'headache',
    'head pain': 'headache',
    'throbbing headache': 'severe_headache',
    'severe headache': 'severe_headache',
    'pulsating headache': 'severe_headache',
    'neck pain': 'neck_pain',
    'chest pain': 'chest_pain',
    'severe chest pain': 'severe_chest_pain',  # Added for heart attack
    'crushing chest pain': 'severe_chest_pain',  # Added for heart attack
    'chest discomfort': 'chest_discomfort',
    'chest pressure': 'chest_pressure',  # Added for heart attack
    'pressure in chest': 'chest_pressure',  # Added for heart attack
    'chest tightness': 'chest_pressure',  # Added for heart attack
    'stomach pain': 'stomach_pain',
    'abdominal pain': 'abdominal_pain',
    'belly pain': 'abdominal_pain',
    'facial pain': 'facial_pain',
    'eye pain': 'eye_pain',
    'sinus pressure': 'sinus_pressure',
    'pain behind eyes': 'pain_behind_eyes',
    'right upper abdominal pain': 'right_upper_abdominal_pain',
    'left arm pain': 'left_arm_pain',  # Added for heart attack
    'arm pain': 'left_arm_pain',  # Added for heart attack
    'pain in left arm': 'left_arm_pain',  # Added for heart attack
    'radiating arm pain': 'left_arm_pain',  # Added for heart attack
    'jaw pain': 'jaw_pain',  # Added for heart attack
    'pain in jaw': 'jaw_pain',  # Added for heart attack
    
    # Joint related - for Arthritis
    'joint stiffness': 'joint_stiffness',
    'joint swelling': 'joint_swelling',
    'reduced joint mobility': 'reduced_joint_mobility',
    'morning stiffness': 'morning_stiffness',
    'joint warmth': 'joint_warmth',
    'muscle and joint pain': 'muscle_and_joint_pain',
    'muscle weakness': 'muscle_weakness',
    'joint redness': 'joint_redness',
    'stiff joints': 'joint_stiffness',
    'painful joints': 'joint_pain',
    'swollen joints': 'joint_swelling',
    'difficulty moving joints': 'reduced_joint_mobility',
    
    # Fever related
    'fever': 'fever',
    'high fever': 'high_fever',
    'mild fever': 'mild_fever',
    'periodic fever': 'periodic_fever',
    'persistent fever': 'persistent_fever',
    'intermittent fever': 'intermittent_fever',
    'elevated temperature': 'fever',
    
    # Respiratory related
    'cough': 'cough',
    'dry cough': 'dry_cough',
    'persistent cough': 'persistent_cough',
    'coughing blood': 'coughing_blood',
    'coughing': 'cough',
    'shortness of breath': 'shortness_of_breath',
    'breathlessness': 'shortness_of_breath',
    'difficulty breathing': 'shortness_of_breath',
    'shortness of breathe': 'shortness_of_breath',  # Added corrected spelling
    
    # Heart attack/cardiac related
    'cold sweat': 'cold_sweats',  # Added for heart attack
    'cold sweats': 'cold_sweats',  # Added for heart attack
    'swaeting': 'sweating',  # Added common misspelling
    'cold sweet': 'cold_sweats',  # Added common misspelling
    'sweating': 'sweating',
    'excessive sweating': 'sweating',
    'anxiety': 'anxiety',
    'feeling of doom': 'anxiety',  # Added for heart attack
    'feeling anxious': 'anxiety',
    
    # Digestive/Nausea related
    'nausea': 'nausea',
    'feeling sick': 'nausea',
    'vomiting': 'vomiting',
    'throwing up': 'vomiting',
    
    # Additional mappings for other symptoms
    'weakness': 'weakness',
    'tiredness': 'fatigue',
    'exhaustion': 'fatigue',
    'lethargy': 'lethargy',
    'malaise': 'malaise',
    'chills': 'chills',
    'sweating': 'sweating',
    'night sweats': 'night_sweats',
    'excessive sweating': 'sweating',
    'dehydration': 'dehydration',
    'dark urine': 'dark_urine',
    'yellow urine': 'yellow_urine',
    'sunken eyes': 'sunken_eyes',
    'weight loss': 'weight_loss',
    'rose spots': 'rose_spots',
    'bleeding gums': 'bleeding_gums',
    'nose bleeds': 'nose_bleeds',
    
    # Circulatory/Heart related
    'irregular heartbeat': 'irregular_heartbeat',
    'palpitations': 'irregular_heartbeat',  # Added for heart conditions
    'heart racing': 'irregular_heartbeat',  # Added for heart conditions
    'rapid heartbeat': 'irregular_heartbeat',  # Added for heart conditions
    'cold hands': 'cold_hands',
    'cold feet': 'cold_hands',
    
    # Neurological related
    'dizziness': 'dizziness',
    'lightheaded': 'dizziness',
    'lightheadedness': 'dizziness',  # Added for heart attack
    'confusion': 'confusion',
    'altered sensorium': 'altered_sensorium',
    'lack of concentration': 'lack_of_concentration',
    'loss of balance': 'loss_of_balance'
}

def standardize_symptom(symptom):
    """Standardize symptom names"""
    symptom = symptom.lower().strip()
    # First try direct mapping
    if symptom in symptom_mapping:
        return symptom_mapping[symptom]
    # Try replacing spaces with underscores
    normalized = symptom.replace(' ', '_')
    if normalized in symptom_columns:
        return normalized
    # Try the original mapping as fallback
    return symptom_mapping.get(symptom, normalized)

# Define a blacklist of rare diseases that should not be predicted for common symptoms
rare_diseases_blacklist = ['heart attack', 'stroke', 'cancer', 'kidney failure', 'liver failure']

# Load and process disease-symptoms mapping
try:
    df = pd.read_csv(os.path.join(parent_dir, "data/DiseaseAndSymptoms.csv"))
    disease_symptoms_map = {}

    for _, row in df.iterrows():
        disease = row['Disease']
        symptoms = [s.strip() for s in row[1:] if pd.notna(s) and s.strip() != '']
        if disease not in disease_symptoms_map:
            disease_symptoms_map[disease] = set()
        standardized = {standardize_symptom(s) for s in symptoms}
        disease_symptoms_map[disease].update(standardized)
    logger.info("Successfully loaded disease-symptoms mapping")
except Exception as e:
    logger.error(f"Error loading disease-symptoms mapping: {e}")
    raise

# Load and process disease-precautions mapping
try:
    df_precautions = pd.read_csv(os.path.join(parent_dir, "data/Disease precaution.csv"))
    precaution_map = {}

    for _, row in df_precautions.iterrows():
        disease = row['Disease']
        precautions = [p.strip() for p in row[1:] if pd.notna(p) and p.strip() != '']
        if disease not in precaution_map:
            precaution_map[disease] = precautions
    logger.info("Successfully loaded disease-precautions mapping")
except Exception as e:
    logger.error(f"Error loading disease-precautions mapping: {e}")
    raise

logger.info("Medicine recommendation system initialized successfully")

# Load and process disease data with age and gender considerations
try:
    df_diseases = pd.read_csv(os.path.join(parent_dir, "data/disease_data.csv"))
    disease_info_map = {}

    for _, row in df_diseases.iterrows():
        disease = row['Disease']
        disease_info_map[disease] = {
            'age_group': row['Common_Age_Group'],
            'gender_specific': row['Gender_Specific'],
            'common_symptoms': row['Common_Symptoms'].split(','),
            'severity': row['Severity'],
            'precautions': row['Precautions'].split(',')
        }
    logger.info("Successfully loaded disease information data")
except Exception as e:
    logger.error(f"Error loading disease information data: {e}")
    raise

# Disease name mappings
disease_name_mappings = {
    'common_cold': 'Common Cold',
    'stomach_flu': 'Gastritis',
    'food_poisoning': 'Food Poisoning',
    'bronchial asthma': 'Asthma',
    'vertigo': 'Migraine',
    'chronic cholestasis': 'Jaundice',
    'aids': 'Adult Depression',
    'impetigo': 'Impetigo',
    'gerd': 'Gastritis',
    'high_fever': 'Fever',
    'fever': 'Fever',
    'allergy': 'Allergies',
    'allergic': 'Allergies',
    'hay_fever': 'Allergies',
    'seasonal_allergy': 'Allergies',
    'migrane': 'Migraine',
    'headache': 'Migraine',
    'severe_headache': 'Migraine',
    'diabetes_mellitus': 'Diabetes',
    'type_1_diabetes': 'Diabetes',
    'type_2_diabetes': 'Diabetes',
    'arthritis': 'Arthritis',
    'rheumatoid_arthritis': 'Arthritis',
    'osteoarthritis': 'Arthritis',
    'joint_pain': 'Arthritis',
    'asthma': 'Asthma',
    'bronchitis': 'Bronchitis',
    'acute_bronchitis': 'Bronchitis',
    'chronic_bronchitis': 'Bronchitis',
    'gastroenteritis': 'Gastritis',
    'stomach_infection': 'Gastritis',
    'food_intolerance': 'Food Poisoning',
    'jaundice': 'Jaundice',
    'yellowing_skin': 'Jaundice',
    'yellow_eyes': 'Jaundice',
    'yellowish_skin': 'Jaundice',
    'yellowing_eyes': 'Jaundice',
    'viral_hepatitis': 'Hepatitis',
    'hepatitis': 'Hepatitis',
    'liver_inflammation': 'Hepatitis',
    'typhoid_fever': 'Typhoid',
    'typhoid': 'Typhoid',
    'enteric_fever': 'Typhoid',
    'dengue': 'Dengue',
    'dengue_fever': 'Dengue',
    'breakbone_fever': 'Dengue',
    'food_poisoning_symptoms': 'Food Poisoning',
    'stomach_bug': 'Food Poisoning',
    'food_sickness': 'Food Poisoning',
    'food_contamination': 'Food Poisoning'
}

def get_missing_symptoms(disease, input_symptoms):
    """Get symptoms that are common for the disease but not in input"""
    if disease not in disease_symptoms_map:
        return []
    
    # Standardize input symptoms
    standardized_input = {standardize_symptom(s) for s in input_symptoms}
    
    # Get missing symptoms (excluding those already mentioned)
    disease_symptoms = disease_symptoms_map[disease]
    missing = disease_symptoms - standardized_input
    
    # Sort and return the list of missing symptoms
    return sorted(list(missing))

def get_precautions(disease):
    """Get precautions for a given disease"""
    return precaution_map.get(disease, [])

# Define common disease groups and their typical symptoms
common_disease_groups = {
    'common_cold': {
        'symptoms': ['runny_nose', 'sneezing', 'cough', 'sore_throat', 'mild_fever', 'fatigue'],
        'min_symptoms': 2
    },
    'flu': {
        'symptoms': ['high_fever', 'body_pain', 'fatigue', 'headache', 'cough', 'sore_throat'],
        'min_symptoms': 3
    },
    'food_poisoning': {
        'symptoms': ['nausea', 'vomiting', 'diarrhea', 'stomach_pain', 'weakness'],
        'min_symptoms': 3,
        'exclude_symptoms': ['yellowing_skin', 'yellow_eyes', 'yellowish_skin', 'yellowing_eyes', 'dark_urine', 'jaundice', 
                            'pale_stools', 'clay_colored_stools', 'right_upper_abdominal_pain']
    },
    'hepatitis': {
        'symptoms': ['yellowing_skin', 'yellow_eyes', 'dark_urine', 'fatigue', 'right_upper_abdominal_pain', 'nausea', 'jaundice'],
        'min_symptoms': 3,
        'exclude_symptoms': ['diarrhea']
    },
    'jaundice': {
        'symptoms': ['yellowing_skin', 'yellow_eyes', 'dark_urine', 'pale_stools', 'fatigue', 'itching', 'jaundice'],
        'min_symptoms': 3,
        'exclude_symptoms': ['diarrhea']
    },
    'gastritis': {
        'symptoms': ['stomach pain', 'nausea', 'vomiting', 'bloating', 'indigestion'],
        'min_symptoms': 2,
        'exclude_symptoms': ['yellowing_skin', 'yellow_eyes', 'dark_urine', 'yellowish_skin', 'yellowing_eyes', 'jaundice']
    }
}

def is_age_appropriate(disease, age):
    """Check if the disease is appropriate for the given age"""
    if disease not in disease_info_map:
        return True  # If no age info, assume appropriate
    
    age_group = disease_info_map[disease]['age_group']
    if age_group == 'all':
        return True
    
    if age_group == '40+':
        return age >= 40
    
    if '-' in age_group:
        min_age, max_age = map(int, age_group.split('-'))
        return min_age <= age <= max_age
    
    return True

def is_gender_appropriate(disease, gender):
    """Check if the disease is appropriate for the given gender"""
    if disease not in disease_info_map:
        return True  # If no gender info, assume appropriate
    
    gender_specific = disease_info_map[disease]['gender_specific']
    if gender_specific == 'all':
        return True
    
    return gender.lower() == gender_specific.lower()

def calculate_symptom_match_score(input_symptoms, disease_symptoms):
    """Calculate symptom match score"""
    if not disease_symptoms:
        return 0
    matched = set(input_symptoms) & set(disease_symptoms)
    return len(matched) / len(disease_symptoms)

def adjust_confidence(base_confidence, age, gender, disease):
    """Adjust confidence based on age and gender factors"""
    confidence = base_confidence
    
    # Age-based adjustments
    if disease_info_map and disease in disease_info_map:
        age_group = disease_info_map[disease]['age_group']
        if age:
            if age_group == 'children' and age > 18:
                confidence *= 0.8
            elif age_group == 'adults' and age < 18:
                confidence *= 0.8
            elif age_group == 'elderly' and age < 60:
                confidence *= 0.8
    
    # Gender-based adjustments
    if disease_info_map and disease in disease_info_map:
        gender_specific = disease_info_map[disease]['gender_specific']
        if gender and gender_specific != 'both' and gender_specific != gender:
            confidence *= 0.7
    
        return confidence

# Disease information with detailed recommendations
disease_info = {
    'Common Cold': {
        'description': 'Viral infection of the upper respiratory tract',
        'symptoms': ['runny nose', 'sore throat', 'cough', 'congestion', 'slight body aches', 'mild headache', 'low-grade fever', 'sneezing'],
        'severity': 'low',
        'precautions': [
            'Rest and get adequate sleep',
            'Stay hydrated by drinking plenty of fluids',
            'Use over-the-counter cold medications',
            'Gargle with warm salt water for sore throat',
            'Use a humidifier to add moisture to the air',
            'Avoid close contact with others to prevent spread'
        ],
        'medicine_recommendations': [
            {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 4-6 hours', 'purpose': 'Fever and pain relief'},
            {'medicine': 'Chlorpheniramine', 'dosage': '4mg every 4-6 hours', 'purpose': 'Runny nose and sneezing'},
            {'medicine': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Cough and congestion'}
        ],
        'food_preferences': [
            'Hot soups and broths',
            'Ginger tea with honey',
            'Citrus fruits rich in vitamin C',
            'Garlic and onion for immune support',
            'Warm water with lemon and honey'
        ],
        'exercises': [
            'Light walking if feeling up to it',
            'Deep breathing exercises',
            'Rest is most important'
        ]
    },
    'Flu': {
        'description': 'Influenza viral infection affecting respiratory system',
        'symptoms': ['high fever', 'body aches', 'fatigue', 'headache', 'cough', 'sore throat'],
        'severity': 'medium',
        'precautions': [
            'Rest and stay home',
            'Stay hydrated',
            'Use fever reducers',
            'Cover mouth when coughing',
            'Wash hands frequently'
        ],
        'medicine_recommendations': [
            {'medicine': 'Oseltamivir (Tamiflu)', 'dosage': 'As prescribed', 'purpose': 'Antiviral medication'},
            {'medicine': 'Ibuprofen', 'dosage': '400mg every 6-8 hours', 'purpose': 'Fever and pain relief'},
            {'medicine': 'Decongestant', 'dosage': 'As directed', 'purpose': 'Nasal congestion'}
        ],
        'food_preferences': [
            'Clear broths',
            'Chicken soup',
            'Fresh fruits',
            'Herbal teas',
            'Light, easily digestible foods'
        ],
        'exercises': [
            'Rest is essential',
            'Light stretching when feeling better',
            'Gradual return to activity'
        ]
    },
    'Pneumonia': {
        'description': 'Infection causing inflammation of the air sacs in lungs',
        'symptoms': ['chest pain', 'cough with phlegm', 'fever', 'difficulty breathing', 'fatigue'],
        'severity': 'high',
        'precautions': [
            'Complete prescribed antibiotics',
            'Get plenty of rest',
            'Stay hydrated',
            'Use breathing exercises',
            'Follow up with doctor'
        ],
        'medicine_recommendations': [
            {'medicine': 'Antibiotics', 'dosage': 'As prescribed', 'purpose': 'Treat bacterial infection'},
            {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever reduction'},
            {'medicine': 'Expectorant', 'dosage': 'As directed', 'purpose': 'Loosen mucus'}
        ],
        'food_preferences': [
            'High-protein foods',
            'Vitamin C rich fruits',
            'Warm soups',
            'Yogurt',
            'Plenty of fluids'
        ],
        'exercises': [
            'Deep breathing exercises',
            'Gentle walking when approved',
            'Spirometry exercises',
            'Gradual increase in activity'
        ]
    },
    'Bronchitis': {
        'description': 'Inflammation of the bronchial tubes',
        'symptoms': ['persistent cough', 'mucus production', 'fatigue', 'mild fever', 'chest discomfort'],
        'severity': 'medium',
        'precautions': [
            'Avoid smoking and secondhand smoke',
            'Use a humidifier',
            'Get plenty of rest',
            'Stay hydrated',
            'Practice good hand hygiene'
        ],
        'medicine_recommendations': [
            {'medicine': 'Dextromethorphan', 'dosage': 'As directed', 'purpose': 'Cough suppression'},
            {'medicine': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Expectorant'},
            {'medicine': 'Inhaler', 'dosage': 'As prescribed', 'purpose': 'Bronchodilation'}
        ],
        'food_preferences': [
            'Warm herbal teas',
            'Honey',
            'Ginger',
            'Citrus fruits',
            'Spicy foods to clear sinuses'
        ],
        'exercises': [
            'Pursed lip breathing',
            'Diaphragmatic breathing',
            'Light walking',
            'Avoid strenuous activity'
        ]
    },
    'Gastritis': {
        'description': 'Inflammation of the stomach lining',
        'symptoms': ['stomach pain', 'nausea', 'vomiting', 'bloating', 'indigestion'],
        'severity': 'medium',
        'precautions': [
            'Avoid spicy and acidic foods',
            'Eat smaller meals',
            'Avoid alcohol',
            'Manage stress',
            'Stop smoking'
        ],
        'medicine_recommendations': [
            {'medicine': 'Omeprazole', 'dosage': '20mg once daily', 'purpose': 'Reduce acid production'},
            {'medicine': 'Antacids', 'dosage': 'As needed', 'purpose': 'Immediate acid relief'},
            {'medicine': 'Sucralfate', 'dosage': 'As prescribed', 'purpose': 'Stomach lining protection'}
        ],
        'food_preferences': [
            'Plain yogurt',
            'Bananas',
            'Rice',
            'Toast',
            'Lean proteins'
        ],
        'exercises': [
            'Gentle walking',
            'Light yoga',
            'Stress-reducing activities',
            'Avoid exercising right after meals'
        ]
    },
    'Dengue': {
        'description': 'Mosquito-borne viral infection',
        'symptoms': ['high fever', 'severe headache', 'joint pain', 'rash', 'fatigue'],
        'severity': 'high',
        'precautions': [
            'Complete bed rest',
            'Stay hydrated',
            'Monitor temperature',
            'Watch for warning signs',
            'Regular blood tests'
        ],
        'medicine_recommendations': [
            {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever and pain relief'},
            {'medicine': 'Oral rehydration salts', 'dosage': 'As needed', 'purpose': 'Maintain hydration'},
            {'medicine': 'Avoid NSAIDs', 'dosage': 'N/A', 'purpose': 'Risk of bleeding'}
        ],
        'food_preferences': [
            'Papaya leaf juice',
            'High fluid intake',
            'Easily digestible foods',
            'Vitamin C rich fruits',
            'Light soups'
        ],
        'exercises': [
            'Complete rest during fever',
            'Gentle movements when recovering',
            'Light stretching after recovery',
            'Gradual return to normal activity'
        ]
    },
    'Malaria': {
        'description': 'Parasitic infection transmitted by mosquitoes',
        'symptoms': ['fever and chills', 'headache', 'fatigue', 'muscle aches', 'nausea'],
        'severity': 'high',
        'precautions': [
            'Complete prescribed medication',
            'Rest and hydration',
            'Monitor temperature',
            'Use mosquito protection',
            'Regular check-ups'
        ],
        'medicine_recommendations': [
            {'medicine': 'Artemisinin combination therapy', 'dosage': 'As prescribed', 'purpose': 'Anti-malarial'},
            {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever management'},
            {'medicine': 'Iron supplements', 'dosage': 'As directed', 'purpose': 'Treat anemia'}
        ],
        'food_preferences': [
            'High-protein foods',
            'Iron-rich foods',
            'Fresh fruits',
            'Plenty of fluids',
            'Light, frequent meals'
        ],
        'exercises': [
            'Rest during acute phase',
            'Gentle walking during recovery',
            'Light stretching',
            'Gradual return to activity'
        ]
    },
    'Tuberculosis': {
        'description': 'Bacterial infection primarily affecting the lungs',
        'symptoms': ['persistent cough', 'weight loss', 'night sweats', 'fever', 'fatigue'],
        'severity': 'high',
        'precautions': [
            'Complete full course of medication',
            'Wear mask when in public',
            'Good ventilation',
            'Regular check-ups',
            'Isolation during initial phase'
        ],
        'medicine_recommendations': [
            {'medicine': 'Isoniazid', 'dosage': 'As prescribed', 'purpose': 'Anti-TB medication'},
            {'medicine': 'Rifampicin', 'dosage': 'As prescribed', 'purpose': 'Anti-TB medication'},
            {'medicine': 'Pyridoxine', 'dosage': 'As directed', 'purpose': 'Prevent side effects'}
        ],
        'food_preferences': [
            'High-protein diet',
            'Calorie-rich foods',
            'Fresh fruits and vegetables',
            'Milk and dairy products',
            'Adequate hydration'
        ],
        'exercises': [
            'Rest during initial phase',
            'Deep breathing exercises',
            'Gradual increase in activity',
            'Light walking when approved'
        ]
    },
    'Typhoid': {
        'description': 'Bacterial infection affecting the intestinal tract',
        'symptoms': ['high fever', 'weakness', 'stomach pain', 'headache', 'loss of appetite'],
        'severity': 'high',
        'precautions': [
            'Complete antibiotic course',
            'Strict hygiene measures',
            'Rest and hydration',
            'Avoid solid foods initially',
            'Regular temperature monitoring'
        ],
        'medicine_recommendations': [
            {'medicine': 'Ciprofloxacin', 'dosage': 'As prescribed', 'purpose': 'Antibiotic treatment'},
            {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever control'},
            {'medicine': 'ORS', 'dosage': 'As needed', 'purpose': 'Maintain hydration'}
        ],
        'food_preferences': [
            'Clear broths',
            'Soft, easily digestible foods',
            'Boiled vegetables',
            'Rice soup',
            'Plenty of fluids'
        ],
        'exercises': [
            'Complete bed rest initially',
            'Gentle movements during recovery',
            'Light walking when fever subsides',
            'Gradual return to normal activity'
        ]
    },
    'Impetigo': {
        'description': 'Bacterial skin infection',
        'symptoms': ['red sores', 'itching', 'fluid-filled blisters', 'yellow crusts', 'skin rash'],
        'severity': 'medium',
        'precautions': [
            'Keep affected area clean',
            'Avoid scratching',
            'Use separate towels',
            'Wash hands frequently',
            'Complete antibiotic course'
        ],
        'medicine_recommendations': [
            {'medicine': 'Mupirocin', 'dosage': 'Apply 3 times daily', 'purpose': 'Topical antibiotic'},
            {'medicine': 'Oral antibiotics', 'dosage': 'As prescribed', 'purpose': 'For severe cases'},
            {'medicine': 'Antiseptic wash', 'dosage': 'As directed', 'purpose': 'Clean affected area'}
        ],
        'food_preferences': [
            'Nutrient-rich foods',
            'Protein-rich diet',
            'Vitamin C rich foods',
            'Stay hydrated',
            'Avoid processed foods'
        ],
        'exercises': [
            'Light activity',
            'Avoid contact sports',
            'Keep affected area dry',
            'Avoid swimming',
            'Maintain good hygiene'
        ]
    },
    'Chicken Pox': {
        'description': 'Highly contagious viral infection causing itchy rash and fluid-filled blisters',
        'symptoms': ['fever', 'fatigue', 'itchy rash', 'blisters', 'fluid-filled blisters', 'loss of appetite', 'headache'],
        'severity': 'medium',
        'precautions': [
            'Isolate until all blisters have crusted over',
            'Avoid scratching to prevent scarring',
            'Keep skin clean and dry',
            'Use calamine lotion for itch relief',
            'Take lukewarm baths with baking soda or colloidal oatmeal',
            'Wear loose-fitting, cotton clothing'
        ],
        'medicine_recommendations': [
            {'medicine': 'Calamine lotion', 'dosage': 'Apply to affected areas as needed', 'purpose': 'Relieve itching'},
            {'medicine': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Reduce fever and pain'},
            {'medicine': 'Antihistamines', 'dosage': 'As directed', 'purpose': 'Reduce itching and help sleep'},
            {'medicine': 'Acyclovir', 'dosage': 'As prescribed', 'purpose': 'Antiviral (for severe cases)'}
        ],
        'food_preferences': [
            'Soft, bland foods that are easy to eat',
            'Cold foods like smoothies and popsicles to soothe throat',
            'Plenty of fluids to prevent dehydration',
            'Foods rich in vitamin C to boost immune system',
            'Avoid spicy or acidic foods that may irritate blisters in mouth'
        ],
        'exercises': [
            'Rest during the illness',
            'Light activities when feeling better',
            'Avoid strenuous exercise until recovery',
            'Gentle stretching during recovery phase',
            'Return to normal activity gradually after all blisters crust over'
        ]
    }
}

def get_disease_info(disease_name):
    # First check if there's a mapping
    mapped_name = disease_name_mappings.get(disease_name.lower())
    if mapped_name and mapped_name in disease_info:
        return disease_info[mapped_name]
    
    # Try exact match
    if disease_name in disease_info:
        return disease_info[disease_name]
    
    # Try case-insensitive match
    disease_name_lower = disease_name.lower()
    for key in disease_info:
        if key.lower() == disease_name_lower:
            return disease_info[key]
    
    # Try partial match
    for key in disease_info:
        if disease_name_lower in key.lower() or key.lower() in disease_name_lower:
            return disease_info[key]
    
    # If no match found, return None
    return None

def get_medicine_recommendations(disease_name, age=None, gender=None):
    """Get medicine recommendations for a disease from the disease_info dictionary"""
    disease_data = get_disease_info(disease_name)
    if not disease_data or 'medicine_recommendations' not in disease_data:
        return []
        
    recommendations = disease_data['medicine_recommendations']
    
    # Adjust dosage based on age if needed
    if age is not None:
        adjusted_recommendations = []
        for rec in recommendations:
            adjusted_rec = rec.copy()
            if age < 12:
                if 'mg' in rec['dosage']:
                    adjusted_rec['dosage'] = 'Consult pediatrician for child dosage'
            elif age > 65:
                if 'mg' in rec['dosage'] and 'as needed' not in rec['dosage'].lower():
                    try:
                        current_dose = int(''.join(filter(str.isdigit, rec['dosage'].split('-')[0])))
                        adjusted_rec['dosage'] = f"{int(current_dose * 0.75)}mg (reduced for elderly) {rec['dosage'].split('mg')[1]}"
                    except:
                        pass  # Keep original dosage if parsing fails
            adjusted_recommendations.append(adjusted_rec)
        return adjusted_recommendations
        
    return recommendations

@app.route("/")
def home():
    return "MEDIS API is running."

@app.route("/health")
def health_check():
    """Health check endpoint to verify the backend is running"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {error}")
    return jsonify({"error": "Internal server error", "details": str(error)}), 500

def standardize_symptoms(symptoms):
    """Standardize a list of symptoms"""
    return [standardize_symptom(symptom) for symptom in symptoms]

def symptoms_to_vector(standardized_symptoms):
    """Convert standardized symptoms to input vector"""
    input_vector = np.zeros(len(symptom_columns))
    for symptom in standardized_symptoms:
        if symptom in symptom_columns:
            idx = symptom_columns.index(symptom)
            input_vector[idx] = 1
    return input_vector

def validate_recommendation_fields(result):
    """Ensure all required recommendation fields are present in the result"""
    required_fields = ["medicines", "precautions", "diet", "exercise", "lifestyle"]
    
    # First add the severity field if missing
    if "severity" not in result and "danger_level" in result:
        # Add severity field based on danger level
        if result["danger_level"] == "HIGH":
            result["severity"] = "high"
        elif result["danger_level"] == "MEDIUM":
            result["severity"] = "medium"
        else:
            result["severity"] = "low"
    elif "severity" not in result:
        # Default severity
        result["severity"] = "medium"
    
    # Special case for Bronchitis
    if result['disease'] == 'Bronchitis':
        logger.info("Adding complete recommendations for Bronchitis")
        result.update({
            "medicines": [
                {"name": "Dextromethorphan", "dosage": "As directed", "purpose": "Cough suppression"},
                {"name": "Guaifenesin", "dosage": "200-400mg every 4 hours", "purpose": "Expectorant"},
                {"name": "Inhaler", "dosage": "As prescribed", "purpose": "Bronchodilation"}
            ],
            "precautions": [
                "Avoid smoking and secondhand smoke",
                "Use a humidifier",
                "Get plenty of rest",
                "Stay hydrated",
                "Practice good hand hygiene"
            ],
            "diet": [
                "Warm herbal teas",
                "Honey",
                "Ginger",
                "Citrus fruits",
                "Spicy foods to clear sinuses"
            ],
            "exercise": [
                "Pursed lip breathing",
                "Diaphragmatic breathing",
                "Light walking",
                "Avoid strenuous activity"
            ],
            "lifestyle": [
                "Avoid irritants like smoke and pollution",
                "Use humidifier in dry environments",
                "Stay warm in cold weather",
                "Practice proper coughing technique",
                "Follow up with healthcare provider"
            ]
        })
        return result
        
    # Ensure all required fields are present
    for field in required_fields:
        if field not in result:
            logger.info(f"Adding default {field} for {result['disease']}")
            if field == "medicines":
                result[field] = [
                    {"name": "Consult doctor", "dosage": "As prescribed", "purpose": "Proper diagnosis and treatment"}
                ]
            elif field == "precautions":
                result[field] = [
                    "Consult healthcare provider for proper guidance",
                    "Rest adequately",
                    "Stay hydrated",
                    "Monitor symptoms",
                    "Follow doctor's recommendations"
                ]
            elif field == "diet":
                result[field] = [
                    "Balanced nutrition",
                    "Stay hydrated",
                    "Fresh fruits and vegetables",
                    "Easily digestible foods",
                    "Follow dietary guidance from healthcare provider"
                ]
            elif field == "exercise":
                result[field] = [
                    "Rest as needed",
                    "Gentle activities as tolerated",
                    "Follow exercise guidance from healthcare provider",
                    "Gradual return to normal activities",
                    "Avoid overexertion"
                ]
            elif field == "lifestyle":
                result[field] = [
                    "Get adequate rest",
                    "Manage stress",
                    "Maintain good hygiene",
                    "Follow up with healthcare provider",
                    "Avoid exposure to triggers"
                ]
    
    # Ensure medicine fields have consistent structure
    if "medicines" in result:
        for medicine in result["medicines"]:
            if isinstance(medicine, dict):
                if "name" not in medicine and "medicine" in medicine:
                    medicine["name"] = medicine["medicine"]
                    
                if "dosage" not in medicine:
                    medicine["dosage"] = "As prescribed"
                    
                if "purpose" not in medicine:
                    medicine["purpose"] = "Treatment"
    
    return result

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict diseases based on symptoms and other factors.
    First checks for critical diseases, then falls back to ML model.
    """
    try:
        data = request.get_json()
        if not data or 'symptoms' not in data:
            return jsonify({'error': 'No symptoms provided'}), 400

        symptoms = data['symptoms']
        age_group = data.get('age_group')
        season = data.get('season')
        
        # Log received symptoms
        logger.info(f"Received symptoms before standardization: {symptoms}")
        
        # Standardize symptoms
        standardized = standardize_symptoms(symptoms)
        logger.info(f"Standardized symptoms: {standardized}")

        # Check for Jaundice/Hepatitis specific symptoms
        jaundice_symptoms = ["yellowing_skin", "yellow_skin", "yellowing_eyes", "yellow_eyes", "jaundice", 
                           "dark_urine", "pale_stools", "clay_colored_stools", "yellowish_skin", "yellowing of skin", 
                           "yellow skin", "yellow eyes", "eye yellowing", "skin yellowing", "yellow colored eyes", 
                           "yellow colored skin", "yellow coloration", "yellow sclera"]
        
        logger.info(f"Checking for jaundice/hepatitis symptoms: {jaundice_symptoms}")
        matching_jaundice_symptoms = [s for s in standardized if s in jaundice_symptoms]
        logger.info(f"Matched jaundice symptoms: {matching_jaundice_symptoms}")
        
        jaundice_symptom_count = sum(1 for s in standardized if s in jaundice_symptoms)
        logger.info(f"Total jaundice symptom matches: {jaundice_symptom_count}")
        
        # If there are strong indicators of jaundice/hepatitis, prioritize these diagnoses
        if jaundice_symptom_count >= 1:
            logger.info(f"Jaundice symptoms detected: {jaundice_symptom_count} symptoms")
            
            # First check for critical diseases
            critical_results = check_critical_diseases(standardized, season)
            
            # Filter to keep only liver-related diseases if we have jaundice symptoms
            liver_diseases = []
            for result in critical_results:
                if result['disease'] in ['Jaundice', 'Hepatitis']:
                    # Boost confidence for liver diseases
                    result['confidence'] = min(1.0, result['confidence'] * 1.5)
                    
                    # Extra boost for Hepatitis when right upper abdominal pain is present
                    if result['disease'] == 'Hepatitis' and 'right_upper_abdominal_pain' in standardized:
                        result['confidence'] = 1.0  # Maximum confidence
                        # Place this at the beginning of the list to be first
                        liver_diseases.insert(0, result)
                    else:
                        liver_diseases.append(result)
            
            # Sort by confidence score to bring highest confidence first
            if liver_diseases:
                liver_diseases.sort(key=lambda x: x['confidence'], reverse=True)
                logger.info(f"Found liver diseases with jaundice symptoms: {[r['disease'] for r in liver_diseases]}")
            else:
                # If no liver diseases were found but we have jaundice symptoms, create a fallback entry
                logger.info("No liver diseases detected from critical check, creating fallback")
                # Check for specific jaundice symptoms only
                jaundice_specific = ["yellowish_skin", "yellow_skin", "yellowing_eyes", "yellow_eyes", 
                                    "yellowing_skin", "jaundice", "yellow coloration", "yellowing of skin",
                                    "dark_urine", "pale_stools", "clay_colored_stools"]
                
                jaundice_count = sum(1 for s in standardized if s in jaundice_specific)
                logger.info(f"Found {jaundice_count} specific jaundice symptoms")
                
                # If we have right upper abdominal pain or Hepatitis-specific symptoms
                if "right_upper_abdominal_pain" in standardized or any(s in standardized for s in ["nausea", "loss_of_appetite", "vomiting"]):
                    # Prioritize Hepatitis 
                    liver_diseases.append({
                        "disease": "Hepatitis",
                        "confidence": 0.85,
                        "danger_level": "HIGH",
                        "requires_immediate_attention": True
                    })
                    logger.info("Created fallback Hepatitis diagnosis")
                # If we have clear jaundice symptoms, prioritize Jaundice
                elif jaundice_count > 0:
                    # Default to Jaundice with high confidence
                    liver_diseases.append({
                        "disease": "Jaundice",
                        "confidence": 0.85,
                        "danger_level": "HIGH",
                        "requires_immediate_attention": True
                    })
                    logger.info("Created fallback Jaundice diagnosis")
                # Fallback with moderate confidence if no clear indicators
                else:
                    # If we have any yellowing symptoms at all, default to Jaundice
                    for symptom in standardized:
                        if "yellow" in symptom or "jaundice" in symptom:
                            liver_diseases.append({
                                "disease": "Jaundice",
                                "confidence": 0.75,
                                "danger_level": "HIGH",
                                "requires_immediate_attention": True
                            })
                            logger.info("Created generic yellowing fallback Jaundice diagnosis")
                            break
            
            # If we found liver diseases with strong confidence
            if liver_diseases:
                logger.info(f"Found liver diseases with jaundice symptoms: {[r['disease'] for r in liver_diseases]}")
                
                # Add recommendations
                for result in liver_diseases:
                    if result['disease'] == 'Jaundice':
                        logger.info(f"Adding special recommendations for Jaundice")
                        result.update({
                            'severity': 'high',
                            'medicines': [
                                {'name': 'Consult doctor immediately', 'dosage': 'As prescribed', 'purpose': 'Diagnosis and treatment'},
                                {'name': 'Ursodeoxycholic acid', 'dosage': 'As prescribed', 'purpose': 'To improve bile flow'},
                                {'name': 'Antihistamines', 'dosage': 'As directed', 'purpose': 'For itching'}
                            ],
                            'precautions': [
                                'Avoid alcohol completely',
                                'Low-fat diet',
                                'Rest adequately',
                                'Stay hydrated',
                                'Seek immediate medical attention'
                            ],
                            'diet': [
                                'Low-fat foods',
                                'Fruits and vegetables',
                                'Whole grains',
                                'Lean proteins',
                                'Plenty of water'
                            ],
                            'exercise': [
                                'Rest initially',
                                'Gentle walking when feeling better',
                                'Light stretching',
                                'No strenuous activity',
                                'Consult doctor before resuming exercise'
                            ],
                            'lifestyle': [
                                'Complete abstinence from alcohol',
                                'Avoid medications that strain the liver',
                                'Regular follow-up with healthcare provider',
                                'Monitor symptoms',
                                'Get adequate rest'
                            ]
                        })
                    elif result['disease'] == 'Hepatitis':
                        logger.info(f"Adding special recommendations for Hepatitis")
                        result.update({
                            'severity': 'high',
                            'medicines': [
                                {'name': 'Consult doctor immediately', 'dosage': 'As prescribed', 'purpose': 'Diagnosis and treatment'},
                                {'name': 'Antiviral medications', 'dosage': 'As prescribed', 'purpose': 'For viral hepatitis'},
                                {'name': 'Supportive care', 'dosage': 'As needed', 'purpose': 'Manage symptoms'}
                            ],
                            'precautions': [
                                'Avoid alcohol completely',
                                'Avoid sharing personal items',
                                'Practice good hygiene',
                                'Rest adequately',
                                'Seek immediate medical attention'
                            ],
                            'diet': [
                                'Low-fat foods',
                                'Protein-rich foods',
                                'Fresh fruits and vegetables',
                                'Avoid processed foods',
                                'Plenty of fluids'
                            ],
                            'exercise': [
                                'Rest initially',
                                'Gentle walking when approved',
                                'Light activities only',
                                'No strenuous exercise',
                                'Follow doctor\'s advice'
                            ],
                            'lifestyle': [
                                'Complete abstinence from alcohol',
                                'Avoid medications that strain the liver',
                                'Practice good hygiene',
                                'Get vaccinated for other hepatitis types',
                                'Regular follow-up with healthcare provider'
                            ]
                        })
                
                # Get suggested symptoms
                suggested = get_missing_symptoms(liver_diseases[0]['disease'], standardized)
                
                return jsonify({
                    'predictions': liver_diseases,
                    'critical_warning': True,
                    'suggested_symptoms': suggested,
                    'special_note': 'Liver condition detected. Please consult a doctor immediately.'
                })
        
        # If no definite jaundice case, proceed with normal flow
        # First check for critical diseases
        critical_results = check_critical_diseases(standardized, season)
        
        # Log critical disease check results
        logger.info(f"Critical disease check results: {critical_results}")
        
        # Special case handling for chicken pox and similar diseases
        for result in critical_results:
            if result['disease'] == 'Chicken Pox':
                logger.info("Found Chicken Pox, adding hard-coded recommendations")
                
                # Add severity field
                result['severity'] = 'medium'
                
                # Add recommendations from our dictionary
                from disease_recommendations import DISEASE_RECOMMENDATIONS
                if 'Chicken Pox' in DISEASE_RECOMMENDATIONS:
                    logger.info("Adding Chicken Pox recommendations from dictionary")
                    chicken_pox_recs = DISEASE_RECOMMENDATIONS['Chicken Pox']
                    result.update(chicken_pox_recs)
                    logger.info(f"Updated result keys: {result.keys()}")
                
                # Validate and ensure all recommendation fields are present
                result = validate_recommendation_fields(result)
                
                # Get suggested symptoms 
                suggested = get_missing_symptoms('Chicken Pox', standardized)
                
                return jsonify({
                    'predictions': [result],
                    'critical_warning': True,
                    'suggested_symptoms': suggested
                })
            
            # Handle other common diseases
            elif result['disease'] in ['Malaria', 'Typhoid', 'Dengue', 'Jaundice', 'COVID', 'Hypertension', 'Heart Attack']:
                logger.info(f"Found {result['disease']}, adding recommendations")
                
                # Add severity field based on danger level
                if result['danger_level'] == 'HIGH':
                    result['severity'] = 'high'
                elif result['danger_level'] == 'MEDIUM':
                    result['severity'] = 'medium'
                else:
                    result['severity'] = 'low'
                
                # Add recommendations from our dictionary
                from disease_recommendations import DISEASE_RECOMMENDATIONS
                if result['disease'] in DISEASE_RECOMMENDATIONS:
                    logger.info(f"Adding {result['disease']} recommendations from dictionary")
                    disease_recs = DISEASE_RECOMMENDATIONS[result['disease']]
                    result.update(disease_recs)
                    logger.info(f"Updated result keys: {result.keys()}")
                
                # Validate and ensure all recommendation fields are present
                result = validate_recommendation_fields(result)
                
                # Get suggested symptoms 
                suggested = get_missing_symptoms(result['disease'], standardized)
                
                return jsonify({
                    'predictions': [result],
                    'critical_warning': True,
                    'suggested_symptoms': suggested
                })
        
        # If we found critical diseases with high confidence, return those
        high_confidence_critical = [r for r in critical_results if r['confidence'] > 5.0]
        if high_confidence_critical:
            logger.info(f"Found critical diseases: {[r['disease'] for r in high_confidence_critical]}")
            
            # Add recommendations for each disease
            for result in high_confidence_critical:
                # Make sure we have a severity field (required by frontend)
                if 'danger_level' in result and not 'severity' in result:
                    if result['danger_level'] == 'HIGH':
                        result['severity'] = 'high'
                    elif result['danger_level'] == 'MEDIUM':
                        result['severity'] = 'medium'
                    else:
                        result['severity'] = 'low'
                        
                # Get recommendations from disease_recommendations
                # First ensure disease name matches case in recommendations dictionary
                disease_name = result['disease']
                logger.info(f"Looking for recommendations for {disease_name}")
                
                # Try direct match with disease_recommendations
                from disease_recommendations import DISEASE_RECOMMENDATIONS
                if disease_name in DISEASE_RECOMMENDATIONS:
                    logger.info(f"Found recommendations for {disease_name} in DISEASE_RECOMMENDATIONS")
                    disease_recs = DISEASE_RECOMMENDATIONS[disease_name]
                    result.update(disease_recs)
                    logger.info(f"Updated result keys: {result.keys()}")
                else:
                    # Try get_recommendations function
                    recommendations = get_recommendations(disease_name, age_group)
                    if recommendations:
                        logger.info(f"Found recommendations for {disease_name} via get_recommendations")
                        result.update(recommendations)
                        result["severity"] = result.get("danger_level", "MEDIUM").lower()
                        logger.info(f"Updated result keys: {result.keys()}")
                    else:
                        logger.info(f"No recommendations found for {disease_name}")
                    
                # If no recommendations found, try disease_info as backup
                if result['disease'] in disease_info:
                    logger.info(f"Found disease info for {result['disease']}")
                    disease_data = disease_info[result['disease']]
                    for key in ['description', 'precautions', 'medicine_recommendations', 'food_preferences', 'exercises']:
                        if key in disease_data:
                            if key == 'medicine_recommendations':
                                result['medicines'] = disease_data[key]
                            elif key == 'food_preferences':
                                result['diet'] = disease_data[key]
                            elif key == 'exercises':
                                result['exercise'] = disease_data[key]
                            else:
                                result[key] = disease_data[key]
                    logger.info(f"Updated result keys from disease_info: {result.keys()}")
                else:
                    logger.info(f"No disease info found for {result['disease']}")
                
                # Validate and ensure all recommendation fields are present
                result = validate_recommendation_fields(result)
            
            # Get suggested symptoms for the top disease
            suggested = get_missing_symptoms(high_confidence_critical[0]['disease'], standardized)
            
            return jsonify({
                'predictions': high_confidence_critical,
                'critical_warning': True,
                'suggested_symptoms': suggested
            })
        
        # Otherwise, use ML model as backup
        symptom_vector = symptoms_to_vector(standardized)
        
        # Get model predictions
        predictions = model.predict_proba([symptom_vector])[0]
        diseases = label_encoder.classes_
        
        # Define conflicting symptoms for diseases
        conflicting_symptoms = {
            "Depression": ["itchy_rash", "blisters", "red_spots", "fluid_filled_blisters", 
                          "skin_rash", "rash", "itching"],
            "Food Poisoning": ["yellowing_skin", "yellow_eyes", "yellowish_skin", "yellowing_eyes",
                              "dark_urine", "jaundice", "pale_stools", "clay_colored_stools"]
        }
        
        # Convert to list of predictions
        ml_results = []
        for disease, prob in zip(diseases, predictions):
            if prob > 0.001:  # Only include significant probabilities
                # Check for conflicting symptoms
                if disease in conflicting_symptoms:
                    conflict_found = False
                    for conflict in conflicting_symptoms[disease]:
                        if conflict in standardized:
                            conflict_found = True
                            logger.info(f"Found conflicting symptom {conflict} for disease {disease}")
                            break
                    
                    # Skip this disease if conflicts found
                    if conflict_found:
                        logger.info(f"Skipping {disease} due to conflicting symptoms")
                        continue
                
                # Special case for Food Poisoning - double check
                if disease == "Food Poisoning":
                    # If there are jaundice symptoms present, don't predict Food Poisoning
                    jaundice_symptom_count = sum(1 for s in standardized if s in jaundice_symptoms)
                    if jaundice_symptom_count > 0:
                        logger.info(f"Skipping Food Poisoning due to presence of {jaundice_symptom_count} jaundice symptoms")
                        continue
                
                # Calculate symptom match score
                disease_symptoms = disease_symptoms_map.get(disease, set())
                if disease_symptoms:
                    # Calculate match percentage
                    matched_symptoms = set(standardized) & disease_symptoms
                    match_percent = len(matched_symptoms) / len(disease_symptoms)
                    
                    # Calculate how many of user's symptoms match the disease
                    user_symptom_match = len(matched_symptoms) / len(standardized)
                    
                    # Combine both match percentages with ML probability
                    combined_score = (match_percent * 0.4) + (user_symptom_match * 0.3) + (prob * 0.3)
                    
                    # Boost confidence for very good matches
                    if match_percent > 0.6 and user_symptom_match > 0.6:
                        combined_score = max(combined_score, 0.8)
                    elif match_percent > 0.4 and user_symptom_match > 0.4:
                        combined_score = max(combined_score, 0.6)
                        
                    adjusted_prob = combined_score
                else:
                    adjusted_prob = prob

                result = {
                    'disease': disease,
                    'confidence': float(adjusted_prob),
                    'danger_level': 'MEDIUM',
                    'requires_immediate_attention': False,
                    'severity': 'medium'  # Add severity explicitly
                }
                
                # Add recommendations
                # First try direct match with disease_recommendations
                from disease_recommendations import DISEASE_RECOMMENDATIONS
                if disease in DISEASE_RECOMMENDATIONS:
                    logger.info(f"Found recommendations for {disease} in DISEASE_RECOMMENDATIONS")
                    disease_recs = DISEASE_RECOMMENDATIONS[disease]
                    result.update(disease_recs)
                    logger.info(f"Updated result keys: {result.keys()}")
                else:
                    # Try get_recommendations function
                    recommendations = get_recommendations(disease, age_group)
                    if recommendations:
                        logger.info(f"Found recommendations for {disease} via get_recommendations")
                        result.update(recommendations)
                        logger.info(f"Updated result keys: {result.keys()}")
                    # If no recommendations found, try disease_info as backup
                    elif disease in disease_info:
                        logger.info(f"Found disease info for {disease}")
                        disease_data = disease_info[disease]
                        for key in ['description', 'precautions', 'medicine_recommendations', 'food_preferences', 'exercises']:
                            if key in disease_data:
                                if key == 'medicine_recommendations':
                                    result['medicines'] = disease_data[key]
                                elif key == 'food_preferences':
                                    result['diet'] = disease_data[key]
                                elif key == 'exercises':
                                    result['exercise'] = disease_data[key]
                                else:
                                    result[key] = disease_data[key]
                        logger.info(f"Updated result keys from disease_info: {result.keys()}")
                
                # Validate and ensure all recommendation fields are present
                result = validate_recommendation_fields(result)
                                
                ml_results.append(result)
        
        # Combine results, prioritizing critical diseases
        combined_results = critical_results + [r for r in ml_results if r['disease'] not in [cr['disease'] for cr in critical_results]]
        combined_results.sort(key=lambda x: x['confidence'], reverse=True)
        
        # Take top 5 results
        final_results = combined_results[:5]
        
        # Filter out predictions with very low confidence
        final_results = [result for result in final_results if result['confidence'] > 0.05]
        
        if not final_results:
            # If no results meet even the lowered threshold, return a default result
            default_disease = "Common Cold"  # Default to a common disease
            default_result = {
                'disease': default_disease,
                'confidence': 0.4,  # Moderate confidence
                'danger_level': 'LOW',
                'requires_immediate_attention': False,
                'severity': 'low'
            }
            
            # Add recommendations
            from disease_recommendations import DISEASE_RECOMMENDATIONS
            if default_disease in DISEASE_RECOMMENDATIONS:
                logger.info(f"Using default recommendations for {default_disease}")
                default_result.update(DISEASE_RECOMMENDATIONS[default_disease])
            
            # Validate and ensure all recommendation fields are present
            default_result = validate_recommendation_fields(default_result)
            
            final_results = [default_result]
        
        # Ensure all results have complete recommendation fields
        for result in final_results:
            result = validate_recommendation_fields(result)
        
        if not final_results:
            return jsonify({
                'error': 'No predictions available for the given symptoms. Please check the symptoms and try again.',
                'provided_symptoms': symptoms,
                'standardized_symptoms': standardized
            }), 404
        
        # Get suggested symptoms for the top disease
        suggested = get_missing_symptoms(final_results[0]['disease'], standardized)
        
        logger.info(f"Successful prediction for symptoms: {symptoms}")
        return jsonify({
            'predictions': final_results,
            'critical_warning': bool(critical_results),
            'suggested_symptoms': suggested
        })

    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

def save_prediction_history(symptoms, predicted_disease, confidence, age=None, gender=None):
    """Save prediction to history database"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("prediction_history.csv", "a") as f:
            f.write(f"{timestamp},{','.join(symptoms)},{predicted_disease},{confidence},{age},{gender}\n")
    except Exception as e:
        logger.error(f"Error saving prediction history: {e}")

if __name__ == "__main__":
    # Use port 5001 by default, or from environment variable
    port = int(os.getenv('PORT', 5001))
    try:
        logger.info("Starting MEDIS backend server...")
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise
