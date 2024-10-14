# food_delivery_time

# Food Delivery Time Prediction

This project is focused on predicting the delivery time of food orders using machine learning techniques. The goal is to provide users with a more accurate prediction of delivery times based on various factors, such as traffic, weather, vehicle condition, and more.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Food Delivery Time Prediction** project uses a machine learning model to predict the estimated delivery time for food orders. The model is trained on data that includes various features such as the condition of the delivery vehicle, traffic conditions, weather, and the type of order. The main goal of this project is to provide a range of estimated delivery times in an easy-to-understand format.

### Features:
- Predicts delivery time in minutes
- Provides delivery time range (e.g., 35-40 minutes) along with exact predictions
- Utilizes traffic, weather, and other order-related data

## Installation

### Prerequisites:
- Python 3.7 or above
- [XGBoost](https://xgboost.readthedocs.io/en/stable/) for machine learning
- [Streamlit](https://streamlit.io/) for the web interface
- [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/) for data handling
- [Geopy](https://geopy.readthedocs.io/en/stable/) for distance calculation

### Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/food-delivery-time-prediction.git
    cd food-delivery-time-prediction
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the project using Streamlit:
    ```bash
    streamlit run main.py
    ```

## Project Structure

```bash
food-delivery-time-prediction/
│
├── data/                   # Folder for storing datasets
├── models/                 # Folder for storing saved models
├── prediction.py           # Contains prediction logic
├── main.py                 # Streamlit app entry point
├── requirements.txt        # List of project dependencies
├── README.md               # Project documentation
└── tests/                  # Folder for unit tests
