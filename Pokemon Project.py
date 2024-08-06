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

# Create the main window
root = tk.Tk()
root.title("Pokémon Data Visualization")

# Create a dropdown menu with adjusted width
selected_graph = tk.StringVar()
graph_options = [
    "Frequency of Pokémon Types",
    "Types of Pokémon per Generation",
    "Number of Legendary Pokémon per Generation"
]
selected_graph.set(graph_options[0])  # default value

dropdown = ttk.Combobox(root, textvariable=selected_graph, values=graph_options, width=40)
dropdown.pack(pady=10)

# Create a frame for the plot
plot_frame = tk.Frame(root)
plot_frame.pack(pady=10, fill=tk.BOTH, expand=True)

def plot_frequency_of_types():
    """Plot the frequency of Pokémon types."""
    if 'Type1' not in merged_df.columns or merged_df['Type1'].empty:
        print("Error: 'Type1' column is missing or empty.")
        return

    fig, ax = plt.subplots(figsize=(12, 8))  # Adjust size for better formatting
    type_counts = merged_df['Type1'].str.lower().value_counts()  # Convert to lowercase to match color map
    
    # Set colors based on Pokémon types
    colors = [type_colors.get(t, '#B0BEC5') for t in type_counts.index]  # Default to light gray if type not found
    
    bars = ax.bar(type_counts.index, type_counts.values, color=colors)
    ax.set_title('Frequency of Pokémon Types')
    ax.set_xlabel('Type')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

    # Add legend to the side
    handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
    labels = [t.capitalize() for t in type_counts.index]
    ax.legend(handles, labels, title='Type', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adjust layout to fit all elements
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
