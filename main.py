# The scope of this project: a code return current temperature, weather conditions, and humidity from any city in the world from OpenWeather site
# I wrote the code using Colab and then used PyCharm to synchronize with GitHub platform

# Steps:
#   I open an account on OpenWeather site
#   personal API key obtained from site: your API key 81661abd3ae3f6f042b8111f19aa7a9f
#   I checked in the site for examples and templates for how does API call looks like:
#       Example of API call: api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=81661abd3ae3f6f042b8111f19aa7a9f
#       Template fits for this code needs: http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# code:

# first I imported the requests library to be able to extract API from open world weather site
# at the terminal tab I wrote: pip install requests followed by -
import requests

city_name = input('please enter city name you would like to know about the local weather: ')
city = city_name.replace(' ', '%20')
API = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=81661abd3ae3f6f042b8111f19aa7a9f'
information = requests.get(API)
data = information.json()
print(f'The weather in {city_name} is:', data['weather'][0]['description'])
print(f'The temperature in {city_name} is:', data['main']['temp'], 'Co')
print(f'The humidity in {city_name} is:', data['main']['humidity'], 'Co')
print(information.text)


