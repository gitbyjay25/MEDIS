import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import re

class DataPreprocessing:
    def __init__(self, disease_file):
        self.df = pd.read_csv(disease_file)
        # Remove duplicate rows
        self.df = self.df.drop_duplicates()
        
        # Enhanced symptom synonyms mapping
        self.symptom_mapping = {
            # Breathing related
            'shortness of breath': 'breathlessness',
            'breathlessness': 'breathlessness',
            'trouble breathing': 'breathlessness',
            'difficulty breathing': 'breathlessness',
            'labored breathing': 'breathlessness',
            'respiratory distress': 'breathlessness',
            
            # Chest related
            'chest pain': 'chest_pain',
            'chest discomfort': 'chest_pain',
            'chest tightness': 'chest_pain',
            'angina': 'chest_pain',
            
            # Temperature related
            'fever': 'high_fever',
            'high fever': 'high_fever',
            'elevated temperature': 'high_fever',
            'low grade fever': 'mild_fever',
            
            # Respiratory
            'coughing': 'cough',
            'dry cough': 'cough',
            'wet cough': 'productive_cough',
            'mucus cough': 'productive_cough',
            
            # Fatigue related
            'tired': 'fatigue',
            'exhaustion': 'fatigue',
            'feeling tired': 'fatigue',
            'weakness': 'fatigue',
            'lethargy': 'fatigue',
            
            # Pain related
            'headache': 'head_pain',
            'head pain': 'head_pain',
            'migraine': 'severe_headache',
            'stomach pain': 'abdominal_pain',
            'abdominal pain': 'abdominal_pain',
            'belly pain': 'abdominal_pain',
            
            # Digestive
            'nausea': 'nausea',
            'vomiting': 'vomiting',
            'throwing up': 'vomiting',
            'diarrhea': 'loose_stools',
            'loose stools': 'loose_stools',
            
            # Skin related
            'rash': 'skin_rash',
            'skin rash': 'skin_rash',
            'itching': 'itching',
            'pruritus': 'itching',
            'yellowing': 'yellowish_skin',
            'jaundice': 'yellowish_skin'
        }
        
        # Key symptoms that should be present for specific diseases
        self.required_symptoms = {
            'Heart Attack': ['chest_pain', 'breathlessness'],
            'Asthma': ['breathlessness', 'wheezing'],
            'Pneumonia': ['cough', 'high_fever', 'breathlessness'],
            'Diabetes': ['frequent_urination', 'excessive_thirst'],
            'Hypertension': ['headache', 'dizziness'],
            'Migraine': ['severe_headache', 'light_sensitivity'],
            'Bronchitis': ['cough', 'chest_pain'],
            'UTI': ['frequent_urination', 'burning_urination'],
            'Gastritis': ['abdominal_pain', 'nausea'],
            'Hepatitis': ['yellowish_skin', 'abdominal_pain']
        }

    def standardize_symptoms(self, symptom):
        """Standardize symptom names using the mapping"""
        if pd.isna(symptom) or symptom == "":
            return ""
        
        # Convert to lowercase and remove special characters
        symptom = re.sub(r'[^a-zA-Z\s]', '', str(symptom).lower().strip())
        
        # Check direct mapping
        if symptom in self.symptom_mapping:
            return self.symptom_mapping[symptom]
        
        # Convert spaces to underscores for consistency
        symptom = re.sub(r'\s+', '_', symptom)
        
        return symptom

    def validate_disease_symptoms(self):
        """Ensure each disease has its required symptoms"""
        symptom_cols = [col for col in self.df.columns if "Symptom" in col]
        
        for disease, required_symptoms in self.required_symptoms.items():
            disease_rows = self.df[self.df['Disease'] == disease]
            for row_idx in disease_rows.index:
                row_symptoms = set()
                for col in symptom_cols:
                    symptom = self.standardize_symptoms(self.df.at[row_idx, col])
                    if symptom:
                        row_symptoms.add(symptom)
                
                # Add missing required symptoms
                missing_symptoms = set(required_symptoms) - row_symptoms
                if missing_symptoms:
                    empty_cols = [col for col in symptom_cols if pd.isna(self.df.at[row_idx, col]) or self.df.at[row_idx, col] == ""]
                    for symptom, col in zip(missing_symptoms, empty_cols[:len(missing_symptoms)]):
                        self.df.at[row_idx, col] = symptom

    def handle_missing_values(self):
        """Handle missing values with improved strategies"""
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # For categorical columns, use mode instead of empty string
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0] if not self.df[col].mode().empty else "")
            else:
                # For numerical columns, use median instead of mean to handle outliers better
                self.df[col] = self.df[col].fillna(self.df[col].median())

    def encode_symptoms(self):
        """Encode symptoms with improved validation and standardization"""
        symptom_cols = [col for col in self.df.columns if "Symptom" in col]
        
        # First pass: standardize all symptoms
        for col in symptom_cols:
            self.df[col] = self.df[col].apply(self.standardize_symptoms)
        
        # Validate required symptoms for each disease
        self.validate_disease_symptoms()
        
        # Get all unique valid symptoms
        all_symptoms = set()
        for col in symptom_cols:
            all_symptoms.update(self.df[col].unique())
        all_symptoms.discard("")  # Remove empty string
        
        # Create a new DataFrame for symptoms with improved structure
        symptom_df = pd.DataFrame(0, index=self.df.index, columns=sorted(list(all_symptoms)))
        
        # Set 1 for present symptoms with validation
        for col in symptom_cols:
            for symptom in all_symptoms:
                mask = self.df[col] == symptom
                if mask.any():
                    symptom_df.loc[mask, symptom] = 1
        
        # Add severity indicators for certain symptoms
        severity_indicators = {
            'high_fever': ['fever', 'very_high_fever'],
            'severe_headache': ['headache', 'migraine'],
            'chest_pain': ['mild_chest_pain', 'severe_chest_pain']
        }
        
        for base_symptom, indicators in severity_indicators.items():
            if base_symptom in symptom_df.columns:
                for indicator in indicators:
                    if indicator not in symptom_df.columns:
                        symptom_df[indicator] = 0
                        # Set severity indicators based on co-occurring symptoms
                        symptom_df.loc[symptom_df[base_symptom] == 1, indicator] = 1
        
        # Save symptom mapping and metadata
        os.makedirs("models", exist_ok=True)
        joblib.dump(self.symptom_mapping, "models/symptom_mapping.pkl")
        joblib.dump(list(symptom_df.columns), "models/symptom_columns.pkl")
        
        # Drop the original symptom columns and add the new ones
        self.df = self.df.drop(columns=symptom_cols)
        self.df = pd.concat([self.df, symptom_df], axis=1)

    def encode_target(self):
        """Encode disease labels with validation"""
        if "Disease" in self.df.columns:
            # Clean disease names
            self.df["Disease"] = self.df["Disease"].apply(lambda x: str(x).strip().title())
            
            # Validate against required symptoms
            for disease in self.required_symptoms.keys():
                if disease not in self.df["Disease"].unique():
                    print(f"Warning: Disease '{disease}' from required_symptoms not found in dataset")
            
            self.label_encoder = LabelEncoder()
            self.df["Disease_Encoded"] = self.label_encoder.fit_transform(self.df["Disease"])
            
            # Save label encoder and disease metadata
            os.makedirs("models", exist_ok=True)
            joblib.dump(self.label_encoder, "models/label_encoder.pkl")
            
            # Save disease-symptom relationships
            disease_symptom_map = {}
            for disease in self.df["Disease"].unique():
                disease_rows = self.df[self.df["Disease"] == disease]
                # Convert to numeric columns only for symptom analysis
                numeric_cols = disease_rows.drop(columns=["Disease", "Disease_Encoded"]).select_dtypes(include=['int64', 'float64']).columns
                symptoms = disease_rows[numeric_cols].sum()
                common_symptoms = symptoms[symptoms > len(disease_rows) * 0.5].index.tolist()
                disease_symptom_map[disease] = common_symptoms
            
            joblib.dump(disease_symptom_map, "models/disease_symptom_map.pkl")

    def save_clean_data(self, output_file):
        """Save cleaned data with validation"""
        # Validate final dataset
        assert not self.df.isnull().any().any(), "Dataset contains null values"
        assert len(self.df) > 0, "Dataset is empty"
        assert "Disease" in self.df.columns, "Disease column is missing"
        assert "Disease_Encoded" in self.df.columns, "Disease_Encoded column is missing"
        
        # Save with index for traceability
        self.df.to_csv(output_file, index=True)
        print(f"✅ Saved cleaned dataset with {len(self.df)} rows and {len(self.df.columns)} columns")

if __name__ == "__main__":
    file_path = "data/diseases.csv"
    output_path = "data/cleaned_diseases.csv"

    processor = DataPreprocessing(file_path)
    processor.handle_missing_values()
    processor.encode_symptoms()
    processor.encode_target()
    processor.save_clean_data(output_path)

    print("✅ Data Preprocessing Completed!")
    print(f"Total diseases: {len(processor.df['Disease'].unique())}")
    print(f"Total unique symptoms: {len(processor.df.drop(columns=['Disease', 'Disease_Encoded']).columns)}")
