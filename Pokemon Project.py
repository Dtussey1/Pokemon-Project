import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Dtussey\OneDrive\Pokemon Project\archive\Pokemon.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Define custom colors for Pokémon types
type_colors = {
    'Bug': '#A8B820',
    'Dark': '#705848',
    'Dragon': '#7038F8',
    'Electric': '#F8D030',
    'Fairy': '#EE99AC',
    'Fighting': '#C03028',
    'Fire': '#F08030',
    'Flying': '#A890F0',
    'Ghost': '#705898',
    'Grass': '#78C850',
    'Ground': '#E0C068',
    'Ice': '#98D8D8',
    'Normal': '#A8A878',
    'Poison': '#A040A0',
    'Psychic': '#F85888',
    'Rock': '#B8A038',
    'Steel': '#B8B8D0',
    'Water': '#6890F0'
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

