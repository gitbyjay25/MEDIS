import pandas as pd
import random

def clean_symptom(symptom):
    """Clean symptom text by removing extra spaces and standardizing format"""
    if pd.isna(symptom) or symptom == '':
        return ''
    # Remove extra spaces and convert to lowercase
    symptom = str(symptom).strip().lower()
    # Replace spaces with underscores
    symptom = symptom.replace(' ', '_')
    # Remove any double underscores
    symptom = symptom.replace('__', '_')
    return symptom

# Define new diseases with their symptoms
new_diseases = [
    # Heart Attack - Updated with more comprehensive symptoms
    {
        'Disease': 'Heart attack',
        'symptoms': [
            'chest_pain', 'arm_pain', 'shoulder_pain', 'jaw_pain', 'back_pain',
            'stomach_pain', 'shortness_of_breath', 'nausea', 'vomiting',
            'dizziness', 'cold_sweat', 'fatigue', 'indigestion', 'anxiety',
            'pale_skin', 'breathlessness', 'pain_in_arm', 'sweating'
        ]
    },
    # Pneumonia - Updated with more comprehensive symptoms
    {
        'Disease': 'Pneumonia',
        'symptoms': [
            'cough', 'fever', 'shortness_of_breath', 'chest_pain', 'fatigue',
            'loss_of_appetite', 'sweating', 'rapid_breathing', 'shallow_breathing',
            'bluish_lips', 'wheezing', 'difficulty_feeding', 'irritability',
            'confusion', 'low_body_temperature', 'chills', 'muscle_pain'
        ]
    },
    # Food Poisoning - Updated with more comprehensive symptoms
    {
        'Disease': 'Food Poisoning',
        'symptoms': [
            'nausea', 'vomiting', 'diarrhea', 'stomach_cramps', 'abdominal_pain',
            'fever', 'weakness', 'fatigue', 'headache', 'loss_of_appetite',
            'chills', 'dehydration', 'dry_mouth', 'dark_urine', 'dizziness'
        ]
    },
    # Kidney Stone - Updated with more comprehensive symptoms
    {
        'Disease': 'Kidney Stone',
        'symptoms': [
            'severe_back_pain', 'side_pain', 'lower_abdominal_pain', 'painful_urination',
            'blood_in_urine', 'frequent_urination', 'small_urine_amounts',
            'nausea', 'vomiting', 'cloudy_urine', 'foul_smelling_urine',
            'burning_urination', 'fever', 'chills'
        ]
    },
    # Appendicitis - Updated with more comprehensive symptoms
    {
        'Disease': 'Appendicitis',
        'symptoms': [
            'lower_right_abdominal_pain', 'navel_pain', 'pain_with_movement',
            'loss_of_appetite', 'nausea', 'vomiting', 'low_grade_fever',
            'abdominal_swelling', 'constipation', 'diarrhea', 'inability_to_pass_gas',
            'abdominal_bloating'
        ]
    },
    # Migraine - Added with detailed symptoms
    {
        'Disease': 'Migraine',
        'symptoms': [
            'throbbing_headache', 'sensitivity_to_light', 'sensitivity_to_sound',
            'nausea', 'vomiting', 'visual_disturbances', 'aura', 'neck_pain',
            'dizziness', 'fatigue', 'weakness', 'numbness_tingling'
        ]
    },
    # Bronchitis - Added with detailed symptoms
    {
        'Disease': 'Bronchitis',
        'symptoms': [
            'persistent_cough', 'mucus_production', 'wheezing', 'chest_tightness',
            'shortness_of_breath', 'fatigue', 'mild_fever', 'chest_discomfort',
            'sore_throat', 'body_aches', 'nasal_congestion'
        ]
    },
    # UTI (Urinary Tract Infection) - Added with detailed symptoms
    {
        'Disease': 'UTI',
        'symptoms': [
            'frequent_urination', 'burning_sensation', 'cloudy_urine', 'strong_urine_odor',
            'pelvic_pain', 'lower_back_pain', 'blood_in_urine', 'fatigue',
            'fever', 'pressure_in_lower_abdomen'
        ]
    },
    # Gastritis - Added with detailed symptoms
    {
        'Disease': 'Gastritis',
        'symptoms': [
            'upper_abdominal_pain', 'nausea', 'vomiting', 'bloating',
            'indigestion', 'loss_of_appetite', 'dark_stools', 'hiccups',
            'burning_sensation', 'fullness_after_eating'
        ]
    },
    # Asthma - Added with detailed symptoms
    {
        'Disease': 'Asthma',
        'symptoms': [
            'wheezing', 'shortness_of_breath', 'chest_tightness', 'coughing',
            'difficulty_breathing', 'rapid_breathing', 'anxiety', 'difficulty_speaking',
            'pale_face', 'blue_lips_or_fingernails', 'fatigue'
        ]
    },
    # Sinusitis - Updated with more symptoms
    {
        'Disease': 'Sinusitis',
        'symptoms': [
            'nasal_congestion', 'facial_pain', 'headache', 'loss_of_smell',
            'cough', 'fatigue', 'fever', 'runny_nose', 'sore_throat',
            'bad_breath', 'dental_pain', 'ear_pressure'
        ]
    },
    # Ear Infection - Updated with more symptoms
    {
        'Disease': 'Ear Infection',
        'symptoms': [
            'ear_pain', 'hearing_loss', 'fever', 'ear_discharge',
            'irritability', 'difficulty_sleeping', 'loss_of_balance',
            'headache', 'tugging_at_ear', 'poor_appetite', 'crying_at_night'
        ]
    },
    # Conjunctivitis - Updated with more symptoms
    {
        'Disease': 'Conjunctivitis',
        'symptoms': [
            'red_eyes', 'watery_eyes', 'eye_pain', 'light_sensitivity',
            'itchy_eyes', 'eye_discharge', 'blurred_vision', 'gritty_feeling',
            'swollen_eyelids', 'burning_sensation', 'morning_crusting'
        ]
    }
]

