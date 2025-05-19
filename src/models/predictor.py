"""
Core prediction logic for the MEDIS system.
Provides disease prediction and symptom suggestion functionality.
"""

from .disease_profiles import (
    DISEASE_PROFILES,
    SYMPTOM_CATEGORIES,
    SYMPTOM_SEVERITY,
    AGE_GROUPS,
    SEASONS
)

def calculate_disease_confidence(symptoms, disease_profile, age_group=None, season=None):
    """Calculate confidence score for a disease based on symptoms and other factors."""
    score = 0
    matched_critical = 0
    matched_high = 0
    
    # Check critical symptoms
    for symptom, weight in disease_profile["critical_symptoms"].items():
        if symptom in symptoms:
            score += weight * 2
            matched_critical += 1
    
    # Check high priority symptoms
    for symptom, weight in disease_profile["high_priority"].items():
        if symptom in symptoms:
            score += weight * 1.5
            matched_high += 1
    
    # Check medium priority symptoms
    for symptom, weight in disease_profile["medium_priority"].items():
        if symptom in symptoms:
            score += weight
    
    # Age group specific symptoms
    if age_group and "age_specific_symptoms" in disease_profile:
        age_symptoms = disease_profile["age_specific_symptoms"].get(age_group, [])
        for symptom in age_symptoms:
            if symptom in symptoms:
                score += 2
    
    # Seasonal factors
    if season and "seasonal_factor" in disease_profile:
        if season in disease_profile["seasonal_factor"]:
            score *= 1.2
    
    # Check minimum requirements
    min_critical = disease_profile.get("min_critical_needed", 1)
    min_high = disease_profile.get("min_high_needed", 1)
    
    if matched_critical < min_critical or matched_high < min_high:
        score *= 0.5
    
    return score

def predict_diseases(symptoms, age_group=None, season=None):
    """
    Predict possible diseases based on symptoms and other factors.
    Returns list of diseases sorted by confidence score.
    """
    predictions = []
    
    for disease_name, profile in DISEASE_PROFILES.items():
        confidence = calculate_disease_confidence(symptoms, profile, age_group, season)
        if confidence > 0:
            predictions.append({
                "disease": disease_name,
                "confidence": confidence,
                "description": profile["description"],
                "danger_level": profile["danger_level"],
                "requires_immediate_attention": profile["requires_immediate_attention"]
            })
    
    # Sort by confidence score
    predictions.sort(key=lambda x: x["confidence"], reverse=True)
    
    return predictions

def get_suggested_symptoms(current_symptoms, age_group=None):
    """
    Suggest additional symptoms to check based on current symptoms.
    Returns list of suggested symptoms sorted by relevance.
    """
    suggestions = {}
    
    # Get diseases matching current symptoms
    possible_diseases = predict_diseases(current_symptoms, age_group)
    
    # For each possible disease, suggest its symptoms that aren't already reported
    for disease in possible_diseases[:3]:  # Consider top 3 matches
        profile = DISEASE_PROFILES[disease["disease"]]
        
        # Add critical symptoms first
        for symptom in profile["critical_symptoms"]:
            if symptom not in current_symptoms:
                suggestions[symptom] = suggestions.get(symptom, 0) + 3
        
        # Add high priority symptoms
        for symptom in profile["high_priority"]:
            if symptom not in current_symptoms:
                suggestions[symptom] = suggestions.get(symptom, 0) + 2
        
        # Add medium priority symptoms
        for symptom in profile["medium_priority"]:
            if symptom not in current_symptoms:
                suggestions[symptom] = suggestions.get(symptom, 0) + 1
    
    # Convert to list and sort by relevance score
    suggested_list = [{"symptom": s, "relevance": r} for s, r in suggestions.items()]
    suggested_list.sort(key=lambda x: x["relevance"], reverse=True)
    
    return suggested_list