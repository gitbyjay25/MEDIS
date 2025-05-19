import pandas as pd
import os
import joblib  # ✅ for saving the symptom columns

# Directory where the script is located
current_folder = os.path.dirname(__file__)

# Correct path to the "data" folder (no extra "data" folder in the path)
data_folder = current_folder  # Both script and data are in the same folder

# Check if the data folder exists
if not os.path.exists(data_folder):
    print(f"❌ The 'data' folder does not exist at the expected location: {data_folder}")
else:
    # Loop through all files in the "data" folder
    for file in os.listdir(data_folder):
        if file.endswith(".csv"):  # Only process CSV files
            # Read the CSV file
            df = pd.read_csv(os.path.join(data_folder, file))  # Correct path here
            print(f"File: {file}, Shape: {df.shape}")

            # Check for the specific file name and process it
            if file == "cleaned_diseases.csv":  # Adjust this based on your actual file name
                # Extract symptom columns (remove 'Disease' and 'Disease_Encoded')
                symptom_columns = df.drop(columns=["Disease", "Disease_Encoded"]).columns.tolist()

                # Save the symptom columns to a file
                if not os.path.exists("models"):
                    os.makedirs("models")
                joblib.dump(symptom_columns, "models/symptom_columns.pkl")

                print("✅ Symptom columns saved successfully!")
