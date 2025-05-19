import pandas as pd

# Load datasets
df_existing = pd.read_csv("data/DiseaseAndSymptoms.csv")
df_new = pd.read_csv("data/new_diseases.csv")

# Concatenate the datasets
df_merged = pd.concat([df_existing, df_new], ignore_index=True)

# Save the merged dataset
df_merged.to_csv("data/DiseaseAndSymptoms.csv", index=False)

print("✅ Successfully merged new diseases into the dataset!")

# Now update the precautions file
df_precautions = pd.read_csv("data/Disease precaution.csv")

# Add new disease precautions if they don't exist
new_precautions = pd.DataFrame({
    'Disease': ['Heart attack'],
    'Precaution_1': ['call ambulance'],
    'Precaution_2': ['chew or swallow asprin'],
    'Precaution_3': ['keep calm'],
    'Precaution_4': ['rest']
})

df_precautions = pd.concat([df_precautions, new_precautions], ignore_index=True)
df_precautions.to_csv("data/Disease precaution.csv", index=False)

print("✅ Successfully updated disease precautions!") 