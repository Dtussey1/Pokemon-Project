# Pokémon Project

## Overview

This project uses Pokémon data to create visualization tools to interpret the data. The project will read two CSV files, clean the data and perform a pandas merge, and plot three graphs using matplotlib. My goal with this project is to make the data contained within the two files provided more readable to the user. This will be accomplished by creating various graphs showing some points of interest within the datsets in a visually pleasing and informative manner. I intend to show the user the distribution of Pokemon types and occurrence of legendary Pokemon across the generations that this data covers.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Dtussey1/Pokemon-Project.git
    cd Pokemon-Project
    ```

2. **Set up a virtual environment (optional but recommended):**
    - **For Windows:**
      ```sh
      python -m venv venv
      venv\Scripts\activate
      ```
    - **For macOS/Linux:**
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the required CSV files:**
    - **Download from OneDrive:**
      - [pokemon.csv](https://1drv.ms/x/c/2dee6ebdd0760e9f/EVYH_auH5hRJuG3O1rludYABE_OPZP30XbWZGr5cgUd4bA?e=VbGujS)
      - [pokemon_file_2.csv](https://1drv.ms/x/c/2dee6ebdd0760e9f/EQQqBTYF1e1Io5lun2vvHG0BBrj3gcGhzWr1EOEGOcpfSA?e=BRCIzS)

    - Place the downloaded files in the project directory (the same directory as `Pokemon_Project.py`).

5. **Run the project:**
    ```sh
    python Pokemon_Project.py
    ```

## Notes

- Ensure you have Python installed.
- The `requirements.txt` file includes all necessary packages. If you encounter any issues, make sure your Python environment is up to date.
- The CSV files should be placed in the project directory where `Pokemon_Project.py` is located.


## Acknowledgements

- Pokémon Images and Types dataset provided by [Vishal Subbiah on Kaggle](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types).
- Pokémon dataset provided by [Rounak Banik on Kaggle](https://www.kaggle.com/datasets/rounakbanik/pokemon).