This application will utilize two CSV files for the requirements of the capstone project.

# Pokemon data visualization tool


## Setup

1. **Clone the repository:**


2. **Download the required CSV files from Kaggle:**
    - Go to the [Kaggle Dataset Page](https://www.kaggle.com/dataset-page-url)
    - Download https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types and https://www.kaggle.com/datasets/rounakbanik/pokemon

3. **Place the downloaded files in the `data` directory:**
    ```sh
    mkdir data
    mv /path/to/downloaded/file1.csv data/file1.csv
    mv /path/to/downloaded/file2.csv data/file2.csv
    ```

4. **Install dependencies:**
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


5. **Run the project:**
    ```sh
    Pokemon Project.py
    ```

## Notes

- Ensure you have Python installed.
- Follow any additional setup instructions specific to your project.

## Acknowledgements

- Datasets provided by https://www.kaggle.com/rounakbanik and https://www.kaggle.com/vishalsubbiah on Kaggle.
