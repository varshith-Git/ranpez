# scripts/validate.py

import pandas as pd

def validate_file(file_path, file_type):
    try:
        if file_type == 'csv':
            pd.read_csv(file_path)
        elif file_type == 'json':
            pd.read_json(file_path)
        elif file_type == 'parquet':
            pd.read_parquet(file_path)
        elif file_type == 'excel':
            pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type.")
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False
