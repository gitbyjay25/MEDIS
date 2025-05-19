import pandas as pd
import os

# Define paths
data_folder = "data/"
file1 = os.path.join(data_folder, "DiseaseAndSymptoms.csv")
file2 = os.path.join(data_folder, "Disease precaution.csv")

# Check if files exist
if not os.path.exists(file1):
    print(f"❌ ERROR: {file1} not found!")
if not os.path.exists(file2):
    print(f"❌ ERROR: {file2} not found!")

# Load datasets
df_symptoms = pd.read_csv(file1)
df_precautions = pd.read_csv(file2)

# Display first few rows
print("\n🔹 Disease and Symptoms Dataset:")
print(df_symptoms.head())

print("\n🔹 Disease and Precaution Dataset:")
print(df_precautions.head())
