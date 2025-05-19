import pandas as pd

# Load dataset
df = pd.read_csv("data/DiseaseAndSymptoms.csv")

# Extract symptoms columns
symptom_columns = [col for col in df.columns if "Symptom" in col]
df_symptoms = df[["Disease"] + symptom_columns]

# Save to CSV
df_symptoms.to_csv("data/symptoms.csv", index=False)

print("✅ Symptoms extracted and saved to symptoms.csv")
