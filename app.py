class Cal:
    def kel_to_far(self, x):
        return (x - 273.15) * (9/5) + 32
    def kel_to_cel(self, x):
        return x - 273.15

import requests

def getWeather(lat, lon, APIkey):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    weatherDICT = {
        "main_temp": [data["main"]["temp"]],
        "max_temp": [data["main"]["temp_max"]],
        "min_temp": [data["main"]["temp_min"]],
        "wind_speed": [data["wind"]["speed"]],
    }
    print(weatherDICT)
getWeather(input("Enter latitude"), input("Enter Longitude"), input("Enter APIkey"))

"077be3b7d8efd9180e8de0642a4ce332"
    
    




