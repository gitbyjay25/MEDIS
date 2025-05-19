import pandas as pd

# Load the dataset
file_path = "data/cleaned_diseases.csv"  # Update if needed
df = pd.read_csv(file_path)

# Find all columns related to precautions dynamically
precaution_cols = [col for col in df.columns if "Precaution" in col]

if not precaution_cols:
    print("No precaution columns found in the dataset.")
else:
    print(f"Found {len(precaution_cols)} precaution columns: {precaution_cols}")

# Checking the data type of each precaution column
for col in precaution_cols:
    print(f"Checking column: {col}")
    if df[col].dtype in ["int64", "float64"]:
        print(f"✅ {col} is numerical.")
    else:
        print(f"⚠️ {col} is NOT numerical. Found type: {df[col].dtype}")

# Display the first few rows for verification
print("\nSample Data:")
print(df[precaution_cols].head())