# Define precautions for diseases with more detailed instructions
new_precautions = {
    'Heart attack': [
        'call_emergency_immediately',
        'chew_aspirin_if_prescribed',
        'stay_calm_and_rest',
        'loosen_tight_clothing'
    ],
    'Pneumonia': [
        'complete_prescribed_antibiotics',
        'get_plenty_of_rest',
        'stay_hydrated',
        'use_humidifier'
    ],
    'Food Poisoning': [
        'stay_hydrated_with_electrolytes',
        'rest_and_avoid_solid_foods',
        'gradually_reintroduce_bland_foods',
        'seek_medical_help_if_severe'
    ],
    'Kidney Stone': [
        'drink_plenty_of_water',
        'take_prescribed_pain_medication',
        'strain_urine_to_catch_stones',
        'follow_dietary_restrictions'
    ],
    'Appendicitis': [
        'seek_immediate_medical_care',
        'do_not_take_pain_medication',
        'do_not_eat_or_drink',
        'avoid_heating_pads'
    ],
    'Migraine': [
        'rest_in_dark_quiet_room',
        'stay_hydrated',
        'apply_cold_or_hot_compress',
        'take_prescribed_medication'
    ],
    'Bronchitis': [
        'get_plenty_of_rest',
        'stay_hydrated',
        'use_humidifier',
        'avoid_smoking_and_irritants'
    ],
    'UTI': [
        'drink_plenty_of_water',
        'complete_antibiotics_course',
        'urinate_frequently',
        'take_pain_relievers'
    ],
    'Gastritis': [
        'eat_smaller_frequent_meals',
        'avoid_trigger_foods',
        'take_prescribed_medication',
        'quit_smoking_and_alcohol'
    ],
    'Asthma': [
        'follow_asthma_action_plan',
        'avoid_triggers',
        'take_prescribed_inhalers',
        'monitor_peak_flow'
    ],
    'Sinusitis': [
        'use_nasal_irrigation',
        'take_decongestants',
        'apply_warm_compress',
        'get_adequate_rest'
    ],
    'Ear Infection': [
        'take_prescribed_antibiotics',
        'apply_warm_compress',
        'rest_with_head_elevated',
        'avoid_water_in_ear'
    ],
    'Conjunctivitis': [
        'wash_hands_frequently',
        'avoid_touching_eyes',
        'use_prescribed_eyedrops',
        'use_clean_towels_daily'
    ]
}

# Load existing datasets
df_symptoms = pd.read_csv("data/DiseaseAndSymptoms.csv")
df_precautions = pd.read_csv("data/Disease precaution.csv")

# Clean existing symptom columns
symptom_cols = [col for col in df_symptoms.columns if 'Symptom_' in col]
for col in symptom_cols:
    df_symptoms[col] = df_symptoms[col].apply(clean_symptom)

# Create new entries for diseases with variations
new_entries = []
for disease in new_diseases:
    # Create multiple variations of symptoms for better training
    base_symptoms = disease['symptoms']
    
    # Full set of symptoms
    entry = {'Disease': disease['Disease']}
    for i, symptom in enumerate(base_symptoms, 1):
        entry[f'Symptom_{i}'] = symptom
    new_entries.append(entry)
    
    # Create variations with different combinations
    for i in range(7):  # Create more variations for better coverage
        entry = {'Disease': disease['Disease']}
        symptoms = base_symptoms.copy()
        if len(symptoms) > 8:
            # Randomly select 6-10 symptoms for more realistic combinations
            num_symptoms = random.randint(6, min(10, len(symptoms)))
            symptoms = random.sample(symptoms, num_symptoms)
        
        # Ensure key symptoms are always included
        key_symptoms = base_symptoms[:3]  # First 3 symptoms are considered key
        symptoms = list(set(key_symptoms + symptoms))
        
        for j, symptom in enumerate(symptoms, 1):
            entry[f'Symptom_{j}'] = symptom
        new_entries.append(entry)

# Create DataFrame from new entries
df_new = pd.DataFrame(new_entries)

# Remove any existing entries of these diseases to avoid duplicates
df_symptoms = df_symptoms[~df_symptoms['Disease'].isin([d['Disease'] for d in new_diseases])]

# Concatenate with existing data
df_symptoms = pd.concat([df_symptoms, df_new], ignore_index=True)

# Update precautions
new_precautions_df = pd.DataFrame({
    'Disease': list(new_precautions.keys()),
    'Precaution_1': [precautions[0] for precautions in new_precautions.values()],
    'Precaution_2': [precautions[1] for precautions in new_precautions.values()],
    'Precaution_3': [precautions[2] for precautions in new_precautions.values()],
    'Precaution_4': [precautions[3] for precautions in new_precautions.values()]
})

# Remove any existing entries of these diseases from precautions
df_precautions = df_precautions[~df_precautions['Disease'].isin(new_precautions.keys())]

# Add new precautions
df_precautions = pd.concat([df_precautions, new_precautions_df], ignore_index=True)

# Save updated datasets
df_symptoms.to_csv("data/DiseaseAndSymptoms.csv", index=False)
df_precautions.to_csv("data/Disease precaution.csv", index=False)

print("✅ Successfully updated diseases and symptoms!")
print("✅ Successfully updated precautions!")
print("\nDiseases updated with comprehensive symptoms:")
for disease in new_diseases:
    print(f"\n- {disease['Disease']}:")
    print("  Symptoms:", ", ".join(disease['symptoms']))