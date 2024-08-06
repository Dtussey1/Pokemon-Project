import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Dtussey\OneDrive\Pokemon Project\archive\Pokemon.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Define custom colors for Pokémon types
# Create a color map for Pokémon types with distinct hexadecimal colors
type_colors = {
    'grass': '#4CAF50', 'water': '#2196F3', 'fire': '#F44336', 'electric': '#FFEB3B',
    'psychic': '#9C27B0', 'ice': '#00BCD4', 'dragon': '#FF9800', 'dark': '#212121',
    'fairy': '#E91E63', 'fighting': '#795548', 'flying': '#03A9F4', 'poison': '#8E24AA',
    'ground': '#8B4513', 'rock': '#9E9E9E', 'bug': '#ADFF2F', 'steel': '#A9A9A9',
    'normal': '#C0C0C0', 'ghost': '#8A2BE2'
}

# Plot the count of Pokémon types
def plot_type_counts():
    
    type_counts = df['Type 1'].value_counts()
    colors = [type_colors[type_] for type_ in type_counts.index]
    fig, ax = plt.subplots()
    type_counts.plot(kind='bar', ax=ax, color=colors)
    ax.set_xlabel('Type 1')
    ax.set_ylabel('Count')
    ax.set_title('Count of Pokémon by Type')
    plt.tight_layout()  
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.15)  
    return fig

# Plot the frequency of Pokémon types across generations
def plot_type_generation_counts():
    
    type_generation_counts = df.groupby(['Generation', 'Type 1']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 8))
    type_colors_sorted = [type_colors[type_] for type_ in type_generation_counts.columns]
    type_generation_counts.plot(kind='bar', stacked=True, ax=ax, color=type_colors_sorted)
    ax.set_xlabel('Generation')
    ax.set_ylabel('Count')
    ax.set_title('Frequency of Pokémon Types Across Generations')
    ax.legend(title='Type 1', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()  
    fig.subplots_adjust(left=0.1, right=0.75, top=0.9, bottom=0.15)  
    return fig

