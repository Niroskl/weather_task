import requests
import streamlit as st
from geopy.geocoders import Nominatim
import folium
import geopy
from streamlit_folium import st_folium

st.title("☁️Weather 🌈 App☁️")
st.markdown(f'Hello,  \nYou are in the right place for WEATHER check👋')
city_name = st.text_input('Please enter city name you would like to know about the local weather:')

if city_name:
    city = city_name.replace(' ', '%20')
    API = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=81661abd3ae3f6f042b8111f19aa7a9f'
    information = requests.get(API)
    data = information.json()

    if information.status_code == 200:
        st.write(f'<h2><b>The weather in {city_name.capitalize()}</b></h2>', unsafe_allow_html=True)
        st.write(f"<h4>⛅ Condition: {data['weather'][0]['description'].capitalize()}</h4>", unsafe_allow_html=True)
        st.write(f"<h4>🌡️ Temperature: {data['main']['temp']} °C</h4>", unsafe_allow_html=True)
        st.write(f"<h4>💧 Humidity: {data['main']['humidity']} %</h4>", unsafe_allow_html=True)
        st.write(f"<h4>💨 Wind: {data['wind']['speed']} m/s</h4>", unsafe_allow_html=True)
        st.write(f"<h4>🛰️ Pressure: {data['main']['pressure']} hPa</h4>", unsafe_allow_html=True)

    else:
        st.error("city name is invalid, please try again")

if city_name:
    geolocator = Nominatim(user_agent="city_mapper")
    location = geolocator.geocode(city_name)

    if location:
        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
        folium.Marker([location.latitude, location.longitude], popup=city_name).add_to(m)

        st_folium(m, width=700, height=500)





