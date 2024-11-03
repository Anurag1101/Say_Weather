import requests
import json
import pyttsx3

while True:
    city = input("Enter the name of city: ")
    url = f"https://api.weatherapi.com/v1/current.json?key=3d17c583de334f9195491352240311&q={city}"

    r=requests.get(url)
    wdic= json.loads(r.text)
    engine = pyttsx3.init()
    temp=(wdic["current"]["temp_c"])
    engine.say(f"The weather of {city} is {temp} degree Celsius")
    print(f"The weather of {city} is {temp} degree Celsius")
    engine.runAndWait()