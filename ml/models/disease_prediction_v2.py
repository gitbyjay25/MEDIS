SYMPTOM_CATEGORIES = {
    "fever_types": {
        "high_fever": 3.0,
        "periodic_fever": 3.0,
        "mild_fever": 1.0,
        "intermittent_fever": 2.0,
        "fever": 2.0  # Added base fever
    },
    "pain_types": {
        "headache": 2.0,
        "severe_headache": 3.0,
        "body_ache": 2.0,
        "joint_pain": 2.0,
        "muscle_pain": 2.0,
        "chest_pain": 3.0,
        "pain_behind_eyes": 3.0, # Added
        "muscle_and_joint_pain": 3.0 # Added combined symptom
    },
    "skin_related": {
        "skin_rash": 3.0,
        "red_spots": 3.0,
        "itching": 2.0,
        "skin_peeling": 2.0,
        "rash": 3.0 # Added base rash
    },
    "respiratory": {
        "cough": 2.0,
        "dry_cough": 3.0,
        "breathing_difficulty": 3.0,
        "congestion": 1.0,
        "shortness_of_breath": 3.0, # Added
        "wheezing": 3.0, # Added
        "chest_tightness": 3.0, # Added
        "chest_discomfort": 2.5, # Added with slightly lower weight than chest_tightness
        "production_of_mucus": 2.0 # Added
    }
}

SYMPTOM_SEVERITY = {
    "MILD": 1.0,
    "MODERATE": 2.0,
    "SEVERE": 3.0
}

AGE_GROUPS = {
    "INFANT": "0-2",
    "CHILD": "3-12",
    "TEEN": "13-19",
    "ADULT": "20-60",
    "ELDERLY": "60+"
}

SEASONS = {
    "SUMMER": ["heat_related", "dehydration_risk"],
    "WINTER": ["cold_related", "respiratory_risk"],
    "MONSOON": ["water_borne", "infection_risk"],
    "SPRING": ["allergy_risk", "pollen_related"]
}

