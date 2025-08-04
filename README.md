# Project name: weather_task

# scope and information
#   The scope of this project: a code return current temperature, weather conditions, and humidity from any city in the world from OpenWeather site
#   I wrote the code using Colab and then used PyCharm to synchronize with GitHub platform
#   my GitHub username: Niroskl

# code to run:
#   the code file "main.py" - to run on PyCharm
#   the code file "weather_app_nir.py" - to run on streamlit
#       after looking at the streamlit site and using ChatGPT, I tried to adapt the code language to streamlit platform

# How to use this project:
#   press enter to get the question: "please enter city name you would like to know about the local weather:"
#   then type the name of the city you wish to know the local following data: temperature, weather conditions, and humidity
#   the code will check for details using the OpenWeather site and return the data back


# Coding steps:
#   I open an account on OpenWeather site
#   personal API key obtained from site: your API key 81661abd3ae3f6f042b8111f19aa7a9f
#   I checked in the site for examples and templates for how does API call looks like:
#       Example of API call: api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=81661abd3ae3f6f042b8111f19aa7a9f
#       Template fits for this code needs: http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}




