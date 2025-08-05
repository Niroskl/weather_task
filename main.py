# code:
# first I imported the requests library to be able to extract API from open world weather site
# at the terminal tab I wrote: "pip install requests" followed by -

import requests

while True:
    city_name = input('please enter city name you would like to know about the local weather: ')
    city = city_name.replace(' ', '%20')
    API = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=81661abd3ae3f6f042b8111f19aa7a9f'
    information = requests.get(API)

    if information.status_code == 200:
        data = information.json()
        print(f'The current weather in {city_name} is:', data['weather'][0]['description'])
        print(f'The temperature in {city_name} is:', data['main']['temp'], '°C')
        print(f'The humidity in {city_name} is:', data['main']['humidity'], '%')
        print(information.text)
        break
    else:
        print("city name is invalid, please try again")