DISEASE_PROFILES = {
    "Malaria": {
        "critical_symptoms": {
            "periodic_fever": 3.0,
            "chills": 3.0,
            "sweating": 3.0,
            "high_fever": 2.5 # Added for overlap
        },
        "high_priority": {
            "severe_headache": 2.0,
            "nausea": 2.0,
            "body_ache": 2.0,
            "fatigue": 2.0,
            "vomiting": 2.0,
            "headache": 1.5 # Added for overlap
        },
        "medium_priority": {
            "diarrhea": 1.0,
            "muscle_pain": 1.0,
            "weakness": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A parasitic disease spread by mosquitoes",
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "seasonal_factor": ["MONSOON", "SUMMER"],
        "age_specific_symptoms": {
            "INFANT": ["irritability", "poor_feeding"],
            "CHILD": ["severe_anemia", "rapid_breathing"],
            "ADULT": ["jaundice", "mental_confusion"],
            "ELDERLY": ["organ_failure", "severe_complications"]
        },
        "complications": [
            "Cerebral malaria",
            "Organ failure",
            "Severe anemia",
            "Respiratory distress"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Artemisinin-based combination therapy (ACT)", "duration": "3 days"},
                {"name": "Chloroquine (in sensitive areas)", "duration": "3 days"}
            ],
            "lifestyle": [
                "Complete bed rest",
                "Increased fluid intake",
                "Balanced nutrition",
                "Regular temperature monitoring"
            ],
            "prevention": [
                "Use mosquito nets",
                "Apply insect repellent",
                "Wear protective clothing",
                "Eliminate standing water"
            ]
        },
        "symptom_duration": {
            "onset_period": "10-15 days",
            "critical_period": "3-7 days",
            "recovery_period": "2-4 weeks"
        }
    },
    
    "Sinusitis": {
        "critical_symptoms": {
            "facial_pain": 3.0,
            "nasal_congestion": 3.0,
            "loss_of_smell": 3.0
        },
        "high_priority": {
            "ear_pressure": 2.0,
            "dental_pain": 2.0,
            "bad_breath": 2.0,
            "thick_nasal_discharge": 2.0,
            "congestion": 1.5 # Adjusted weight
        },
        "medium_priority": {
            "headache": 1.0,
            "cough": 1.0,
            "fatigue": 1.0,
            "fever": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "Inflammation of the sinuses",
        "danger_level": "LOW",
        "requires_immediate_attention": False,
        "seasonal_factor": ["WINTER", "MONSOON"]
    },
    
    "COVID_19": {
        "critical_symptoms": {
            "high_fever": 3.0,
            "dry_cough": 3.0,
            "breathing_difficulty": 3.0,
            "loss_of_taste": 3.0
        },
        "high_priority": {
            "fatigue": 2.0,
            "body_ache": 2.0,
            "sore_throat": 2.0,
            "loss_of_smell": 2.0,
            "cough": 1.8 # Adjusted weight
        },
        "medium_priority": {
            "headache": 1.0,
            "diarrhea": 1.0,
            "congestion": 1.0,
            "nausea": 1.0,
            "fever": 1.0 # Added base fever
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "Viral infection caused by SARS-CoV-2",
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    
    "Dengue": {
        "critical_symptoms": {
            "high_fever": 3.0,
            "severe_headache": 3.0,
            "pain_behind_eyes": 3.0,
            "muscle_and_joint_pain": 3.0,
            "rash": 3.0
        },
        "high_priority": {
            "fatigue": 2.0,
            "nausea": 2.0,
            "vomiting": 2.0,
            "eye_pain": 2.0,
            "headache": 1.8
        },
        "medium_priority": {
            "joint_pain": 1.0,
            "muscle_pain": 1.0,
            "weakness": 1.0,
            "bleeding_gums": 1.0,
            "nose_bleeds": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A viral infection spread by mosquitoes",
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "seasonal_factor": ["SUMMER", "MONSOON"],
        "age_specific_symptoms": {
            "CHILD": ["lethargy", "poor_appetite"],
            "ADULT": ["rose_spots", "enlarged_spleen"],
            "ELDERLY": ["confusion", "severe_complications"]
        },
        "complications": [
            "Dengue hemorrhagic fever",
            "Dengue shock syndrome",
            "Internal bleeding",
            "Dehydration"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Acetaminophen", "duration": "As needed", "purpose": "Fever and pain relief (avoid aspirin and NSAIDs)"}
            ],
            "lifestyle": [
                "Plenty of rest",
                "Increased fluid intake",
                "Avoid mosquito bites (during fever)"
            ],
            "prevention": [
                "Mosquito control",
                "Use mosquito repellent",
                "Wear protective clothing"
            ]
        },
        "symptom_duration": {
            "onset_period": "4-10 days after bite",
            "critical_period": "2-7 days",
            "recovery_period": "1-2 weeks"
        }
    },
    
    "Chicken_Pox": {
        "critical_symptoms": {
            "itchy_rash": 3.0,
            "blisters": 3.0,
            "red_spots": 3.0,
            "itching": 3.0
        },
        "high_priority": {
            "fever": 2.0,
            "loss_of_appetite": 2.0,
            "tiredness": 2.0,
            "headache": 2.0,
            "swelled_lymph_nodes": 2.0
        },
        "medium_priority": {
            "body_ache": 1.0,
            "sore_throat": 1.0,
            "cough": 1.0
        },
        "min_critical_needed": 1,
        "min_high_needed": 1,
        "description": "A highly contagious viral infection causing an itchy rash and blisters",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False,
        "complications": [
            "Bacterial skin infections",
            "Pneumonia",
            "Encephalitis",
            "Reye's syndrome"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Calamine lotion", "duration": "As needed", "purpose": "Itch relief"},
                {"name": "Antihistamines", "duration": "As prescribed", "purpose": "Reduce itching"},
                {"name": "Acetaminophen", "duration": "As needed", "purpose": "Fever and pain relief"}
            ],
            "lifestyle": [
                "Keep fingernails short",
                "Take cool baths",
                "Wear loose, cotton clothing",
                "Stay home until all blisters have crusted",
                "Get plenty of rest"
            ],
            "prevention": [
                "Vaccination",
                "Avoid contact with infected persons",
                "Good hand hygiene",
                "Isolation during active infection"
            ]
        },
        "symptom_duration": {
            "onset_period": "10-21 days after exposure",
            "critical_period": "5-7 days",
            "recovery_period": "2-3 weeks"
        }
    },
    
    "Typhoid": {
        "critical_symptoms": {
            "high_fever": 3.0,
            "weakness": 3.0,
            "abdominal_pain": 3.0,
            "constipation": 3.0,
            "fever": 2.5
        },
        "high_priority": {
            "headache": 2.0,
            "loss_of_appetite": 2.0,
            "diarrhea": 2.0,
            "rose_spots": 2.0,
            "fatigue": 1.8
        },
        "medium_priority": {
            "muscle_pain": 1.0,
            "nausea": 1.0,
            "vomiting": 1.0,
            "dry_cough": 1.0
        },
        "min_critical_needed": 1,
        "min_high_needed": 2,
        "description": "A bacterial infection that can spread throughout the body",
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "seasonal_factor": ["SUMMER", "MONSOON"],
        "age_specific_symptoms": {
            "CHILD": ["lethargy", "poor_appetite"],
            "ADULT": ["rose_spots", "enlarged_spleen"],
            "ELDERLY": ["confusion", "severe_complications"]
        },
        "complications": [
            "Intestinal bleeding",
            "Intestinal perforation",
            "Peritonitis",
            "Pneumonia"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Ciprofloxacin", "duration": "7-14 days"},
                {"name": "Ceftriaxone", "duration": "10-14 days"}
            ],
            "lifestyle": [
                "Complete bed rest",
                "Soft bland diet",
                "Increased fluid intake",
                "Regular temperature monitoring"
            ],
            "prevention": [
                "Safe drinking water",
                "Proper hand hygiene",
                "Avoid raw foods",
                "Proper food handling"
            ]
        },
        "symptom_duration": {
            "onset_period": "6-30 days",
            "critical_period": "7-10 days",
            "recovery_period": "3-6 weeks"
        }
    },
    
    "Common_Cold": {
        "critical_symptoms": {
            "runny_nose": 3.0,
            "sore_throat": 3.0,
            "congestion": 3.0
        },
        "high_priority": {
            "cough": 2.0,
            "mild_fever": 2.0,
            "sneezing": 2.0,
            "fatigue": 1.5 # Added for overlap
        },
        "medium_priority": {
            "headache": 1.0,
            "body_ache": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "A viral infection of the upper respiratory tract",
        "danger_level": "LOW",
        "requires_immediate_attention": False
    },
    
    "Tuberculosis": {
        "critical_symptoms": {
            "persistent_cough": 3.0,
            "coughing_blood": 3.0,
            "chest_pain": 3.0,
            "weight_loss": 3.0
        },
        "high_priority": {
            "night_sweats": 2.0,
            "fatigue": 2.0,
            "fever": 2.0,
            "loss_of_appetite": 2.0
        },
        "medium_priority": {
            "breathing_difficulty": 1.0,
            "weakness": 1.0,
            "shortness_of_breath": 1.0 # Added for overlap
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A serious bacterial infection affecting the lungs",
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    
    "Jaundice": {
        "critical_symptoms": {
            "yellowing_skin": 3.0,
            "yellowing_eyes": 3.0,
            "dark_urine": 3.0,
            "yellowish_skin": 3.0,
            "yellow_eyes": 3.0,
            "pale_stools": 3.0,
            "clay_colored_stools": 3.0
        },
        "high_priority": {
            "abdominal_pain": 2.0,
            "fatigue": 2.0,
            "loss_of_appetite": 2.0,
            "nausea": 2.0,
            "itching": 2.0
        },
        "medium_priority": {
            "fever": 1.0,
            "weakness": 1.0,
            "vomiting": 1.0,
            "weight_loss": 1.0
        },
        "min_critical_needed": 1,
        "min_high_needed": 1,
        "description": "A condition causing yellowing of the skin and whites of the eyes",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": True,
        "exclude_symptoms": [
            "diarrhea", "loose_stools", "food_poisoning_symptoms"
        ]
    },
    
    "Gastritis": {
        "critical_symptoms": {
            "severe_abdominal_pain": 3.0,
            "burning_stomach_pain": 3.0,
            "persistent_nausea": 3.0
        },
        "high_priority": {
            "vomiting": 2.0,
            "bloating": 2.0,
            "indigestion": 2.0,
            "loss_of_appetite": 2.0,
            "abdominal_pain": 1.5 # Added for overlap
        },
        "medium_priority": {
            "fatigue": 1.0,
            "weakness": 1.0,
            "headache": 1.0
        },
        "min_critical_needed": 1,
        "min_high_needed": 2,
        "description": "Inflammation of the stomach lining",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
    },
    
    "Skin_Infection": {
        "critical_symptoms": {
            "skin_rash": 3.0,
            "pus_filled_pimples": 3.0,
            "scurring": 3.0,
            "rash": 2.5 # Added for overlap
        },
        "high_priority": {
            "itching": 2.0,
            "skin_peeling": 2.0,
            "red_spots": 2.0
        },
        "medium_priority": {
            "mild_fever": 1.0,
            "fatigue": 1.0,
            "body_ache": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "A skin infection characterized by rash and pus-filled lesions",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": True,
        "complications": [
            "Secondary bacterial infection",
            "Scarring",
            "Cellulitis",
            "Skin discoloration"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Topical antibiotics", "duration": "7-10 days"},
                {"name": "Oral antibiotics (if severe)", "duration": "7-14 days"}
            ],
            "lifestyle": [
                "Keep affected area clean and dry",
                "Avoid scratching",
                "Use mild soap",
                "Wear loose, breathable clothing"
            ],
            "prevention": [
                "Maintain good hygiene",
                "Avoid sharing personal items",
                "Keep skin moisturized",
                "Avoid direct contact with infected areas"
            ]
        },
        "symptom_duration": {
            "onset_period": "1-3 days",
            "critical_period": "3-7 days",
            "recovery_period": "1-2 weeks"
        }
    },
    
    "Acne": {
        "critical_symptoms": {
            "pus_filled_pimples": 3.0,
            "skin_rash": 3.0,
            "scurring": 3.0
        },
        "high_priority": {
            "oily_skin": 2.0,
            "blackheads": 2.0,
            "whiteheads": 2.0,
            "red_spots": 2.0
        },
        "medium_priority": {
            "itching": 1.0,
            "skin_peeling": 1.0,
            "facial_inflammation": 1.0,
            "skin_rash": 0.8 # Adjusted weight for overlap
        },
        "min_critical_needed": 1,
        "min_high_needed": 1,
        "description": "A skin condition that occurs when hair follicles become clogged with oil and dead skin cells",
        "danger_level": "LOW",
        "requires_immediate_attention": False,
        "seasonal_factor": ["SUMMER"],
        "age_specific_symptoms": {
            "TEEN": ["severe_breakouts", "hormonal_acne"],
            "ADULT": ["cystic_acne", "persistent_acne"]
        },
        "complications": [
            "Permanent scarring",
            "Skin discoloration",
            "Post-inflammatory hyperpigmentation",
            "Self-esteem issues"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Benzoyl peroxide", "duration": "ongoing"},
                {"name": "Salicylic acid", "duration": "ongoing"},
                {"name": "Topical retinoids", "duration": "as prescribed"},
                {"name": "Antibiotics (if severe)", "duration": "as prescribed by doctor"}
            ],
            "lifestyle": [
                "Wash face twice daily with mild cleanser",
                "Avoid touching face frequently",
                "Use non-comedogenic products",
                "Keep hair clean and away from face",
                "Maintain healthy diet",
                "Stay hydrated"
            ],
            "prevention": [
                "Regular face washing",
                "Oil-free sunscreen use",
                "Avoid heavy makeup",
                "Change pillowcases regularly",
                "Avoid picking or squeezing pimples"
            ]
        },
        "symptom_duration": {
            "onset_period": "gradual",
            "critical_period": "varies",
            "recovery_period": "2-8 weeks with treatment"
        }
    },
    
    "Arthritis": {
        "critical_symptoms": {
            "joint_pain": 3.0,
            "joint_stiffness": 3.0,
            "joint_swelling": 3.0,
            "reduced_joint_mobility": 3.0
        },
        "high_priority": {
            "morning_stiffness": 2.0,
            "joint_warmth": 2.0,
            "fatigue": 2.0,
            "muscle_weakness": 2.0,
            "muscle_and_joint_pain": 1.8,
            "joint_redness": 1.5
        },
        "medium_priority": {
            "fever": 1.0,
            "weight_loss": 1.0,
            "loss_of_appetite": 1.0,
            "body_ache": 0.8
        },
        "min_critical_needed": 1,
        "min_high_needed": 1,
        "description": "A condition causing inflammation in joints, leading to pain and stiffness",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False,
        "age_specific_symptoms": {
            "ADULT": ["chronic_pain", "joint_deformity"],
            "ELDERLY": ["severe_mobility_issues", "bone_spurs"]
        },
        "complications": [
            "Joint deformity",
            "Reduced mobility",
            "Chronic pain",
            "Depression due to chronic pain"
        ]
    },
    
    "AIDS": {
        "critical_symptoms": {
            "severe_weight_loss": 3.0,
            "recurring_fever": 3.0,
            "extreme_fatigue": 3.0,
            "swollen_lymph_nodes": 3.0
        },
        "high_priority": {
            "night_sweats": 2.0,
            "persistent_cough": 2.0,
            "skin_lesions": 2.0,
            "frequent_infections": 2.0
        },
        "medium_priority": {
            "headache": 1.0,
            "muscle_aches": 1.0,
            "sore_throat": 1.0,
            "nausea": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "Advanced stage of HIV infection affecting the immune system",
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "complications": [
            "Opportunistic infections",
            "Certain cancers",
            "Wasting syndrome",
            "Neurological complications"
        ],
        "treatment_recommendations": {
            "medications": [
                {"name": "Antiretroviral therapy", "duration": "lifelong"},
                {"name": "Opportunistic infection prophylaxis", "duration": "as prescribed"},
                {"name": "Other medications based on complications", "duration": "as needed"}
            ],
            "lifestyle": [
                "Regular medical check-ups",
                "Proper nutrition",
                "Adequate rest",
                "Stress management",
                "Safe sex practices"
            ],
            "prevention": [
                "Safe sex practices",
                "Regular HIV testing",
                "Avoid sharing needles",
                "Mother-to-child transmission prevention"
            ]
        },
        "symptom_duration": {
            "onset_period": "variable",
            "critical_period": "ongoing",
            "recovery_period": "chronic condition requiring lifelong management"
        }
    },
    
    "Flu": {
        "critical_symptoms": {
            "fever": 3.0,
            "chills": 3.0,
            "body_ache": 3.0,
            "fatigue": 2.8 # Increased weight
        },
        "high_priority": {
            "sore_throat": 2.0,
            "cough": 2.0,
            "headache": 2.0,
            "muscle_and_joint_pain": 2.5 # Added and increased weight
        },
        "medium_priority": {
            "runny_nose": 1.0,
            "congestion": 1.0
        },
        "min_critical_needed": 2, # Lowered requirement
        "min_high_needed": 2,
        "description": "A common viral infection that attacks the respiratory system",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
    },
    
    "Asthma": {
        "critical_symptoms": {
            "breathing_difficulty": 3.0,
            "wheezing": 3.0,
            "chest_tightness": 3.0,
            "shortness_of_breath": 2.8 # Increased weight
        },
        "high_priority": {
            "cough": 2.0,
            "chest_discomfort": 2.5 # Increased weight
        },
        "medium_priority": {
            "fatigue": 1.0
        },
        "min_critical_needed": 2, # Kept as 2
        "min_high_needed": 1,
        "description": "A chronic respiratory disease that inflames and narrows the airways",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": True
    },
    
    "Pneumonia": {
        "critical_symptoms": {
            "cough": 3.0,
            "fever": 3.0,
            "breathing_difficulty": 3.0,
            "chest_pain": 3.0,
            "shortness_of_breath": 2.8 # Increased weight
        },
        "high_priority": {
            "chills": 2.0,
            "fatigue": 2.0,
            "production_of_mucus": 2.5 # Added and increased weight
        },
        "medium_priority": {
            "nausea": 1.0,
            "vomiting": 1.0,
            "diarrhea": 1.0
        },
        "min_critical_needed": 2, # Lowered requirement
        "min_high_needed": 2,
        "description": "An infection that inflames the air sacs in one or both lungs",
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    
    "Hepatitis": {
        "critical_symptoms": {
            "jaundice": 3.0,
            "yellowing_skin": 3.0,
            "yellowing_eyes": 3.0,
            "right_upper_abdominal_pain": 3.0,
            "dark_urine": 3.0,
            "yellowish_skin": 3.0
        },
        "high_priority": {
            "fatigue": 2.0,
            "nausea": 2.0,
            "vomiting": 2.0,
            "loss_of_appetite": 2.0,
            "fever": 2.0,
            "pale_stools": 2.0
        },
        "medium_priority": {
            "abdominal_pain": 1.0,
            "muscle_pain": 1.0,
            "joint_pain": 1.0,
            "weakness": 1.0,
            "weight_loss": 1.0
        },
        "min_critical_needed": 1,
        "min_high_needed": 2,
        "description": "Inflammation of the liver typically caused by viral infection or liver damage",
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "exclude_symptoms": [
            "diarrhea", "loose_stools", "food_poisoning_symptoms",
            "rose_spots", "constipation"
        ]
    },
    
    "Depression": {
        "critical_symptoms": {
            "persistent_sadness": 3.0,
            "loss_of_interest": 3.0,
            "fatigue": 3.0
        },
        "high_priority": {
            "changes_in_sleep": 2.0,
            "changes_in_appetite": 2.0,
            "difficulty_concentrating": 2.0,
            "feelings_of_worthlessness": 2.0
        },
        "medium_priority": {
            "irritability": 1.0,
            "physical_aches": 1.0,
             "headache": 0.8
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "A mood disorder that causes a persistent feeling of sadness and loss of interest",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
    },
    
    "Alzheimer": {
        "critical_symptoms": {
            "memory_loss": 3.0,
            "difficulty_thinking": 3.0,
            "difficulty_problem_solving": 3.0
        },
        "high_priority": {
            "confusion": 2.0,
            "difficulty_speaking": 2.0,
            "difficulty_walking": 2.0,
            "changes_in_mood": 2.0
        },
        "medium_priority": {
            "withdrawal_from_activities": 1.0,
            "fatigue": 0.8 # Added for overlap
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A progressive disease that destroys memory and other important mental functions",
        "danger_level": "HIGH",
        "requires_immediate_attention": False
    },
    
    "Parkinson": {
        "critical_symptoms": {
            "tremor": 3.0,
            "slowed_movement": 3.0,
            "rigid_muscles": 3.0
        },
        "high_priority": {
            "impaired_posture": 2.0,
            "loss_of_balance": 2.0,
            "loss_of_automatic_movements": 2.0,
            "speech_changes": 2.0
        },
        "medium_priority": {
            "writing_changes": 1.0,
            "loss_of_smell": 1.0,
            "fatigue": 0.8 # Added for overlap
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A progressive nervous system disorder that affects movement",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
    },
    
    "UTI": {
        "critical_symptoms": {
            "painful_urination": 3.0,
            "burning_sensation_urination": 3.0,
            "frequent_urination": 3.0
        },
        "high_priority": {
            "cloudy_urine": 2.0,
            "strong_smelling_urine": 2.0,
            "pelvic_pain": 2.0
        },
        "medium_priority": {
            "fever": 1.0,
            "fatigue": 1.0,
            "abdominal_pain": 0.8 # Added for overlap
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "An infection in any part of your urinary system",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
    }
}

def calculate_disease_confidence(symptoms, disease_profile, age_group=None, season=None):
    """
    Calculate confidence score for a disease based on matched symptoms with additional factors
    """
    matched_critical = 0
    matched_high = 0
    total_score = 0
    
    # Calculate base symptom scores
    for symptom in symptoms:
        if symptom in disease_profile["critical_symptoms"]:
            matched_critical += 1
            total_score += disease_profile["critical_symptoms"][symptom] * 3.0
        elif symptom in disease_profile["high_priority"]:
            matched_high += 1
            total_score += disease_profile["high_priority"][symptom] * 2.0
        elif symptom in disease_profile["medium_priority"]:
            total_score += disease_profile["medium_priority"][symptom] * 1.0
    
    # Calculate maximum possible score
    max_possible_score = (
        sum(disease_profile["critical_symptoms"].values()) * 3.0 +
        sum(disease_profile["high_priority"].values()) * 2.0 +
        sum(disease_profile["medium_priority"].values()) * 1.0
    )

    if max_possible_score == 0:
        return 0.0

    # Minimum requirements check with stricter enforcement
    if matched_critical < disease_profile["min_critical_needed"] or matched_high < disease_profile["min_high_needed"]:
        return 0.0
    
    # Calculate base confidence
    confidence = (total_score / max_possible_score) * 100
    
    # Critical symptom ratio - how many of the disease's critical symptoms are present?
    critical_ratio = matched_critical / len(disease_profile["critical_symptoms"])
    
    # Apply stricter threshold based on disease specificity
    disease_name = disease_profile.get("disease", "")
    
    # Define signature symptoms that strongly indicate specific diseases
    signature_symptoms = {
        "Flu": ["chills", "fever", "body_ache", "fatigue"],
        "Malaria": ["periodic_fever", "chills", "sweating"],
        "Chicken_Pox": ["itchy_rash", "blisters", "red_spots"],
        "Dengue": ["high_fever", "pain_behind_eyes", "muscle_and_joint_pain"],
        "Asthma": ["wheezing", "chest_tightness", "shortness_of_breath"],
        "Tuberculosis": ["persistent_cough", "coughing_blood", "weight_loss"],
        "Arthritis": ["joint_pain", "joint_stiffness", "reduced_joint_mobility"],
        "Pneumonia": ["cough", "high_fever", "breathing_difficulty", "production_of_mucus"],
        "Hepatitis": ["yellowing_skin", "yellowing_eyes", "dark_urine"],
        "Typhoid": ["high_fever", "abdominal_pain", "weakness"],
        "Alzheimer": ["memory_loss", "difficulty_thinking", "difficulty_problem_solving"],
        "Parkinson": ["tremor", "slowed_movement", "rigid_muscles"],
        "UTI": ["painful_urination", "burning_sensation_urination", "frequent_urination"]
    }
    
    # Check if the signature symptoms for this disease are present
    if disease_name in signature_symptoms:
        sig_symptoms = signature_symptoms[disease_name]
        sig_count = sum(1 for s in symptoms if s in sig_symptoms)
        sig_ratio = sig_count / len(sig_symptoms)
        
        # Boost confidence if signature symptoms are present
        if sig_ratio > 0.5:
            confidence *= (1.0 + sig_ratio)
        else:
            # Penalize if signature symptoms are missing
            confidence *= 0.7
    
    # Apply age-specific adjustments
    if age_group and age_group in disease_profile.get("age_specific_symptoms", {}):
        age_specific_symptoms = disease_profile["age_specific_symptoms"][age_group]
        age_matches = sum(1 for s in symptoms if s in age_specific_symptoms)
        confidence += age_matches * 5.0  # Add 5% per age-specific symptom match
    
    # Apply seasonal adjustments
    if season and season in disease_profile.get("seasonal_factor", []):
        confidence *= 1.2  # 20% boost for seasonal match
    
    # Disease-specific adjustments
    if disease_name == "Chicken_Pox":
        # Key symptoms combination for Chicken Pox
        if "itchy_rash" in symptoms and "blisters" in symptoms:
            confidence *= 1.5
    elif disease_name == "Malaria":
        # Key symptoms combination for Malaria
        if "periodic_fever" in symptoms and "chills" in symptoms:
            confidence *= 1.3
    elif disease_name == "Dengue":
        # Key symptoms combination for Dengue
        if "high_fever" in symptoms and "pain_behind_eyes" in symptoms:
            confidence *= 1.4
    elif disease_name == "Flu":
        # Key symptoms combination for Flu
        if "fever" in symptoms and "body_ache" in symptoms and "fatigue" in symptoms:
            confidence *= 1.3
    elif disease_name == "Asthma":
        # Key symptoms combination for Asthma
        if "wheezing" in symptoms and "chest_tightness" in symptoms:
            confidence *= 1.5
    elif disease_name == "Pneumonia":
        # Key symptoms for Pneumonia
        if "cough" in symptoms and "high_fever" in symptoms and "production_of_mucus" in symptoms:
            confidence *= 1.4
    elif disease_name == "Hepatitis":
        # Key symptoms for Hepatitis
        if "yellowing_skin" in symptoms and "yellowing_eyes" in symptoms:
            confidence *= 1.5
    elif disease_name == "Typhoid":
        # Key symptoms for Typhoid
        if "high_fever" in symptoms and "abdominal_pain" in symptoms:
            confidence *= 1.3
    
    # Check for conflicting symptoms - symptoms that strongly suggest it's NOT this disease
    conflicting_symptoms = {
        "Flu": ["itchy_rash", "yellowing_skin", "joint_stiffness", "memory_loss"],
        "Malaria": ["wheezing", "memory_loss", "tremor", "painful_urination"],
        "Chicken_Pox": ["wheezing", "joint_pain", "memory_loss", "tremor"],
        "Asthma": ["itchy_rash", "blisters", "yellowing_skin", "memory_loss"],
        "Arthritis": ["itchy_rash", "wheezing", "yellowing_skin", "memory_loss"],
        "Pneumonia": ["joint_stiffness", "memory_loss", "tremor", "yellowing_skin"],
        "Dengue": ["wheezing", "memory_loss", "tremor", "yellowing_skin"],
        "Hepatitis": ["itchy_rash", "wheezing", "joint_stiffness", "memory_loss"],
        "Typhoid": ["itchy_rash", "wheezing", "memory_loss", "tremor"],
        "Alzheimer": ["itchy_rash", "wheezing", "yellowing_skin", "painful_urination"],
        "Parkinson": ["itchy_rash", "yellowing_skin", "painful_urination"],
        "UTI": ["itchy_rash", "wheezing", "yellowing_skin", "memory_loss"],
        "Depression": ["itchy_rash", "blisters", "red_spots", "rash", "joint_pain", "yellowing_skin", "painful_urination"]
    }
    
    # Check for conflicting symptoms
    if disease_name in conflicting_symptoms:
        conflicts = sum(1 for s in symptoms if s in conflicting_symptoms[disease_name])
        if conflicts > 0:
            confidence *= (1.0 - (conflicts * 0.3))  # Reduce confidence for each conflicting symptom
    
    # If critical ratio is low, reduce confidence
    if critical_ratio < 0.5:
        confidence *= 0.8
    
    # Apply penalties for common symptoms
    common_symptoms = {"headache", "fatigue", "cough", "fever", "body_ache"}
    common_symptom_count = sum(1 for s in symptoms if s in common_symptoms)
    if common_symptom_count > 2 and critical_ratio < 0.6:
        confidence *= 0.85  # Penalty for having too many common symptoms but low critical ratio
    
    # Ensure confidence doesn't exceed 100% or go below 0%
    confidence = max(0, min(confidence, 100.0))
    
    return round(confidence, 2)

def predict_diseases(symptoms, age_group=None, season=None):
    """
    Predict possible diseases based on given symptoms and additional factors
    """
    predictions = []
    
    # Standardize symptom format (convert spaces to underscores and lowercase)
    standard_symptoms = []
    for symptom in symptoms:
        # Handle common variations
        symptom_lower = symptom.lower()
        if "high fever" in symptom_lower:
            standard_symptoms.append("high_fever")
        elif "mild fever" in symptom_lower or "slight fever" in symptom_lower:
            standard_symptoms.append("mild_fever")
        elif "periodic fever" in symptom_lower:
            standard_symptoms.append("periodic_fever")
        elif "fever" in symptom_lower:
            standard_symptoms.append("fever")
        elif "pain behind eyes" in symptom_lower:
            standard_symptoms.append("pain_behind_eyes")
        elif "muscle and joint pain" in symptom_lower:
            standard_symptoms.append("muscle_and_joint_pain")
        elif "itchy rash" in symptom_lower:
            standard_symptoms.append("itchy_rash")
        elif "skin rash" in symptom_lower:
            standard_symptoms.append("skin_rash")
        elif "rash" in symptom_lower:
            standard_symptoms.append("rash")
        elif "fatigue" in symptom_lower or "tiredness" in symptom_lower:
            standard_symptoms.append("fatigue")
        else:
            # Default conversion
            standard_symptoms.append(symptom_lower.replace(' ', '_'))
    
    for disease_name, profile in DISEASE_PROFILES.items():
        profile_copy = profile.copy()
        # Add disease name to the profile for reference
        profile_copy["disease"] = disease_name
        
        confidence = calculate_disease_confidence(standard_symptoms, profile_copy, age_group, season)
        
        # Higher confidence threshold to reduce false positives
        if confidence > 40.0:
            matched_critical = [s for s in standard_symptoms if s in profile["critical_symptoms"]]
            matched_high = [s for s in standard_symptoms if s in profile["high_priority"]]
            matched_medium = [s for s in standard_symptoms if s in profile["medium_priority"]]
            
            # Second validation: make sure we have enough critical symptoms ratio
            critical_ratio = len(matched_critical) / len(profile["critical_symptoms"]) if len(profile["critical_symptoms"]) > 0 else 0
            
            # Only include if we have a reasonable critical symptom match ratio
            if len(matched_critical) >= profile["min_critical_needed"] and critical_ratio >= 0.4:
                prediction = {
                    "disease": disease_name,
                    "confidence": confidence,
                    "danger_level": profile["danger_level"],
                    "requires_immediate_attention": profile["requires_immediate_attention"],
                    "description": profile["description"],
                    "matching_symptoms": {
                        "critical": matched_critical,
                        "high_priority": matched_high,
                        "medium_priority": matched_medium
                    },
                    "complications": profile.get("complications", []),
                    "treatment_recommendations": profile.get("treatment_recommendations", {}),
                    "symptom_duration": profile.get("symptom_duration", {})
                }
                
                if season and season in profile.get("seasonal_factor", []):
                    prediction["seasonal_match"] = True
                    prediction["seasonal_factors"] = SEASONS[season]
                
                if age_group and age_group in profile.get("age_specific_symptoms", {}):
                    prediction["age_specific_symptoms"] = profile["age_specific_symptoms"][age_group]
                
                predictions.append(prediction)
    
    # Sort predictions by confidence score
    predictions.sort(key=lambda x: x["confidence"], reverse=True)
    
    # Further filter: If we have high-confidence predictions, remove low-confidence ones
    if predictions and predictions[0]["confidence"] > 70:
        top_confidence = predictions[0]["confidence"]
        # Filter out predictions with significantly lower confidence
        predictions = [p for p in predictions if p["confidence"] > (top_confidence * 0.6)]
        
    return predictions

def get_suggested_symptoms(current_symptoms, age_group=None):
    """
    Suggest additional symptoms to check based on current symptoms and patient age
    """
    suggested = set()
    
    # Standardize symptom format (like in predict_diseases)
    standard_symptoms = []
    for symptom in current_symptoms:
        symptom_lower = symptom.lower()
        if "high fever" in symptom_lower:
            standard_symptoms.append("high_fever")
        elif "mild fever" in symptom_lower or "slight fever" in symptom_lower:
            standard_symptoms.append("mild_fever")
        elif "periodic fever" in symptom_lower:
            standard_symptoms.append("periodic_fever")
        elif "fever" in symptom_lower:
            standard_symptoms.append("fever")
        elif "pain behind eyes" in symptom_lower:
            standard_symptoms.append("pain_behind_eyes")
        elif "muscle and joint pain" in symptom_lower:
            standard_symptoms.append("muscle_and_joint_pain")
        elif "itchy rash" in symptom_lower:
            standard_symptoms.append("itchy_rash")
        elif "skin rash" in symptom_lower:
            standard_symptoms.append("skin_rash")
        elif "rash" in symptom_lower:
            standard_symptoms.append("rash")
        elif "fatigue" in symptom_lower or "tiredness" in symptom_lower:
            standard_symptoms.append("fatigue")
        else:
            standard_symptoms.append(symptom_lower.replace(' ', '_'))
    
    for disease, profile in DISEASE_PROFILES.items():
        has_some_symptoms = False
        for symptom in standard_symptoms:
            if (symptom in profile["critical_symptoms"] or 
                symptom in profile["high_priority"]):
                has_some_symptoms = True
                break
        
        if has_some_symptoms:
            # Suggest critical and high priority symptoms
            for symptom in profile["critical_symptoms"]:
                if symptom not in standard_symptoms:
                    suggested.add(symptom)
            for symptom in profile["high_priority"]:
                if symptom not in standard_symptoms:
                    suggested.add(symptom)
            
            # Add age-specific suggestions
            if age_group and age_group in profile.get("age_specific_symptoms", {}):
                for symptom in profile["age_specific_symptoms"][age_group]:
                    if symptom not in standard_symptoms:
                        suggested.add(symptom)
    
    return list(suggested)

def test_prediction_system():
    print("\n=== MEDIS Disease Prediction System V2.0 ===\n")
    
    # Run individual test cases
    test_malaria()
    test_chicken_pox() 
    test_dengue()
    test_common_cold()
    
    # Add new tests for problematic disease combinations
    test_flu()
    test_asthma()
    test_arthritis()
    test_hepatitis()
    test_typhoid()
    test_alzheimer()
    test_parkinson()
    test_uti()

def test_malaria():
    # Test Case 1: Malaria-like symptoms
    malaria_symptoms = [
        "periodic fever",
        "chills",
        "sweating",
        "severe headache",
        "nausea",
        "body ache",
        "fatigue",
        "vomiting"
    ]
    
    print("Test Case 1 - Malaria Symptoms:")
    print("Symptoms:", ", ".join(malaria_symptoms))
    predictions = predict_diseases(malaria_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

    # Get suggested additional symptoms
    suggested = get_suggested_symptoms(malaria_symptoms)
    print("\nSuggested additional symptoms to check:", ", ".join(suggested))

def test_chicken_pox():
    # Test Case 2: Chicken Pox-like symptoms
    print("\n" + "="*50 + "\n")
    chicken_pox_symptoms = [
        "itchy rash",
        "blisters",
        "red spots",
        "itching",
        "fever",
        "loss of appetite",
        "fatigue",
        "headache"
    ]
    
    print("Test Case 2 - Chicken Pox Symptoms:")
    print("Symptoms:", ", ".join(chicken_pox_symptoms))
    predictions = predict_diseases(chicken_pox_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_dengue():
    # Test Case 3: Dengue symptoms
    print("\n" + "="*50 + "\n")
    dengue_symptoms = [
        "high fever",
        "severe headache",
        "pain behind eyes",
        "muscle and joint pain",
        "rash",
        "fatigue"
    ]
    
    print("Test Case 3 - Dengue Symptoms:")
    print("Symptoms:", ", ".join(dengue_symptoms))
    predictions = predict_diseases(dengue_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_common_cold():
    # Test Case 4: Common Cold symptoms
    print("\n" + "="*50 + "\n")
    cold_symptoms = [
        "runny nose",
        "sore throat",
        "congestion",
        "cough",
        "mild fever"
    ]
    
    print("Test Case 4 - Common Cold Symptoms:")
    print("Symptoms:", ", ".join(cold_symptoms))
    predictions = predict_diseases(cold_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_flu():
    print("\n" + "="*50 + "\n")
    flu_symptoms = [
        "fever",
        "chills",
        "body ache",
        "fatigue",
        "cough",
        "headache",
        "sore throat"
    ]
    
    print("Test Case - Flu Symptoms:")
    print("Symptoms:", ", ".join(flu_symptoms))
    predictions = predict_diseases(flu_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_asthma():
    print("\n" + "="*50 + "\n")
    asthma_symptoms = [
        "wheezing",
        "chest tightness",
        "shortness of breath",
        "breathing difficulty",
        "cough",
        "chest discomfort"
    ]
    
    print("Test Case - Asthma Symptoms:")
    print("Symptoms:", ", ".join(asthma_symptoms))
    predictions = predict_diseases(asthma_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_arthritis():
    print("\n" + "="*50 + "\n")
    arthritis_symptoms = [
        "joint pain",
        "joint stiffness",
        "joint swelling",
        "reduced joint mobility",
        "morning stiffness",
        "joint warmth"
    ]
    
    print("Test Case - Arthritis Symptoms:")
    print("Symptoms:", ", ".join(arthritis_symptoms))
    predictions = predict_diseases(arthritis_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_hepatitis():
    print("\n" + "="*50 + "\n")
    hepatitis_symptoms = [
        "yellowing skin",
        "yellowing eyes",
        "dark urine",
        "fatigue",
        "abdominal pain",
        "loss of appetite"
    ]
    
    print("Test Case - Hepatitis Symptoms:")
    print("Symptoms:", ", ".join(hepatitis_symptoms))
    predictions = predict_diseases(hepatitis_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_typhoid():
    print("\n" + "="*50 + "\n")
    typhoid_symptoms = [
        "high fever",
        "weakness",
        "abdominal pain",
        "headache",
        "loss of appetite",
        "diarrhea"
    ]
    
    print("Test Case - Typhoid Symptoms:")
    print("Symptoms:", ", ".join(typhoid_symptoms))
    predictions = predict_diseases(typhoid_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_alzheimer():
    print("\n" + "="*50 + "\n")
    alzheimer_symptoms = [
        "memory loss",
        "difficulty thinking",
        "difficulty problem solving",
        "confusion",
        "difficulty speaking",
        "changes in mood"
    ]
    
    print("Test Case - Alzheimer Symptoms:")
    print("Symptoms:", ", ".join(alzheimer_symptoms))
    predictions = predict_diseases(alzheimer_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_parkinson():
    print("\n" + "="*50 + "\n")
    parkinson_symptoms = [
        "tremor",
        "slowed movement",
        "rigid muscles",
        "impaired posture",
        "loss of balance",
        "speech changes"
    ]
    
    print("Test Case - Parkinson Symptoms:")
    print("Symptoms:", ", ".join(parkinson_symptoms))
    predictions = predict_diseases(parkinson_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_uti():
    print("\n" + "="*50 + "\n")
    uti_symptoms = [
        "painful urination",
        "burning sensation urination",
        "frequent urination",
        "cloudy urine",
        "strong smelling urine",
        "pelvic pain"
    ]
    
    print("Test Case - UTI Symptoms:")
    print("Symptoms:", ", ".join(uti_symptoms))
    predictions = predict_diseases(uti_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_specific_symptoms():
    print("\n" + "="*50 + "\n")
    specific_symptoms = [
        "fever",
        "fatigue",
        "itchy rash",
        "blisters",
        "loss of appetite"
    ]
    
    print("Test Case - Specific Symptoms:")
    print("Symptoms:", ", ".join(specific_symptoms))
    predictions = predict_diseases(specific_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

def test_depression_vs_pox():
    print("\n" + "="*50 + "\n")
    mixed_symptoms = [
        "fatigue",
        "loss of appetite",
        "itchy rash",
        "blisters",
        "fever",
        "changes in sleep",  # Depression symptom
        "feelings of worthlessness"  # Depression symptom
    ]
    
    print("Test Case - Mixed Symptoms (Should be Chicken Pox, not Depression):")
    print("Symptoms:", ", ".join(mixed_symptoms))
    predictions = predict_diseases(mixed_symptoms)
    
    print("\nPredictions:")
    for pred in predictions:
        print(f"\nDisease: {pred['disease']}")
        print(f"Confidence: {pred['confidence']}%")
        print(f"Danger Level: {pred['danger_level']}")
        print("Matching Symptoms:")
        print("- Critical:", ", ".join(pred['matching_symptoms']['critical']))
        print("- High Priority:", ", ".join(pred['matching_symptoms']['high_priority']))
        if pred['matching_symptoms']['medium_priority']:
            print("- Medium Priority:", ", ".join(pred['matching_symptoms']['medium_priority']))

if __name__ == "__main__":
    test_specific_symptoms()
    test_depression_vs_pox() 