import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Load the data from CSV files
df1 = pd.read_csv(r"C:\Users\Dtussey\OneDrive\Pokemon Project\pokemon.csv")
df2 = pd.read_csv(r"C:\Users\Dtussey\OneDrive\Pokemon Project\pokemon file 2.csv")

# Rename 'type1' in df2 to 'Type1'
df2 = df2.rename(columns={'type1': 'Type1'})

# Perform a right join 
merged_df = pd.merge(df2[['Type1', 'generation', 'is_legendary']], df1, on='Type1', how='left')

# Check if the merged dataframe is not empty
if merged_df.empty:
    raise ValueError("The merged dataframe is empty. Please check your data files and merge conditions.")

# Print some information about the merged dataframe
print("Merged DataFrame Info:")
print(merged_df.info())
print("Merged DataFrame Head:")
print(merged_df.head())

# Create a color map for Pokémon types with distinct hexadecimal colors
type_colors = {
    'grass': '#4CAF50', 'water': '#2196F3', 'fire': '#F44336', 'electric': '#FFEB3B',
    'psychic': '#9C27B0', 'ice': '#00BCD4', 'dragon': '#FF9800', 'dark': '#212121',
    'fairy': '#E91E63', 'fighting': '#795548', 'flying': '#03A9F4', 'poison': '#8E24AA',
    'ground': '#8B4513', 'rock': '#9E9E9E', 'bug': '#ADFF2F', 'steel': '#A9A9A9',
    'normal': '#C0C0C0', 'ghost': '#8A2BE2'
}
