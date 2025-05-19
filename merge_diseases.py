import pandas as pd  # Import pandas

# Load datasets
df_symptoms = pd.read_csv("data/symptoms.csv")
df_precaution = pd.read_csv("data/precaution.csv")

# Ensure column names match
df_precaution.rename(columns=lambda x: x.strip(), inplace=True)  # Remove extra spaces

# Merge
df_merged = pd.merge(df_symptoms, df_precaution, on="Disease", how="left")

# Fill missing precaution values with "Not Available"
df_merged.fillna("Not Available", inplace=True)

# Save+
df_merged.to_csv("data/diseases.csv", index=False)

print(" Fixed merge issue. Check diseases.csv")
