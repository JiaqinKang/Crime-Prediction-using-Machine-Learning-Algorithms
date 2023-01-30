import os
import glob
import pandas as pd

path = 'dataset' # Change this to the directory where your CSV files are located

if os.path.exists(path):
    print("path exists")
else:
    print("path does not exist")
all_files = glob.glob(os.path.join(path, "*.csv"))

df_merged = pd.concat((pd.read_csv(f) for f in all_files))

df_merged.to_csv('merged.csv', index=False)