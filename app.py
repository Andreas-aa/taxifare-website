import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('Welcome')
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

date_time = st.text_input('Put date and time', '2012-10-06 12:10:00')
pickup_longitude = st.number_input('Put pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('Put pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('Put dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('Put dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('Put passenger count', min_value=1, max_value=8, step=1, value=1)

params = {'pickup_datetime': date_time,
          'pickup_longitude':pickup_longitude,
          'pickup_latitude':pickup_latitude,
          'dropoff_longitude':dropoff_longitude,
          'dropoff_latitude':dropoff_latitude,
          'passenger_count':passenger_count}


url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url, params=params).json()
result = round(response['fare'],0)
st.markdown(f'The fare is ${result}')
