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

### Demo:
You can also check out a live demo of this project hosted on **Streamlit** at the following link:
[Live Demo on Streamlit]([https://share.streamlit.io/your-username/food-delivery-time-prediction/main.py](https://fooddeliverytime-marynyk.streamlit.app/))

In this demo, you can input different parameters such as coordinates of restaurant and delivery location, vehicle condition, traffic, weather and others to see real-time predictions for food delivery times.

## Installation

### Prerequisites:
To run this project, you will need the following libraries and tools installed:

- **Python 3.7** or above
- **[geopy](https://geopy.readthedocs.io/en/stable/)** for distance calculation
- **pickle** for saving and loading models (built into Python)
- **[scikit-learn](https://scikit-learn.org/stable/)** for machine learning models
- **[pandas](https://pandas.pydata.org/)** for data manipulation
- **[NumPy](https://numpy.org/)** for numerical computations
- **[Streamlit](https://streamlit.io/)** for the web interface
- **[folium](https://python-visualization.github.io/folium/)** for interactive maps
- **[streamlit-folium](https://github.com/randyzwitch/streamlit-folium)** for integrating folium maps into Streamlit


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
