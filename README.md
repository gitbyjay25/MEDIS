# MEDIS - Medical Diagnosis Prediction System

## Overview
MEDIS is an advanced medical diagnosis prediction system that uses symptom analysis and machine learning to predict potential diseases. The system considers various factors including:
- Weighted symptom categorization
- Age-specific symptoms
- Seasonal factors
- Treatment recommendations
- Complication warnings
- Symptom duration tracking

## Features
- Disease prediction with confidence scoring
- Comprehensive disease profiles
- Age-specific symptom analysis
- Seasonal factor consideration
- Treatment recommendations
- Prevention guidelines
- Complication warnings

## Supported Diseases
- Malaria
- Dengue
- Chicken Pox
- COVID-19
- Typhoid
- Common Cold
- Tuberculosis
- Jaundice
- Gastritis
- Arthritis
- AIDS
- Skin Conditions (including Acne)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MEDIS.git
cd MEDIS
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the System
```python
from disease_prediction_v2 import predict_diseases, get_suggested_symptoms

# Example usage
symptoms = ["fever", "cough", "fatigue"]
age_group = "ADULT"  # Options: INFANT, CHILD, TEEN, ADULT, ELDERLY
season = "SUMMER"    # Options: SUMMER, WINTER, MONSOON, SPRING

predictions = predict_diseases(symptoms, age_group, season)
```

### Running Tests
```bash
python test_symptoms.py
```

## System Components

### 1. Symptom Categories
- Critical symptoms (Weight: 3.0)
- High priority symptoms (Weight: 2.0)
- Medium priority symptoms (Weight: 1.0)

### 2. Age Groups
- INFANT (0-2 years)
- CHILD (3-12 years)
- TEEN (13-19 years)
- ADULT (20-60 years)
- ELDERLY (60+ years)

### 3. Seasonal Factors
- SUMMER
- WINTER
- MONSOON
- SPRING

## API Reference

### predict_diseases(symptoms, age_group=None, season=None)
Returns predictions with confidence scores and recommendations.

### get_suggested_symptoms(current_symptoms, age_group=None)
Returns additional symptoms to check based on current symptoms.

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This system is designed to assist in preliminary diagnosis and should not replace professional medical advice. Always consult with healthcare professionals for proper medical diagnosis and treatment.