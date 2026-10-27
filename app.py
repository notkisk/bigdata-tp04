import os
import pandas as pd

data_dir = "/app/data"
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

if not csv_files:
    print("No CSV dataset found in /app/data")
else:
    for file in csv_files:
        df = pd.read_csv(os.path.join(data_dir, file))
        print(f"\nDataset: {file}")
        print(df.head())
        print(f"Shape: {df.shape}")
