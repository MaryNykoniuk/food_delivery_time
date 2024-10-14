import streamlit as st
from streamlit_folium import st_folium
import folium
from datetime import date
from datetime import datetime
from prediction import prediction
from prediction import format_delivery_time
# 49.84206423570553, 24.03130888684479
# Ініціалізація сесійного стану для збереження координат
if 'location1' not in st.session_state:
    st.session_state['location1'] = (0, 0)
if 'location2' not in st.session_state:
    st.session_state['location2'] = (0, 0)

# Перемикач між першим і другим місцем
st.header("Вибір місцезнаходження")
step = st.selectbox("Виберіть місце, для якого потрібно обрати координати", options=["Адреса ресторану/кафе", "Адреса місця доставки"])

# Визначення центру карти та зуму
center_location = [49.84206423570553, 24.03130888684479]  # Lviv
zoom_start = 12

# Створення карти
m = folium.Map(location=center_location, zoom_start=zoom_start)

# Відображення карти та збереження координат кліків
click_info = st_folium(m, width=700, height=500)

# Оновлення координат тільки на поточному кроці при кліку на карту
if step == "Адреса ресторану/кафе":
    st.write("Визначте координати ресторану/кафе:")
    if click_info and 'last_clicked' in click_info and click_info['last_clicked']:
        if (click_info['last_clicked']['lat'], click_info['last_clicked']['lng']) != st.session_state['location2']:
            st.session_state['location1'] = (click_info['last_clicked']['lat'], click_info['last_clicked']['lng'])

elif step == "Адреса місця доставки":
    st.write("Визначте координати місця доставки:")
    if click_info and 'last_clicked' in click_info and click_info['last_clicked']:
        if (click_info['last_clicked']['lat'], click_info['last_clicked']['lng']) != st.session_state['location1']:
            st.session_state['location2'] = (click_info['last_clicked']['lat'], click_info['last_clicked']['lng'])


# Відображення обох координат, якщо вони визначені
if st.session_state['location1']:
    st.write(f"Координати ресторану/кафе: {st.session_state['location1']}")
if st.session_state['location2']:
    st.write(f"Координати місця доставки: {st.session_state['location2']}")

# Введення даних про кур'єра
st.header("Дані про кур'єра")
age = st.number_input("Вік кур'єра", min_value=18, max_value=100, value=30)
#st.write(type(age))
rating = st.slider("Рейтинг кур'єра", min_value=1.0, max_value=5.0, value=4.5, step=0.1)
#st.write(type(rating))
st.header("Дані про замовлення та умови доставки")
order_date = st.date_input("Дата замовлення", value=date.today())
#st.write(type(order_date))
st.write(order_date)
order_time = st.time_input("Час замовлення")
#st.write(type(order_time))
order_time_picked = st.time_input("Час видачі замовлення рестораном/кафе")
#st.write(type(order_time_picked))
# Список погодних умов
weather_conditions_list = ["Cloudy", "Fog", "Sandstorms", "Stormy", "Sunny", "Windy"]

# Вибір погодних умов зі списку
weather_conditions = st.selectbox("Оберіть погодні умови", options=weather_conditions_list)
#st.write(type(weather_conditions))

road_traffic_density_list = ['High', 'Jam', 'Low', 'Medium']
road_traffic_density = st.selectbox("Оберіть щільність дорожнього руху на час доставки", options=road_traffic_density_list)
#st.write(type(road_traffic_density))

type_of_order_list = ['Buffet', 'Drinks', 'Meal ', 'Snack']
type_of_order = st.selectbox("Оберіть тип замовлення", options=type_of_order_list)
#st.write(type(type_of_order))

type_of_vehicle_list = ['electric_scooter', 'motorcycle', 'scooter']
type_of_vehicle = st.selectbox("Оберіть тип транспорту кур'єра", options=type_of_vehicle_list)
#st.write(type(type_of_vehicle))

festival_list = ['Yes', "No"]
festival = st.selectbox("Замовлення зроблене під час фестивалю або святкового періоду?", options=festival_list)
#st.write(type(festival))

city_type = ['Metropolitian', 'Semi-Urban', 'Urban']
city = st.selectbox("Тип міста", options=city_type)
#st.write(type(city))

vehicle_condition_list = ['Poor', 'Satisfactory', 'Good']
vehicle_condition = st.selectbox("Стан транспортного засобу, який використовує кур'єр", options=vehicle_condition_list)
#st.write(type(vehicle_condition))

multiple_deliveries_list = ['Yes', 'No']
multiple_deliveries = st.selectbox("Чи робить кур'єр кілька доставок під час цього замовлення?", options=multiple_deliveries_list)
#st.write(type(multiple_deliveries))

data_for_pred = [age, rating, st.session_state['location1'], st.session_state['location2'], order_date, order_time,
                 order_time_picked, weather_conditions, road_traffic_density, type_of_order, type_of_vehicle, festival,
                 city, vehicle_condition, multiple_deliveries]

pred_value = prediction(data_for_pred)
pred_value = round(float(pred_value[0]), 2)
formatted_time = format_delivery_time(pred_value)

st.success("The predicted time of delivery is {}.".format(formatted_time))