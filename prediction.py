from geopy.distance import geodesic
import pickle
import sklearn
import pandas as pd
import numpy as np


# Функція для визначення частини доби
def get_time_of_day_single(time):
    if time < pd.Timedelta(hours=6):
        return 'Night'
    elif time < pd.Timedelta(hours=12):
        return 'Morning'
    elif time < pd.Timedelta(hours=18):
        return 'Afternoon'
    else:
        return 'Evening'


def preprocessing(data):
    with open('label_encoders.pkl', 'rb') as file:
        loaded_encodings = pickle.load(file)

    age, rating, coord_restaurant, coord_delivery_loc, order_date, order_time, order_time_picked, weather_conditions, road_traffic_density, type_of_order, type_of_vehicle, festival, city, vehicle_condition, multiple_deliveries = data
    Delivery_person_Age = age
    Delivery_person_Ratings = rating
    Weather_conditions = loaded_encodings['Weather_conditions'].get(weather_conditions)
    Road_traffic_density = loaded_encodings['Road_traffic_density'].get(road_traffic_density)
    vehicle_conditions_mapping = {'Poor': 0, 'Satisfactory': 1, 'Good': 2}
    Vehicle_conditions = vehicle_conditions_mapping.get(vehicle_condition)
    Type_of_order = loaded_encodings['Type_of_order'].get(type_of_order)
    Type_of_vehicle = loaded_encodings['Type_of_vehicle'].get(type_of_vehicle)
    multiple_deliveries_mapping = {'No': 0, 'Yes': 1}
    multiple_deliveries = multiple_deliveries_mapping.get(multiple_deliveries)
    Festival = loaded_encodings['Festival'].get(festival)
    City = loaded_encodings['City'].get(city)

    order_time_delta = pd.to_timedelta(order_time.hour, unit='h') + pd.to_timedelta(order_time.minute, unit='m')
    Time_of_Day = loaded_encodings['Time_of_Day'].get(get_time_of_day_single(order_time_delta))

    order_date_timestamp = pd.Timestamp(order_date)
    Order_day_of_week = order_date_timestamp.day_of_week
    Order_is_weekend = np.where(Order_day_of_week in [5, 6], 1, 0)

    # Форматування часу замовлення
    date_time_ordered = pd.Timestamp.combine(order_date, order_time)
    date_time_order_picked = pd.Timestamp.combine(order_date, order_time_picked)

    # Корекція дати для часу, коли замовлення забрано після півночі
    if order_time_picked < order_time:
        date_time_order_picked += pd.DateOffset(days=1)

    # Обчислення часу підготовки замовлення (в хвилинах)
    order_prepare_time = (date_time_order_picked - date_time_ordered).total_seconds() / 60

    geodesic_distance_km = round(geodesic(coord_restaurant, coord_delivery_loc).kilometers, 2)

    return [Delivery_person_Age, Delivery_person_Ratings, Weather_conditions, Road_traffic_density, Vehicle_conditions, Type_of_order, Type_of_vehicle, multiple_deliveries, Festival, City, Time_of_Day, Order_day_of_week, Order_is_weekend, order_prepare_time, geodesic_distance_km]

def prediction(data):
    features = preprocessing(data)
    features = np.array(features).reshape(1,-1)

    with open('scaler_delivery.pkl', 'rb') as file:
        loaded_scaler = pickle.load(file)

    features_scaled = loaded_scaler.transform(features)
    model = pickle.load(open("xgb_model_delivery", "rb"))
    predictions = model.predict(features_scaled)
    return predictions


def format_delivery_time(predicted_time):
    # Округлення вниз і вгору до найближчих кратних 5
    lower_bound = 5 * np.floor(predicted_time / 5)
    upper_bound = 5 * np.ceil(predicted_time / 5)

    return f"{int(lower_bound)}-{int(upper_bound)} хв (model predicts {predicted_time:.1f} хв)"
