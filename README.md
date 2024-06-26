# Movie Recommender System

## Overview

This repository contains the implementation of a Movie Recommender System using the TMDB 5000 Movie Dataset. The project consists of two main components:
1. **Data Preprocessing and Model Creation:** This includes data preprocessing, feature extraction, and the creation of a movie recommendation model.
2. **Streamlit Web App:** A web application built with Streamlit to provide an interactive interface for recommending movies.

## Table of Contents
- [Movie Recommender System](#movie-recommender-system)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Setup Instructions](#setup-instructions)
  - [Usage](#usage)
    - [Main Code](#main-code)
    - [Streamlit App](#streamlit-app)
  - [Acknowledgements](#acknowledgements)
  - [License](#license)

## Setup Instructions

1. **Clone the Repository:**
    git clone https://github.com/yourusername/movie-recommender-system.git
    cd movie-recommender-system


2. **Install Required Packages:**
    Install the necessary Python packages using `pip`:
    pip install -r requirements.txt


3. **Download the Datasets:**
    Ensure the `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` files are present in the project directory. You can download them from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

## Usage

### Main Code

The main code is located in the `Recommender.ipynb` Jupyter notebook. This notebook demonstrates the entire process of building the movie recommender system, including data preprocessing, feature extraction, and model creation.

1. **Run the Jupyter Notebook:**
    jupyter notebook Recommender.ipynb


2. **Follow the Steps:**
    Open the notebook and run each cell sequentially. The notebook includes detailed markdown explanations for each step.

### Streamlit App

The Streamlit app provides an interactive web interface for recommending movies. The app uses the preprocessed data and the recommendation model created in the Jupyter notebook.

1. **Run the Streamlit App:**
    ```sh
    streamlit run app.py
    ```

2. **Interact with the App:**
    - Select a movie from the dropdown menu.
    - Click the "Recommend" button to see the recommended movies along with their posters.

## Acknowledgements

- The TMDB 5000 Movie Dataset is provided by [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
