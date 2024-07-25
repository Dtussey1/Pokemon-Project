import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Dtussey\OneDrive\Pokemon Project\archive\Pokemon.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())
