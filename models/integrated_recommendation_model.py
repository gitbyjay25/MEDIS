import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib
import os

class IntegratedRecommender:
    def __init__(self):
        self.disease_recommendations = {
            'Common Cold': {
                'medicines': [
                    {'name': 'Paracetamol', 'dosage': '500-1000mg every 4-6 hours', 'purpose': 'Fever and pain relief'},
                    {'name': 'Chlorpheniramine', 'dosage': '4mg every 4-6 hours', 'purpose': 'Runny nose and sneezing'},
                    {'name': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Cough and congestion'}
                ],
                'diet': [
                    {'item': 'Hot chicken soup', 'benefit': 'Helps clear nasal congestion and provides hydration'},
                    {'item': 'Citrus fruits', 'benefit': 'Rich in Vitamin C to boost immunity'},
                    {'item': 'Ginger tea with honey', 'benefit': 'Soothes throat and has anti-inflammatory properties'},
                    {'item': 'Garlic', 'benefit': 'Natural antimicrobial properties'},
                    {'item': 'Yogurt', 'benefit': 'Probiotics support immune system'}
                ],
                'exercises': [
                    {'name': 'Deep breathing', 'duration': '5-10 minutes', 'benefit': 'Helps clear airways'},
                    {'name': 'Light walking', 'duration': '10-15 minutes', 'benefit': 'Maintains circulation'},
                    {'name': 'Gentle stretching', 'duration': '5-10 minutes', 'benefit': 'Relieves muscle tension'}
                ],
                'lifestyle': [
                    'Get adequate rest and sleep',
                    'Stay hydrated with warm fluids',
                    'Use a humidifier in your room',
                    'Avoid cold beverages'
                ]
            },
            'Bronchitis': {
                'medicines': [
                    {'name': 'Dextromethorphan', 'dosage': '15-30mg every 6-8 hours', 'purpose': 'Cough suppression'},
                    {'name': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Expectorant'},
                    {'name': 'Salbutamol inhaler', 'dosage': '2 puffs every 4-6 hours', 'purpose': 'Breathing relief'}
                ],
                'diet': [
                    {'item': 'Warm clear broths', 'benefit': 'Hydration and mucus thinning'},
                    {'item': 'Honey', 'benefit': 'Natural cough suppressant'},
                    {'item': 'Ginger', 'benefit': 'Anti-inflammatory properties'},
                    {'item': 'Turmeric milk', 'benefit': 'Reduces inflammation'},
                    {'item': 'Green tea', 'benefit': 'Antioxidant properties'}
                ],
                'exercises': [
                    {'name': 'Pursed lip breathing', 'duration': '5-10 minutes', 'benefit': 'Improves breathing control'},
                    {'name': 'Diaphragmatic breathing', 'duration': '10 minutes', 'benefit': 'Strengthens breathing muscles'},
                    {'name': 'Light walking', 'duration': '15-20 minutes', 'benefit': 'Improves lung capacity'}
                ],
                'lifestyle': [
                    'Avoid smoking and second-hand smoke',
                    'Keep your living space well-ventilated',
                    'Use a humidifier',
                    'Avoid irritants like dust and strong fragrances'
                ]
            },
            'Pneumonia': {
                'medicines': [
                    {'name': 'Antibiotics', 'dosage': 'As prescribed', 'purpose': 'Treat bacterial infection'},
                    {'name': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever reduction'},
                    {'name': 'Expectorant', 'dosage': 'As directed', 'purpose': 'Loosen mucus'}
                ],
                'diet': [
                    {'item': 'Protein-rich foods', 'benefit': 'Support recovery and immunity'},
                    {'item': 'Vitamin C rich fruits', 'benefit': 'Boost immune system'},
                    {'item': 'Clear broths', 'benefit': 'Hydration and nutrition'},
                    {'item': 'Leafy greens', 'benefit': 'Rich in nutrients'},
                    {'item': 'Probiotic yogurt', 'benefit': 'Gut health support'}
                ],
                'exercises': [
                    {'name': 'Deep breathing exercises', 'duration': '5-10 minutes', 'benefit': 'Improve lung function'},
                    {'name': 'Incentive spirometry', 'duration': '10 times per hour', 'benefit': 'Prevent lung complications'},
                    {'name': 'Gentle walking', 'duration': 'As tolerated', 'benefit': 'Maintain mobility'}
                ],
                'lifestyle': [
                    'Complete bed rest initially',
                    'Regular deep breathing exercises',
                    'Keep room well-ventilated',
                    'Follow up with doctor regularly'
                ]
            },
            'Gastritis': {
                'medicines': [
                    {'name': 'Omeprazole', 'dosage': '20mg once daily', 'purpose': 'Reduce acid production'},
                    {'name': 'Antacid', 'dosage': 'As needed', 'purpose': 'Immediate acid relief'},
                    {'name': 'Sucralfate', 'dosage': '1g four times daily', 'purpose': 'Stomach lining protection'}
                ],
                'diet': [
                    {'item': 'Plain yogurt', 'benefit': 'Probiotic support'},
                    {'item': 'Bananas', 'benefit': 'Easy to digest, soothes stomach'},
                    {'item': 'Rice', 'benefit': 'Gentle on stomach'},
                    {'item': 'Lean proteins', 'benefit': 'Non-irritating protein source'},
                    {'item': 'Cooked vegetables', 'benefit': 'Easy to digest nutrients'}
                ],
                'exercises': [
                    {'name': 'Walking', 'duration': '15-20 minutes', 'benefit': 'Aids digestion'},
                    {'name': 'Gentle yoga', 'duration': '10-15 minutes', 'benefit': 'Reduces stress'},
                    {'name': 'Deep breathing', 'duration': '5-10 minutes', 'benefit': 'Stress relief'}
                ],
                'lifestyle': [
                    'Eat smaller, frequent meals',
                    'Avoid spicy and acidic foods',
                    'No alcohol or smoking',
                    'Practice stress management'
                ]
            },
            'Dengue': {
                'medicines': [
                    {'name': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever and pain relief'},
                    {'name': 'ORS', 'dosage': 'As needed', 'purpose': 'Maintain hydration'},
                    {'name': 'Avoid NSAIDs', 'dosage': 'N/A', 'purpose': 'Risk of bleeding'}
                ],
                'diet': [
                    {'item': 'Papaya leaf juice', 'benefit': 'Increases platelet count'},
                    {'item': 'Coconut water', 'benefit': 'Natural electrolytes'},
                    {'item': 'Fresh fruit juices', 'benefit': 'Vitamin C and hydration'},
                    {'item': 'Light soups', 'benefit': 'Easy to digest nutrients'},
                    {'item': 'ORS drinks', 'benefit': 'Maintain electrolyte balance'}
                ],
                'exercises': [
                    {'name': 'Complete bed rest', 'duration': 'During fever', 'benefit': 'Conserve energy'},
                    {'name': 'Gentle movements', 'duration': 'When recovering', 'benefit': 'Prevent muscle weakness'},
                    {'name': 'Light stretching', 'duration': '5-10 minutes', 'benefit': 'Maintain flexibility'}
                ],
                'lifestyle': [
                    'Regular temperature monitoring',
                    'Use mosquito protection',
                    'Stay hydrated',
                    'Regular blood tests as advised'
                ]
            },
            'Typhoid': {
                'medicines': [
                    {'name': 'Antibiotics', 'dosage': 'As prescribed', 'purpose': 'Treat infection'},
                    {'name': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever control'},
                    {'name': 'ORS', 'dosage': 'As needed', 'purpose': 'Maintain hydration'}
                ],
                'diet': [
                    {'item': 'Soft cooked rice', 'benefit': 'Easy to digest'},
                    {'item': 'Clear broths', 'benefit': 'Hydration and nutrients'},
                    {'item': 'Boiled vegetables', 'benefit': 'Soft and nutritious'},
                    {'item': 'Banana', 'benefit': 'Easy to digest, energy source'},
                    {'item': 'Yogurt', 'benefit': 'Probiotic support'}
                ],
                'exercises': [
                    {'name': 'Bed rest', 'duration': 'Initial phase', 'benefit': 'Recovery'},
                    {'name': 'Gentle walking', 'duration': 'When fever subsides', 'benefit': 'Maintain strength'},
                    {'name': 'Light stretching', 'duration': '5-10 minutes', 'benefit': 'Prevent stiffness'}
                ],
                'lifestyle': [
                    'Complete antibiotic course',
                    'Maintain strict hygiene',
                    'Regular temperature checks',
                    'Avoid solid foods initially'
                ]
            },
            'Malaria': {
                'medicines': [
                    {'name': 'Antimalarial drugs', 'dosage': 'As prescribed', 'purpose': 'Treat infection'},
                    {'name': 'Paracetamol', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever and pain'},
                    {'name': 'Iron supplements', 'dosage': 'As directed', 'purpose': 'Treat anemia'}
                ],
                'diet': [
                    {'item': 'High-protein foods', 'benefit': 'Support recovery'},
                    {'item': 'Iron-rich foods', 'benefit': 'Combat anemia'},
                    {'item': 'Fresh fruits', 'benefit': 'Vitamin C and minerals'},
                    {'item': 'Clear liquids', 'benefit': 'Stay hydrated'},
                    {'item': 'Light meals', 'benefit': 'Easy digestion'}
                ],
                'exercises': [
                    {'name': 'Complete rest', 'duration': 'During fever', 'benefit': 'Recovery'},
                    {'name': 'Light walking', 'duration': 'When improving', 'benefit': 'Maintain strength'},
                    {'name': 'Gentle stretching', 'duration': '5-10 minutes', 'benefit': 'Prevent stiffness'}
                ],
                'lifestyle': [
                    'Use mosquito nets',
                    'Complete medication course',
                    'Regular blood tests',
                    'Stay in cool environment'
                ]
            },
            'Migraine': {
                'medicines': [
                    {'name': 'Sumatriptan', 'dosage': '50mg as needed', 'purpose': 'Acute treatment'},
                    {'name': 'Ibuprofen', 'dosage': '400mg as needed', 'purpose': 'Pain relief'},
                    {'name': 'Anti-nausea medication', 'dosage': 'As prescribed', 'purpose': 'Nausea relief'}
                ],
                'diet': [
                    {'item': 'Water', 'benefit': 'Prevent dehydration'},
                    {'item': 'Magnesium-rich foods', 'benefit': 'May reduce frequency'},
                    {'item': 'Ginger tea', 'benefit': 'Natural anti-inflammatory'},
                    {'item': 'Small, frequent meals', 'benefit': 'Maintain blood sugar'},
                    {'item': 'Avoid trigger foods', 'benefit': 'Prevent attacks'}
                ],
                'exercises': [
                    {'name': 'Rest in dark room', 'duration': 'During attack', 'benefit': 'Reduce stimuli'},
                    {'name': 'Neck stretches', 'duration': '5-10 minutes', 'benefit': 'Relieve tension'},
                    {'name': 'Deep breathing', 'duration': '10 minutes', 'benefit': 'Stress relief'}
                ],
                'lifestyle': [
                    'Identify and avoid triggers',
                    'Maintain regular sleep schedule',
                    'Manage stress levels',
                    'Keep a migraine diary'
                ]
            },
            'Asthma': {
                'medicines': [
                    {'name': 'Salbutamol inhaler', 'dosage': '2 puffs as needed', 'purpose': 'Quick relief'},
                    {'name': 'Corticosteroid inhaler', 'dosage': 'As prescribed', 'purpose': 'Long-term control'},
                    {'name': 'Spacer device', 'dosage': 'Use with inhaler', 'purpose': 'Improve delivery'}
                ],
                'diet': [
                    {'item': 'Vitamin D rich foods', 'benefit': 'Reduce inflammation'},
                    {'item': 'Omega-3 rich foods', 'benefit': 'Anti-inflammatory'},
                    {'item': 'Fresh fruits', 'benefit': 'Antioxidants'},
                    {'item': 'Ginger', 'benefit': 'Natural anti-inflammatory'},
                    {'item': 'Turmeric', 'benefit': 'Reduce inflammation'}
                ],
                'exercises': [
                    {'name': 'Breathing exercises', 'duration': '10-15 minutes', 'benefit': 'Improve lung function'},
                    {'name': 'Swimming', 'duration': '20-30 minutes', 'benefit': 'Build lung capacity'},
                    {'name': 'Walking', 'duration': '30 minutes', 'benefit': 'General fitness'}
                ],
                'lifestyle': [
                    'Avoid triggers (dust, smoke)',
                    'Keep indoor air clean',
                    'Use air purifier if needed',
                    'Regular peak flow monitoring'
                ]
            }
        }
        
        # Age-specific dosage adjustments
        self.age_adjustments = {
            'child': {
                'dosage_factor': 0.5,
                'special_instructions': 'Consult pediatrician for exact dosing'
            },
            'elderly': {
                'dosage_factor': 0.75,
                'special_instructions': 'Monitor for side effects closely'
            }
        }
        
        # Load disease prediction model data
        self.load_model_data()

    def load_model_data(self):
        """Load model data with graceful error handling"""
        try:
            # Get the parent directory path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            
            # Try to load disease data
            disease_data_path = os.path.join(parent_dir, "data/disease_data.csv")
            if os.path.exists(disease_data_path):
                self.disease_data = pd.read_csv(disease_data_path)
            else:
                print(f"Warning: {disease_data_path} not found. Using default recommendations.")
                self.disease_data = None
            
            # Try to load medicine data
            medicine_data_path = os.path.join(parent_dir, "data/medicine_data.csv")
            if os.path.exists(medicine_data_path):
                self.medicine_data = pd.read_csv(medicine_data_path)
            else:
                print(f"Warning: {medicine_data_path} not found. Using default recommendations.")
                self.medicine_data = None
                
            # Try to load precaution data
            precaution_path = os.path.join(parent_dir, "data/Disease precaution.csv")
            if os.path.exists(precaution_path):
                self.precaution_data = pd.read_csv(precaution_path)
            else:
                print(f"Warning: {precaution_path} not found. Using default precautions.")
                self.precaution_data = None
                
            return True
        except Exception as e:
            print(f"Warning: Error loading model data: {str(e)}. Using default recommendations.")
            return False

    def get_age_group(self, age):
        """Determine age group for dosage adjustments"""
        if age < 12:
            return 'child'
        elif age > 65:
            return 'elderly'
        return 'adult'

    def adjust_dosage(self, medicine, age):
        """Adjust medicine dosage based on age"""
        age_group = self.get_age_group(age)
        if age_group in self.age_adjustments:
            adj = self.age_adjustments[age_group]
            if 'mg' in medicine['dosage']:
                try:
                    base_dose = int(''.join(filter(str.isdigit, medicine['dosage'].split('-')[0])))
                    adjusted_dose = int(base_dose * adj['dosage_factor'])
                    medicine['dosage'] = f"{adjusted_dose}mg {adj['special_instructions']}"
                except:
                    medicine['dosage'] += f" ({adj['special_instructions']})"
        return medicine

    def get_recommendations(self, disease, age=None, gender=None, confidence_score=None):
        """Get integrated recommendations for a disease"""
        if disease not in self.disease_recommendations:
            # Provide general recommendations for unknown diseases
            return {
                'medicines': [
                    {'medicine': 'Consult doctor', 'dosage': 'As prescribed', 'purpose': 'Proper diagnosis and treatment'}
                ],
                'diet': [
                    'Balanced diet - Support overall health',
                    'Stay hydrated - Essential for recovery',
                    'Fresh fruits and vegetables - Boost immunity',
                    'Protein-rich foods - Support healing',
                    'Avoid processed foods - Reduce inflammation'
                ],
                'exercises': [
                    'Rest - Allow body to heal',
                    'Light walking - Maintain mobility',
                    'Deep breathing - Reduce stress'
                ],
                'lifestyle': [
                    'Get adequate rest',
                    'Maintain good hygiene',
                    'Avoid stress',
                    'Seek medical attention if symptoms worsen'
                ],
                'warning': 'These are general recommendations. Please consult a healthcare provider for specific advice.'
            }

        recs = self.disease_recommendations[disease]
        result = {
            'medicines': [],
            'diet': [f"{item['item']} - {item['benefit']}" for item in recs['diet']],
            'exercises': [f"{ex['name']} ({ex['duration']}) - {ex['benefit']}" for ex in recs['exercises']],
            'lifestyle': recs.get('lifestyle', [])
        }

        # Adjust medicine dosages based on age
        if age is not None:
            result['medicines'] = [
                {
                    'medicine': med['name'],
                    'dosage': self.adjust_dosage(med.copy(), age)['dosage'],
                    'purpose': med['purpose']
                }
                for med in recs['medicines']
            ]
        else:
            result['medicines'] = [
                {
                    'medicine': med['name'],
                    'dosage': med['dosage'],
                    'purpose': med['purpose']
                }
                for med in recs['medicines']
            ]

        # Add confidence-based warnings if confidence score is low
        if confidence_score and confidence_score < 0.7:
            result['warning'] = "These recommendations are based on preliminary assessment. Please consult a healthcare provider for confirmation."

        return result

    def save_model(self):
        """Save the integrated recommender model"""
        try:
            joblib.dump(self, 'models/integrated_recommender.pkl')
            print("Successfully saved integrated recommender model")
            return True
        except Exception as e:
            print(f"Error saving model: {e}")
            return False

    @classmethod
    def load_model(cls):
        """Create and load a new model instance with error handling"""
        model = cls()
        model.load_model_data()  # Even if this fails, we have default recommendations
        return model

# Create and save a singleton instance
recommender = IntegratedRecommender()
recommender.save_model() 