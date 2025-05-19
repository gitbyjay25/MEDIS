"""
Critical disease patterns and scoring rules.
This module helps identify serious conditions that require immediate attention.
"""

CRITICAL_DISEASES = {
    "Hypertension": {
        "required_symptoms": {
            "headache": 3.0,
            "dizziness": 3.0,
            "vision_problems": 3.0,
            "nosebleeds": 3.0
        },
        "supporting_symptoms": {
            "chest_pain": 2.5,
            "shortness_of_breath": 2.5,
            "fatigue": 1.5,
            "irregular_heartbeat": 2.0,
            "anxiety": 1.0
        },
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    "Heart Attack": {
        "required_symptoms": {
            "severe_chest_pain": 3.0,
            "chest_pressure": 3.0,
            "left_arm_pain": 3.0
        },
        "supporting_symptoms": {
            "nausea": 2.0,
            "cold_sweats": 2.5,
            "dizziness": 2.0,
            "shortness_of_breath": 2.0,
            "anxiety": 1.5,
            "jaw_pain": 2.0
        },
        "min_required": 2,
        "min_supporting": 2,
        "danger_level": "CRITICAL",
        "requires_immediate_attention": True
    },
    "Malaria": {
        "required_symptoms": {
            "high_fever": 3.0,
            "chills": 3.0,
            "sweating": 3.0
        },
        "supporting_symptoms": {
            "headache": 2.0,
            "muscle_pain": 2.0,
            "fatigue": 2.0,
            "nausea": 1.5,
            "vomiting": 1.5
        },
        "seasonal_factors": ["MONSOON", "SUMMER"],
        "min_required": 2,
        "min_supporting": 2,
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    "Typhoid": {
        "required_symptoms": {
            "high_fever": 15.0,
            "persistent_fever": 15.0,
            "abdominal_pain": 15.0,
            "constipation_followed_by_diarrhea": 15.0,
            "weakness": 10.0
        },
        "supporting_symptoms": {
            "headache": 8.0,
            "loss_of_appetite": 8.0,
            "rose_spots": 10.0,
            "mild_cough": 5.0,
            "fatigue": 5.0
        },
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "physical_only": True,
        "exclude_symptoms": [
            "depression", "anxiety", "mood_changes",
            "yellow_skin", "yellow_eyes", "yellowish_skin",
            "itchy_rash", "blisters", "red_spots",
            "fluid_filled_blisters"
        ],
        "diagnostic_criteria": {
            "validation_rules": {
                "minimum_score_threshold": 20.0
            }
        }
    },
    "Jaundice": {
        "disease": "Jaundice",
        "required_symptoms": {
            "yellowish_skin": 20.0,
            "yellowing_eyes": 20.0, 
            "dark_urine": 15.0,
            "jaundice": 25.0,
            "pale_stools": 15.0,
            "clay_colored_stools": 15.0,
            "yellow_skin": 20.0,
            "yellow_eyes": 20.0,
            "yellowing_skin": 20.0,
            "yellowing of skin": 20.0,
            "yellow coloration": 20.0
        },
        "supporting_symptoms": {
            "fatigue": 10.0,
            "itching": 10.0,
            "weight_loss": 5.0,
            "nausea": 5.0
        },
        "min_required": 1,
        "min_supporting": 0,
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "physical_only": True,
        "exclude_symptoms": [],
        "differential_diagnosis": {
            "Food Poisoning": -30.0
        }
    },
    "Gastroenteritis": {
        "required_symptoms": {
            "vomiting": 3.0,
            "diarrhea": 3.0,
            "dehydration": 3.0
        },
        "supporting_symptoms": {
            "nausea": 2.0,
            "abdominal_pain": 2.0,
            "fever": 1.5,
            "fatigue": 1.5,
            "loss_of_appetite": 1.5
        },
        "seasonal_factors": ["MONSOON"],
        "min_required": 2,
        "min_supporting": 2,
        "danger_level": "MEDIUM",
        "requires_immediate_attention": True,
        "differential_diagnosis": {
            "Food Poisoning": -10.0
        }
    },
    "Pneumonia": {
        "required_symptoms": {
            "productive_cough_with_phlegm": 3.5,
            "severe_chest_congestion_with_crackling": 3.5,
            "pneumonia_specific_breathing_difficulty": 3.5,
            "localized_chest_infection": 3.5,
            "pneumonia_specific_fever": 3.5
        },
        "supporting_symptoms": {
            "abnormal_breath_sounds": 2.5,
            "coughing_thick_mucus": 2.5,
            "sharp_chest_pain_on_breathing": 2.5,
            "low_oxygen_saturation": 2.5,
            "pneumonia_fever_pattern": 2.5
        },
        "min_required": 4,
        "min_supporting": 3,
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "exclude_symptoms": [
            "itchy_rash", "fluid_filled_blisters", "skin_lesions",
            "jaundice", "dark_urine", "pale_skin",
            "persistent_headache", "joint_pain", "abdominal_pain",
            "sore_throat", "runny_nose", "nasal_congestion"
        ],
        "characteristic_factors": {
            "onset": "acute",
            "progression": "rapid_respiratory_decline",
            "nature": "lower_respiratory_infection",
            "location": "lung_specific",
            "key_identifiers": [
                "must_have_respiratory_symptoms",
                "must_have_chest_involvement",
                "must_have_infection_signs",
                "must_have_pneumonia_specific_signs"
            ],
            "validation_rules": {
                "minimum_respiratory_symptoms": 3,
                "minimum_chest_symptoms": 2,
                "requires_auscultation": True,
                "requires_lung_involvement": True,
                "requires_specific_fever_pattern": True
            }
        }
    },
    "Dengue": {
        "required_symptoms": {
            "high_fever": 15.0,
            "severe_headache": 15.0,
            "pain_behind_eyes": 15.0,
            "muscle_and_joint_pain": 15.0
        },
        "supporting_symptoms": {
            "rash": 10.0,
            "fatigue": 8.0,
            "nausea": 8.0,
            "vomiting": 8.0,
            "bleeding_tendency": 10.0
        },
        "seasonal_factors": ["MONSOON", "SUMMER"],
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "physical_only": True,
        "exclude_symptoms": [
            "constipation", "rose_spots", 
            "yellow_skin", "yellow_eyes", "dark_urine",
            "itchy_rash", "blisters", "fluid_filled_blisters"
        ]
    },
    "Tuberculosis": {
        "required_symptoms": {
            "persistent_cough": 3.0,
            "coughing_blood": 3.0,
            "chest_pain": 3.0,
            "weight_loss": 3.0
        },
        "supporting_symptoms": {
            "fatigue": 2.0,
            "fever": 2.0,
            "night_sweats": 2.0,
            "loss_of_appetite": 2.0,
            "shortness_of_breath": 2.0
        },
        "min_required": 2,
        "min_supporting": 2,
        "danger_level": "HIGH",
        "requires_immediate_attention": True
    },
    "Anemia": {
        "required_symptoms": {
            "extreme_fatigue": 3.0,
            "persistent_weakness": 3.0,
            "pale_skin": 3.0,
            "pale_gums_and_nailbeds": 3.0
        },
        "supporting_symptoms": {
            "dizziness": 2.5,
            "headache": 2.0,
            "cold_hands_and_feet": 2.5,
            "irregular_heartbeat": 2.0,
            "brittle_nails": 2.0,
            "unusual_cravings": 2.0
        },
        "min_required": 3,
        "min_supporting": 2,
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False,
        "exclude_symptoms": ["productive_cough", "high_fever", "chest_congestion"],
        "characteristic_factors": {
            "onset": "gradual",
            "progression": "slow",
            "nature": "nutritional_or_blood"
        }
    },
    "Bronchitis": {
        "required_symptoms": {
            "persistent_cough": 3.0,
            "mucus_production": 3.0,
            "chest_discomfort": 3.0,
            "shortness_of_breath": 3.0
        },
        "supporting_symptoms": {
            "fatigue": 2.0,
            "mild_fever": 2.0,
            "wheezing": 2.0,
            "chest_pain": 2.0,
            "sore_throat": 1.5
        },
        "min_required": 2,
        "min_supporting": 2,
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False
    },
    "Sinusitis": {
        "required_symptoms": {
            "nasal_congestion": 3.0,
            "facial_pain": 3.0,
            "headache": 3.0,
            "sinus_pressure": 3.0
        },
        "supporting_symptoms": {
            "cough": 2.0,
            "fatigue": 2.0,
            "reduced_smell": 2.0,
            "thick_nasal_discharge": 2.0,
            "post_nasal_drip": 1.5
        },
        "min_required": 2,
        "min_supporting": 2,
        "danger_level": "LOW",
        "requires_immediate_attention": False
    },
    "Hepatitis": {
        "disease": "Hepatitis",
        "required_symptoms": {
            "yellowish_skin": 15.0,
            "yellowing_eyes": 15.0,
            "dark_urine": 12.0,
            "right_upper_abdominal_pain": 25.0,
            "jaundice": 20.0,
            "fatigue": 8.0
        },
        "supporting_symptoms": {
            "nausea": 6.0,
            "loss_of_appetite": 10.0,
            "vomiting": 5.0,
            "fever": 4.0
        },
        "min_required": 1,
        "min_supporting": 1,
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "physical_only": True,
        "exclude_symptoms": [],
        "differential_diagnosis": {
            "Food Poisoning": -25.0,
            "Jaundice": -5.0
        }
    },
    "Chicken Pox": {
        "disease": "Chicken Pox",
        "required_symptoms": {
            "fluid_filled_blisters": 20.0,
            "itchy_rash": 20.0,
            "blisters": 20.0,
            "red_spots": 20.0
        },
        "supporting_symptoms": {
            "mild_fever": 10.0,
            "fever": 10.0,
            "headache": 8.0,
            "loss_of_appetite": 8.0,
            "fatigue": 8.0
        },
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "MEDIUM",
        "requires_immediate_attention": True,
        "physical_only": True,
        "exclude_symptoms": [
            "dry_cough", "shortness_of_breath", "loss_of_taste",
            "loss_of_smell", "chest_pain", "difficulty_breathing",
            "yellow_skin", "dark_urine", "yellow_eyes",
            "persistent_sadness", "loss_of_interest", "changes_in_sleep",
            "feelings_of_worthlessness", "difficulty_concentrating"
        ],
        "diagnostic_criteria": {
            "validation_rules": {
                "requires_rash": True,
                "rash_characteristics": [
                    "fluid_filled_blisters",
                    "itchy_rash",
                    "blisters",
                    "red_spots"
                ]
            }
        }
    },
    "COVID": {
        "disease": "COVID",
        "required_symptoms": {
            "persistent_dry_cough": 20.0,
            "high_fever": 20.0,
            "loss_of_taste": 20.0,
            "loss_of_smell": 20.0
        },
        "supporting_symptoms": {
            "difficulty_breathing": 10.0,
            "chest_pain": 10.0,
            "fatigue": 8.0,
            "body_aches": 8.0
        },
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "HIGH",
        "requires_immediate_attention": True,
        "physical_only": True,
        "exclude_symptoms": [
            "fluid_filled_blisters", "itchy_rash_clusters",
            "rash_different_stages", "red_spots_with_blisters",
            "yellow_skin", "dark_urine"
        ]
    },
    "Depression": {
        "disease": "Depression",
        "required_symptoms": {
            "persistent_sadness": 20.0,
            "loss_of_interest": 20.0,
            "fatigue": 15.0
        },
        "supporting_symptoms": {
            "changes_in_sleep": 10.0,
            "changes_in_appetite": 10.0,
            "difficulty_concentrating": 10.0,
            "feelings_of_worthlessness": 10.0
        },
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False,
        "physical_only": False,
        "exclude_symptoms": [
            "itchy_rash", "blisters", "red_spots", "fluid_filled_blisters",
            "red_spots_with_blisters", "itchy_rash_clusters", "rash_different_stages",
            "yellow_skin", "yellow_eyes", "dark_urine",
            "cough", "shortness_of_breath", "difficulty_breathing",
            "chest_pain", "chest_discomfort", "wheezing"
        ]
    },
    "Food Poisoning": {
        "disease": "Food Poisoning",
        "required_symptoms": {
            "nausea": 15.0,
            "vomiting": 15.0,
            "diarrhea": 15.0
        },
        "supporting_symptoms": {
            "stomach_pain": 10.0,
            "abdominal_pain": 10.0,
            "weakness": 8.0,
            "fever": 6.0,
            "headache": 5.0
        },
        "min_required": 2,
        "min_supporting": 1,
        "danger_level": "MEDIUM",
        "requires_immediate_attention": False,
        "physical_only": True,
        "exclude_symptoms": [
            "yellowish_skin", "yellow_skin", "yellowing_eyes", "yellow_eyes", 
            "jaundice", "dark_urine", "pale_stools", "clay_colored_stools",
            "right_upper_abdominal_pain"
        ],
        "differential_diagnosis": {
            "Gastroenteritis": -5.0
        }
    }
}

def calculate_critical_score(symptoms, disease_pattern, season=None):
    """
    Calculate confidence score for critical diseases based on specific patterns.
    Returns tuple of (score, requires_attention)
    """
    # Special immediate handling for Jaundice and Hepatitis
    if disease_pattern.get("disease") in ["Jaundice", "Hepatitis"]:
        # Define essential symptoms for each
        jaundice_essential = ["yellowish_skin", "yellow_skin", "yellowing_eyes", "yellow_eyes", "jaundice", 
                            "yellowing_skin", "yellowing of skin", "yellow coloration", "dark_urine"]
        hepatitis_essential = jaundice_essential + ["right_upper_abdominal_pain"]
        
        # Check for essential symptoms
        if disease_pattern.get("disease") == "Jaundice":
            # If any jaundice symptom is present, give minimum viable score
            if any(symptom in symptoms for symptom in jaundice_essential):
                base_score = 0.75  # Start with 75% confidence instead of 60%
                
                # Count matches for bonus score
                matches = sum(1 for s in jaundice_essential if s in symptoms)
                bonus = min(0.25, matches * 0.15)  # Up to 25% bonus, with more per match
                
                # Add additional score for key supporting symptoms
                if "dark_urine" in symptoms:
                    base_score += 0.1
                if "pale_stools" in symptoms or "clay_colored_stools" in symptoms:
                    base_score += 0.1
                if "itching" in symptoms:
                    base_score += 0.05
                
                return min(base_score + bonus, 1.0), True
                
        elif disease_pattern.get("disease") == "Hepatitis":
            # If right upper abdominal pain is present with any jaundice symptom, prioritize hepatitis
            if "right_upper_abdominal_pain" in symptoms and any(s in symptoms for s in jaundice_essential):
                return 0.9, True
            
            # If only right upper abdominal pain is present or only jaundice symptoms, give decent score
            elif "right_upper_abdominal_pain" in symptoms or any(s in symptoms for s in jaundice_essential):
                base_score = 0.7
                
                # Additional score for supporting symptoms
                if "loss_of_appetite" in symptoms:
                    base_score += 0.05
                if "fatigue" in symptoms:
                    base_score += 0.05
                if "nausea" in symptoms:
                    base_score += 0.03
                    
                return base_score, True
    
    # Special handling for Food Poisoning
    if disease_pattern.get("disease") == "Food Poisoning":
        # Core symptoms for food poisoning
        core_symptoms = ["nausea", "vomiting", "diarrhea", "stomach_pain", "abdominal_pain"]
        
        # Count how many core symptoms are present
        core_count = sum(1 for s in core_symptoms if s in symptoms)
        
        # If we have at least 3 core symptoms, strongly prioritize food poisoning
        if core_count >= 3:
            base_score = 0.8  # Start with 80% confidence
            
            # Add bonus for more symptoms
            bonus = min(0.2, (core_count - 3) * 0.1)  # Up to 20% bonus
            
            # Ensure we don't prioritize if jaundice symptoms are present
            jaundice_symptoms = ["yellowing_skin", "yellow_skin", "yellowing_eyes", 
                                "yellow_eyes", "jaundice", "dark_urine"]
            if any(s in symptoms for s in jaundice_symptoms):
                return 0, False  # Reject food poisoning if jaundice symptoms present
                
            return base_score + bonus, True
    
    # Handle specific disease conflicts - completely exclude Food Poisoning when Jaundice/Hepatitis symptoms are present
    if disease_pattern.get("disease") == "Food Poisoning" or disease_pattern.get("disease", "") == "Food Poisoning":
        # If there are yellowing symptoms, this is NOT food poisoning
        yellowing_symptoms = ["yellowing_skin", "yellow_skin", "yellowing_eyes", "yellow_eyes", "dark_urine", "jaundice", 
                             "clay_colored_stools", "pale_stools", "right_upper_abdominal_pain"]
        
        if any(symptom in symptoms for symptom in yellowing_symptoms):
            return 0, False  # Completely reject Food Poisoning if any jaundice symptoms present

    # Special boost for Hepatitis and Jaundice when their key symptoms are present
    if disease_pattern.get("disease") in ["Hepatitis", "Jaundice"]:
        liver_symptoms = ["yellowing_skin", "yellow_skin", "yellowing_eyes", "yellow_eyes", "dark_urine", "jaundice"]
        
        # Count how many liver symptoms are present
        liver_symptom_count = sum(1 for s in liver_symptoms if s in symptoms)
        
        # If we have multiple liver symptoms, give a big confidence boost
        if liver_symptom_count >= 2:
            # Starting with high confidence
            base_score = 0.85
            
            # Additional boost for more symptoms
            extra_boost = min(0.15, (liver_symptom_count-2) * 0.05)
            
            # Check for differential diagnosis rules
            if "differential_diagnosis" in disease_pattern:
                for conflicting_disease, penalty in disease_pattern["differential_diagnosis"].items():
                    if conflicting_disease.lower() == "food poisoning":
                        # If food poisoning symptoms are present, slightly reduce confidence 
                        # but still keep it high for liver diseases
                        fp_symptoms = ["vomiting", "diarrhea", "nausea"]
                        fp_count = sum(1 for s in fp_symptoms if s in symptoms)
                        if fp_count > 0:
                            # Small reduction but never below 0.7 for liver diseases with liver symptoms
                            base_score = max(0.7, base_score - (fp_count * 0.05))
            
            return base_score + extra_boost, True
    
    # Block all other diseases if clear Jaundice symptoms are present
    jaundice_symptoms = {
        "primary": ["yellow_skin", "yellow_eyes", "yellowing_skin", "yellowing_eyes", "dark_urine", "pale_stools", "jaundice"],
        "secondary": ["itching", "abdominal_pain", "fatigue", "right_upper_abdominal_pain"]
    }
    
    # Count how many primary and secondary Jaundice symptoms are present
    primary_count = sum(1 for s in jaundice_symptoms["primary"] if s in symptoms)
    secondary_count = sum(1 for s in jaundice_symptoms["secondary"] if s in symptoms)
    
    # If we have enough Jaundice symptoms, block other diseases
    if primary_count >= 2:  # At least 2 primary symptoms
        if disease_pattern.get("disease") not in ["Jaundice", "Hepatitis"]:
            return 0, False
    
    score = 0
    matched_required = 0
    matched_supporting = 0
    
    # Special handling for Jaundice
    if disease_pattern.get("disease") == "Jaundice":
        # Must have yellowing symptoms
        if not any(s in symptoms for s in ["yellow_skin", "yellow_eyes", "yellowing_skin", "yellowing_eyes", "jaundice"]):
            return 0, False
            
        # Calculate primary symptom match percentage
        primary_match_percent = primary_count / len(jaundice_symptoms["primary"])
        
        # If we have both yellow skin and eyes, give very high confidence
        if any(s in symptoms for s in ["yellow_skin", "yellowing_skin"]) and any(s in symptoms for s in ["yellow_eyes", "yellowing_eyes"]):
            score = 0.9  # Start with 90% confidence
            
            # Add more confidence for additional primary symptoms
            if "dark_urine" in symptoms:
                score += 0.05
            if "pale_stools" in symptoms or "clay_colored_stools" in symptoms:
                score += 0.05
                
            # Add small boost for secondary symptoms
            score += min(0.1, secondary_count * 0.03)
            
            return min(score, 1.0), True
            
        # For other combinations of primary symptoms
        if primary_count >= 2:
            score = 0.8  # Start with 80% confidence
            score += min(0.2, secondary_count * 0.05)  # Add up to 20% for secondary symptoms
    
    # Special handling for Hepatitis similar to Jaundice
    if disease_pattern.get("disease") == "Hepatitis":
        # Must have yellowing symptoms or right upper abdominal pain
        if not (any(s in symptoms for s in ["yellow_skin", "yellow_eyes", "yellowing_skin", "yellowing_eyes", "jaundice"]) or 
                "right_upper_abdominal_pain" in symptoms):
            return 0, False
        
        # If we have liver-specific symptoms, give high confidence
        if ("right_upper_abdominal_pain" in symptoms and 
            any(s in symptoms for s in ["yellow_skin", "yellow_eyes", "yellowing_skin", "yellowing_eyes", "dark_urine", "jaundice"])):
            score = 0.9  # Start with 90% confidence
            
            # Add small boost for additional symptoms
            if "fatigue" in symptoms:
                score += 0.03
            if "loss_of_appetite" in symptoms:
                score += 0.03
            if "nausea" in symptoms:
                score += 0.02
                
            return min(score, 1.0), True
    
    # Check required symptoms for other diseases
    required_symptoms = disease_pattern["required_symptoms"]
    total_weight = sum(weight for weight in required_symptoms.values())
    
    for symptom, weight in required_symptoms.items():
        if symptom in symptoms:
            matched_required += 1
            score += (weight / total_weight) * 0.7  # Scale to 70% max for required symptoms
    
    # If not enough required symptoms, return early
    min_required = disease_pattern.get("min_required", 1)
    if matched_required < min_required:
        return 0, False
    
    # Check supporting symptoms
    supporting_symptoms = disease_pattern["supporting_symptoms"]
    total_supporting_weight = sum(weight for weight in supporting_symptoms.values())
    
    for symptom, weight in supporting_symptoms.items():
        if symptom in symptoms:
            matched_supporting += 1
            score += (weight / total_supporting_weight) * 0.3  # Scale to 30% max for supporting symptoms
    
    min_supporting = disease_pattern.get("min_supporting", 1)
    
    if matched_required >= min_required and matched_supporting >= min_supporting:
        # Calculate match percentages
        required_match_percent = matched_required / len(required_symptoms)
        supporting_match_percent = matched_supporting / len(supporting_symptoms)
        
        # Calculate final score giving more weight to required symptoms
        final_score = (required_match_percent * 0.7) + (supporting_match_percent * 0.3)
        
        # Combine with accumulated score
        final_score = (final_score + score) / 2
        
        # Ensure minimum confidence of 70% for good matches
        if required_match_percent >= 0.5 and supporting_match_percent >= 0.3:
            final_score = max(final_score, 0.7)
            
        return min(final_score, 1.0), True
    
    return 0, False

def check_critical_diseases(symptoms, season=None):
    """Check for critical diseases that need immediate attention"""
    critical_results = []
    
    # Heart Attack detection - DISABLED to rely solely on ML model
    # We're commenting out the special heart attack detection to avoid duplicate predictions
    # heart_attack_symptoms = ['chest_pain', 'severe_chest_pain', 'chest_pressure', 'chest_tightness', 
    #                        'left_arm_pain', 'jaw_pain', 'shortness_of_breath', 'sweating', 
    #                        'cold_sweats', 'nausea', 'lightheadedness', 'dizziness', 'anxiety']
    
    # heart_attack_matches = sum(1 for s in symptoms if s in heart_attack_symptoms)
    
    # Make heart attack detection more sensitive - if ANY primary heart attack symptoms are present
    # primary_symptoms = ['chest_pain', 'severe_chest_pain', 'chest_pressure', 'chest_tightness', 'left_arm_pain']
    # has_primary_heart_symptom = any(s in primary_symptoms for s in symptoms)
    
    # if has_primary_heart_symptom or heart_attack_matches >= 2:
    #     confidence = min(1.0, 0.3 + (heart_attack_matches / len(heart_attack_symptoms)) * 0.7)
    #     
    #     # Boost confidence if key symptoms are present
    #     if 'chest_pain' in symptoms or 'severe_chest_pain' in symptoms:
    #         confidence += 0.2
    #     if 'left_arm_pain' in symptoms:
    #         confidence += 0.2
    #     if 'jaw_pain' in symptoms:
    #         confidence += 0.15
    #         
    #     confidence = min(1.0, confidence)  # Cap at 1.0
    #     
    #     critical_results.append({
    #         'disease': 'Heart Attack',
    #         'confidence': confidence,
    #         'danger_level': 'HIGH',
    #         'requires_immediate_attention': True,
    #         'emergency_signs': [
    #             'Chest pain or discomfort',
    #             'Pain radiating to arm, jaw, or back',
    #             'Shortness of breath',
    #             'Cold sweats',
    #             'Nausea or vomiting'
    #         ]
    #     })
    
    for disease, pattern in CRITICAL_DISEASES.items():
        # Skip Heart Attack to let ML model handle it exclusively
        if disease == "Heart Attack":
            continue
            
        score, requires_attention = calculate_critical_score(symptoms, pattern, season)
        if score > 0:
            critical_results.append({
                "disease": disease,
                "confidence": score,
                "danger_level": pattern["danger_level"],
                "requires_immediate_attention": pattern["requires_immediate_attention"] and requires_attention
            })
    
    # Sort by confidence score
    critical_results.sort(key=lambda x: x["confidence"], reverse=True)
    return critical_results 