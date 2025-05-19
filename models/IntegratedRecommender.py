from backend.medicine_recommendation import MedicineRecommender
from models.exercise_recommendation import ExerciseRecommender

class IntegratedRecommender:
    def __init__(self):
        self.medicine_recommender = MedicineRecommender()
        self.exercise_recommender = ExerciseRecommender()
        
    @classmethod
    def load_model(cls):
        return cls()
        
    def get_recommendations(self, disease, age=None, gender=None, confidence_score=None, conditions=None):
        """Get integrated recommendations for a disease"""
        
        # Get medicine recommendations for the specific disease
        medicine_recs = self.medicine_recommender.get_recommendations(disease, age, gender)
        
        # Determine exercise phase based on conditions
        phase = 'acute_phase'  # Default to acute phase
        if conditions and isinstance(conditions, list):
            # If patient has been recovering for a while or symptoms are mild
            recovery_indicators = ['recovering', 'mild', 'improving', 'better']
            if any(indicator in condition.lower() for condition in conditions for indicator in recovery_indicators):
                phase = 'recovery_phase'
        
        # Get exercise recommendations for the specific disease and phase
        exercise_recs = self.exercise_recommender.get_recommendations(
            disease=disease,
            phase=phase,
            age=age,
            conditions=conditions
        )
        
        # Get progression plan for exercises
        exercise_progression = self.exercise_recommender.get_progression_plan(disease, weeks=4)
        
        # Disease-specific diet recommendations
        diet_recs = self._get_diet_recommendations(disease)
        
        # Disease-specific lifestyle modifications
        lifestyle_recs = self._get_lifestyle_recommendations(disease)
        
        # Format medicine recommendations
        formatted_medicines = []
        if isinstance(medicine_recs, dict) and 'medicines' in medicine_recs:
            formatted_medicines = medicine_recs['medicines']
        elif isinstance(medicine_recs, list):
            for med in medicine_recs:
                if isinstance(med, dict):
                    formatted_medicines.append({
                        'medicine': med.get('medicine', ''),
                        'dosage': med.get('dosage', ''),
                        'purpose': med.get('purpose', '')
                    })
        
        # Compile all recommendations
        recommendations = {
            'medicines': formatted_medicines,
            'warnings': exercise_recs.get('warnings', []),
            'exercises': exercise_recs.get('exercises', []),
            'exercise_intensity': exercise_recs.get('intensity', 'light'),
            'intensity_guidelines': exercise_recs.get('intensity_guidelines', {}),
            'exercise_warnings': exercise_recs.get('warnings', []),
            'exercise_progression': exercise_progression,
            'diet': diet_recs,
            'lifestyle': lifestyle_recs
        }
        
        # Add warning for low confidence predictions
        if confidence_score and confidence_score < 0.5:
            if 'warnings' not in recommendations:
                recommendations['warnings'] = []
            recommendations['warnings'].append("This is a preliminary recommendation. Please consult a healthcare provider for accurate diagnosis and treatment.")
        
        return recommendations
        
    def _get_diet_recommendations(self, disease):
        """Get disease-specific diet recommendations"""
        disease_lower = disease.lower()
        
        if 'respiratory' in disease_lower or 'pneumonia' in disease_lower or 'bronchitis' in disease_lower:
            return [
                "Protein-rich foods - Support immune system",
                "Vitamin C rich fruits - Boost immunity",
                "Warm soups and broths - Ease congestion",
                "Honey and ginger - Soothe throat",
                "Stay well hydrated - Essential for recovery"
            ]
        elif 'fever' in disease_lower or 'flu' in disease_lower:
            return [
                "Clear broths - Stay hydrated",
                "Citrus fruits - Vitamin C boost",
                "Light, easily digestible foods",
                "Honey and lemon tea - Soothe throat",
                "Avoid heavy, greasy foods"
            ]
        else:
            return [
                "Balanced diet - Support overall health",
                "Stay hydrated - Essential for recovery",
                "Fresh fruits and vegetables - Boost immunity",
                "Protein-rich foods - Support healing",
                "Avoid processed foods - Reduce inflammation"
            ]
            
    def _get_lifestyle_recommendations(self, disease):
        """Get disease-specific lifestyle recommendations"""
        disease_lower = disease.lower()
        
        if 'respiratory' in disease_lower or 'pneumonia' in disease_lower or 'bronchitis' in disease_lower:
            return [
                "Get adequate rest",
                "Use a humidifier",
                "Avoid smoking and second-hand smoke",
                "Practice good hand hygiene",
                "Sleep with head elevated"
            ]
        elif 'fever' in disease_lower or 'flu' in disease_lower:
            return [
                "Get plenty of rest",
                "Stay home to prevent spread",
                "Keep warm",
                "Monitor temperature",
                "Maintain good hygiene"
            ]
        else:
            return [
                "Get adequate rest",
                "Maintain good hygiene",
                "Avoid stress",
                "Seek medical attention if symptoms worsen"
            ] 