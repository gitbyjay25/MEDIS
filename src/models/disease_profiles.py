"""
Disease profiles and constants for the MEDIS system.
"""

SYMPTOM_CATEGORIES = {
    "fever_types": {
        "high_fever": 3.0,
        "periodic_fever": 3.0,
        "mild_fever": 1.0,
        "intermittent_fever": 2.0
    },
    "pain_types": {
        "headache": 2.0,
        "severe_headache": 3.0,
        "body_ache": 2.0,
        "joint_pain": 2.0,
        "muscle_pain": 2.0,
        "chest_pain": 3.0
    },
    "skin_related": {
        "skin_rash": 3.0,
        "red_spots": 3.0,
        "itching": 2.0,
        "skin_peeling": 2.0
    },
    "respiratory": {
        "cough": 2.0,
        "dry_cough": 3.0,
        "breathing_difficulty": 3.0,
        "congestion": 1.0
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
            "sweating": 3.0
        },
        "high_priority": {
            "severe_headache": 2.0,
            "nausea": 2.0,
            "body_ache": 2.0,
            "fatigue": 2.0,
            "vomiting": 2.0
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
    "Dengue": {
        "critical_symptoms": {
            "high_fever": 3.0,
            "severe_body_ache": 3.0,
            "platelets_low": 3.0
        },
        "high_priority": {
            "rash": 2.0,
            "fatigue": 2.0,
            "severe_headache": 2.0,
            "nausea": 2.0,
            "eye_pain": 2.0
        },
        "medium_priority": {
            "joint_pain": 1.0,
            "muscle_pain": 1.0,
            "weakness": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A viral infection spread by mosquitoes",
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    "Chicken_Pox": {
        "critical_symptoms": {
            "skin_rash": 3.0,
            "red_spots": 3.0,
            "itching": 3.0
        },
        "high_priority": {
            "mild_fever": 2.0,
            "fatigue": 2.0,
            "swelled_lymph_nodes": 2.0
        },
        "medium_priority": {
            "headache": 1.0,
            "loss_of_appetite": 1.0,
            "weakness": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "A highly contagious viral infection",
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
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
            "sore_throat": 2.0
        },
        "medium_priority": {
            "headache": 1.0,
            "diarrhea": 1.0,
            "congestion": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "Viral infection caused by SARS-CoV-2",
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    "Typhoid": {
        "critical_symptoms": {
            "high_fever": 3.0,
            "weakness": 3.0,
            "abdominal_pain": 3.0
        },
        "high_priority": {
            "headache": 2.0,
            "loss_of_appetite": 2.0,
            "diarrhea": 2.0
        },
        "medium_priority": {
            "fatigue": 1.0,
            "muscle_pain": 1.0,
            "nausea": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 2,
        "description": "A bacterial infection that can spread throughout the body",
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "seasonal_factor": ["SUMMER", "MONSOON"],
        "age_specific_symptoms": {
            "CHILD": ["lethargy", "poor_appetite"],
            "ADULT": ["rose_spots", "enlarged_spleen"],
            "ELDERLY": ["confusion", "severe_complications"]
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
            "sneezing": 2.0
        },
        "medium_priority": {
            "headache": 1.0,
            "fatigue": 1.0,
            "body_ache": 1.0
        },
        "min_critical_needed": 2,
        "min_high_needed": 1,
        "description": "A viral infection of the upper respiratory tract",
        "danger_level": "LOW",
        "requires_immediate_attention": False,
        "seasonal_factor": ["WINTER"]
    }
} 