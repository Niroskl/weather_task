# Project name: weather_task

## scope and information
###   The scope of this project is to retrieve the current temperature, weather conditions, and humidity for any city in the world by API using the OpenWeather website
###   I wrote the code using Google Colab and then used PyCharm to synchronize it with GitHub platform
###   my GitHub username: Niroskl

## code to run:
###   the code file "main.py" - to run in PyCharm
###   the code file "weather_app_nir.py" - to run using streamlit
####       after reviewing the documents at the streamlit site and using ChatGPT, I adapted the code language to fit the streamlit platform

## How to use this project:
###   press enter to get the question: "please enter city name you would like to know about the local weather:"
###   then type the name of the city you wish to know the following local weather data: temperature, weather conditions, and humidity
###   the code will check for details using a specific API from the OpenWeather site and return the data back


## Coding steps:
###   1. I opened an account on the OpenWeather site
###   2. personal API key obtained from site: 81661abd3ae3f6f042b8111f19aa7a9f
###   3. I checked on the site for examples and templates for how an API call looks like:
####       Example of API call: api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=81661abd3ae3f6f042b8111f19aa7a9f
####       Among the examples for API call on the site, this template fits the needs for this code: http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}
####           I used this template in the code, using this line (city = city_name.replace(' ', '%20')) to ensure that city names with spaces are correctly processed
###   4. the information returns from the site will be converted to .json format so the code can extract the necessary weather data
###   5. All the relevant data (temperature, humidity, and weather description) will be printed, along with the whole unedited crude json data obtained for the OpenWeather website (last coding line) - this was not requested in the project scope

## code on streamlit:
### to run the code from PyCharm on streamlit, write in the terminal tab: "streamlit run weather_app_nir.py"
### For using the streamlit platform I reviewed the documentation files and adapted the code to the streamlit coding platform with the help of ChatGPT
### note: for the streamlit code, If the city name requested is wrong, there is no need for a "while loop" because the user can delete the previous city name he wrote and write a new name


## files included in this project:
### the current file; README.md
### main.py and weather_app_nir.py
### .gitignore
### poetry.lock and pyproject.toml

# overall, it was very fun doing this project!



