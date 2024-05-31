import datetime
import requests
import numpy as np
import pandas as pd
import streamlit as st

url = 'https://taxifare.lewagon.ai/predict'

today = datetime.datetime.now()
today_date_min_value = datetime.date(today.year, today.month, today.day)
today_time_value = datetime.time(today.hour, today.minute)

datetime_columns = st.columns(2)

date = datetime_columns[0].date_input("Date", min_value = today_date_min_value, key = "date")
time = datetime_columns[1].time_input("Time", value = today_time_value, key = "time")

pickup_columns = st.columns(2)

pickup_longitude = pickup_columns[0].number_input('Longitude de départ', key = "pickup_longitude", min_value = -79.7624, max_value = -71.7517,  value = -74.0518045)
pickup_latitude = pickup_columns[1].number_input('Latitude de départ', key = "pickup_latitude", min_value = 40.4772, max_value = 45.0153, value = 40.7591621)

dropoff_columns = st.columns(2)

dropoff_longitude = dropoff_columns[0].number_input("Longitude d'arrivée", key = "dropoff_longitude", min_value = -79.7624, max_value = -71.7517, value = -73.9235075)
dropoff_latitude = dropoff_columns[1].number_input("Latitude d'arrivée", key = "dropoff_latitude", min_value = 40.4772, max_value = 45.0153, value = 40.8517604)

passenger_count = st.number_input('Nombre de passagers', step = 1, key = "passenger_count", min_value = 1)

params = {
    "pickup_datetime": str(date) + " " + str(time),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

res = requests.get(url, params = params)

st.text("Montant estimé : " + str(round(res.json()["fare"], 2)) + "$")

def get_map_data():
    return pd.DataFrame(
        data = {
            'lat': [pickup_latitude, dropoff_latitude],
            'lon': [pickup_longitude, dropoff_longitude]
        }
    )
df = get_map_data()
st.map(df)
