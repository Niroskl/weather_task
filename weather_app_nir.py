import requests
import streamlit as st

st.title("Weather App by Niro")

city_name = st.text_input('please enter city name you would like to know about the local weather: ')
city = city_name.replace(' ', '%20')
API = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=81661abd3ae3f6f042b8111f19aa7a9f'
information = requests.get(API)
data = information.json()
st.write(f'The weather in {city_name} is:', data['weather'][0]['description'])
st.write(f'The temperature in {city_name} is:', data['main']['temp'], 'Co')
st.write(f'The humidity in {city_name} is:', data['main']['humidity'], 'Co')
st.write(information.text)

