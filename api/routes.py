import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

# Load the cleaned dataset
dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "cleaned_diseases.csv"))
df = pd.read_csv(dataset_path)

# Ensure "Disease" column exists
if "Disease" not in df.columns:
    raise ValueError("🚨 Column 'Disease' is missing from dataset!")

# Identify numeric columns only
X = df.drop(columns=["Disease"])  
y = df["Disease"]

# Convert categorical columns to numerical using one-hot encoding (if necessary)
X = pd.get_dummies(X)

# Check for non-numeric values
if X.select_dtypes(include=["object"]).shape[1] > 0:
    raise ValueError("🚨 Non-numeric values found in features! Ensure all symptoms are properly encoded.")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models", "disease_prediction_model.pkl"))
joblib.dump(model, model_path)

print(f"✅ Model trained and saved at: {model_path}")
