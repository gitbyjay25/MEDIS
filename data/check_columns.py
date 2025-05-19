import pandas as pd
import os

data_folder = "C:/Users/jagdi/Desktop/Head/Projects/AI ML/src/MEDIS/data"

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)
        try:
            df = pd.read_csv(file_path)
            print(f"\n📂 {file}:")
            print(df.columns.tolist())  # Print column names
        except Exception as e:
            print(f"Error reading {file}: {e}")
