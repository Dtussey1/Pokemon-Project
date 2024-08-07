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


4. **Run the project:**
    ```sh
    python Pokemon_Project.py
    ```

## Notes

- Ensure you have Python installed.
- The `requirements.txt` file includes all necessary packages. If you encounter any issues, make sure your Python environment is up to date.


## Acknowledgements

- Pokémon Images and Types dataset provided by [Vishal Subbiah on Kaggle](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types).
- Pokémon dataset provided by [Rounak Banik on Kaggle](https://www.kaggle.com/datasets/rounakbanik/pokemon).