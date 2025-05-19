# MEDIS - Medical Diagnosis Prediction System

## Project Structure
```
MEDIS/
├── frontend/                    # A's Work - Frontend Development
│   ├── templates/              # HTML templates
│   ├── static/                 # CSS, JS, images
│   ├── server.py              # Flask server
│   └── auth/                  # Authentication
│
├── backend/                    # B's Work - Backend Development
│   ├── api/                   # API endpoints
│   ├── routes/               # Route handlers
│   └── app.py                # Main backend app
│
├── ml/                        # J's Work - ML & Disease Prediction
│   ├── models/               # ML models
│   │   ├── disease_prediction_v2.py
│   │   ├── model_training.py
│   │   └── generate_models.py
│   ├── data/                 # Data processing
│   │   ├── data_ingestion.py
│   │   ├── datatransformation.py
│   │   ├── fix_dataset.py
│   │   └── extract_symptoms.py
│   └── tests/                # ML tests
│       ├── test_symptoms.py
│       ├── test_prediction.py
│       └── test_cases.py
│
├── recommendations/           # M's Work - Treatment Recommendations
│   ├── models/
│   │   ├── integrated_recommendation_model.py
│   │   └── medicine_recommendation.py
│   ├── data/
│   │   ├── merge_diseases.py
│   │   └── merge_new_diseases.py
│   └── tests/
│       └── test_recommendations.py
│
├── database/                  # Shared - Database
│   ├── models.py
│   ├── init_db.py
│   └── user_history.db
│
├── config/                    # Shared - Configuration
│   └── config.py
│
├── logs/                      # Shared - Logs
│   └── error.log
│
├── requirements.txt           # Shared - Dependencies
└── README.md                 # Shared - Documentation
```

## Team Responsibilities

### J - ML & Disease Prediction Expert
- Disease prediction model development
- ML model training and optimization
- Data processing and feature engineering
- Model testing and validation

### B - Backend Developer
- API development and maintenance
- Server configuration
- Database integration
- Request handling and validation

### A - Frontend Developer
- User interface design
- Frontend implementation
- User experience optimization
- Responsive design

### M - Data & Recommendations Specialist
- Treatment recommendation system
- Medicine and diet recommendations
- Data validation and cleaning
- Documentation

## Features
- Disease prediction with confidence scoring
- Comprehensive disease profiles
- Age-specific symptom analysis
- Seasonal factor consideration
- Treatment recommendations
- Prevention guidelines
- Complication warnings

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
from ml.models.disease_prediction_v2 import predict_diseases

# Example usage
symptoms = ["fever", "cough", "fatigue"]
age_group = "ADULT"  # Options: INFANT, CHILD, TEEN, ADULT, ELDERLY
season = "SUMMER"    # Options: SUMMER, WINTER, MONSOON, SPRING

predictions = predict_diseases(symptoms, age_group, season)
```

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