import pandas as pd

# Load dataset
df = pd.read_csv("data/Disease precaution.csv")

# Save directly
df.to_csv("data/precaution.csv", index=False)

print("✅ Precautions extracted and saved to precaution.csv")
