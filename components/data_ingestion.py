import pandas as pd

# Load datasets
symptoms_data = pd.read_csv("data/DiseaseAndSymptoms.csv")  # Disease to Symptoms Mapping
precaution_data = pd.read_csv("data/Disease precaution.csv")  # Disease to Precautions Mapping

# Print first few rows to verify
print("Symptoms Dataset:")
print(symptoms_data.head())

print("\nPrecaution Dataset:")
print(precaution_data.head())
