import requests

def getWeather(lat, lon, APIkey):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    print(data)
    return {
        "main_temp": data["main[temp]"],
        "max_temp": data["main.temp_max"],
        "min_temp": data["main.temp_min"],
        "wind_speed": data["wind.speed"],
        "rain": data["rain"]
    }

Weather_Data = getWeather(40, 70, "077be3b7d8efd9180e8de0642a4ce332")
print(Weather_Data)


