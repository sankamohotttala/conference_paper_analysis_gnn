import os
import pandas as pd

root_folder = r'F:\Codes\joint attention\Nano-particle\2024_ICARC_Tute'

reference_columns = None
all_same = True  
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith('.csv'):  
            file_path = os.path.join(foldername, filename)
            
            try:
                df = pd.read_csv(file_path)
                print(f"Loaded: {file_path}")
                
                current_columns = set(df.columns)
                print(f"Columns: {current_columns}")
                
                if reference_columns is None:
                    reference_columns = current_columns
                elif reference_columns != current_columns:
                    all_same = False
                    print(f"Column mismatch in file: {file_path}")
            
            except Exception as e:
                print(f"Error loading file {file_path}: {e}")

if all_same:
    print("All CSV files have the same columns.")
else:
    print("Not all CSV files have the same columns.")
