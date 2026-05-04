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
    
    weather =  {
        "main_temp": [data["main"]["temp"]],
        "max_temp": [data["main"]["temp_max"]],
        "min_temp": [data["main"]["temp_min"]],
        "wind_speed": [data["wind"]["speed"]],

        "clouds": [data["clouds"]["all"]]
    }
    return weather

weatherDATA = getWeather(input("Enter latitude"), input("Enter Longitude"), "077be3b7d8efd9180e8de0642a4ce332")
endPROGRAM = ""
while endPROGRAM != 10:
    questionDICT = {
        "1": "Average Temperature",
        "2": "Max Temperature",
        "3": "Min Temperature",
        "4": "Wind speed",
        "5": "Rain",
        "6": "Cloud Percentage"
    }
    for key, value in questionDICT.items():
        print(key, "→", value)
    userSELECTION = (input("Select information. Type 10 to end the program"))
    farenMAIN = int(weatherDATA["main_temp"][-1])
    farenMAX = int(weatherDATA["max_temp"][-1])
    farenMIN = int(weatherDATA["min_temp"][-1])
    if int(userSELECTION) == 10:
        break
    elif int(userSELECTION) == 1:
        print(round(farenMAIN - 273.15) * 9/5 + 32)
    elif int(userSELECTION) == 2:
        farenMAX = int(weatherDATA["max_temp"][-1])
        if farenMAX == farenMAIN:
            print("MAX and MIN temperatures are only available for large urban areas")
        else:
            print(round(farenMAX - 273.15) * 9/5 + 32)
    elif int(userSELECTION) == 3:
        if farenMIN == farenMAX:
            print("MAX and MIN temperatures are only available for large urban areas")
        else:
            print(round(farenMIN - 273.15) * 9/5 + 32)
    elif int(userSELECTION) == 4:
        print(weatherDATA["wind_speed"], "km")
    elif int(userSELECTION) == 5:
        print(weatherDATA["rain"])
    elif int(userSELECTION) == 6:
        print(weatherDATA["clouds"], "%")
print("WeatherAPP has ended")






