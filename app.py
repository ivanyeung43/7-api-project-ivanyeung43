""" import requests

def getWeather(city):
    response = requests.get(f"http://localhost:3000/weather/{city}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
Weather_Data = getWeather("Curitiba")
print(Weather_Data) """


import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon)
