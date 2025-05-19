import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MedicineRecommender:
    def __init__(self):
        self.medicine_data = None
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.medicine_vectors = None
        self.disease_medicine_map = {}
        self.medicine_details = {}
        
    def load_data(self, data_path):
        """Load medicine data from CSV file"""
        try:
            self.medicine_data = pd.read_csv(data_path)
            self._process_data()
            return True
        except Exception as e:
            print(f"Error loading medicine data: {e}")
            return False
    
    def _process_data(self):
        """Process medicine data and create necessary mappings"""
        # Create disease-medicine mapping with age and gender considerations
        for _, row in self.medicine_data.iterrows():
            disease = row['Disease'].lower()
            medicine = row['Medicine'].lower()
            dosage = row['Dosage']
            side_effects = row['Side_Effects']
            age_group = row.get('Age_Group', 'all')  # Default to 'all' if not specified
            gender = row.get('Gender', 'all')  # Default to 'all' if not specified
            
            if disease not in self.disease_medicine_map:
                self.disease_medicine_map[disease] = {
                    'all': [],  # For all ages and genders
                    'age_groups': {},  # Age-specific recommendations
                    'gender': {}  # Gender-specific recommendations
                }
            
            # Add to general recommendations
            self.disease_medicine_map[disease]['all'].append({
                'medicine': medicine,
                'dosage': dosage,
                'side_effects': side_effects
            })
            
            # Add age-specific recommendations
            if age_group != 'all':
                if age_group not in self.disease_medicine_map[disease]['age_groups']:
                    self.disease_medicine_map[disease]['age_groups'][age_group] = []
                self.disease_medicine_map[disease]['age_groups'][age_group].append({
                    'medicine': medicine,
                    'dosage': dosage,
                    'side_effects': side_effects
                })
            
            # Add gender-specific recommendations
            if gender != 'all':
                if gender not in self.disease_medicine_map[disease]['gender']:
                    self.disease_medicine_map[disease]['gender'][gender] = []
                self.disease_medicine_map[disease]['gender'][gender].append({
                    'medicine': medicine,
                    'dosage': dosage,
                    'side_effects': side_effects
                })
            
            # Store medicine details
            self.medicine_details[medicine] = {
                'dosage': dosage,
                'side_effects': side_effects,
                'age_group': age_group,
                'gender': gender
            }
    
    def get_recommendations(self, disease, age=None, gender=None):
        """Get medicine recommendations for a given disease, age, and gender"""
        disease = disease.lower()
        if disease not in self.disease_medicine_map:
            return []
        
        recommendations = []
        
        # Add general recommendations
        recommendations.extend(self.disease_medicine_map[disease]['all'])
        
        # Add age-specific recommendations
        if age is not None:
            age_group = self._get_age_group(age)
            if age_group in self.disease_medicine_map[disease]['age_groups']:
                recommendations.extend(self.disease_medicine_map[disease]['age_groups'][age_group])
        
        # Add gender-specific recommendations
        if gender is not None:
            gender = gender.lower()
            if gender in self.disease_medicine_map[disease]['gender']:
                recommendations.extend(self.disease_medicine_map[disease]['gender'][gender])
        
        return recommendations
    
    def _get_age_group(self, age):
        """Convert age to age group"""
        if age < 12:
            return 'child'
        elif age < 18:
            return 'teen'
        elif age < 60:
            return 'adult'
        else:
            return 'elderly'
    
    def get_medicine_details(self, medicine):
        """Get detailed information about a specific medicine"""
        medicine = medicine.lower()
        return self.medicine_details.get(medicine, None)

# Create a singleton instance
medicine_recommender = MedicineRecommender() 