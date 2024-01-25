import requests
import json

city = input("Enter the name of the city : ")

url = f"https://api.weatherapi.com/v1/current.json?key=c405d265cc1a4eafa1f172946242501&q={city}&aqi=no"

r=requests.get(url)
#print(r.text)
weather_desc = json.loads(r.text)
#print(weather_desc['current']['temp_c'])
country_name = weather_desc["location"]['country']
print(f"Country : {country_name}")
state_name = weather_desc["location"]['region']
print(f"State : {state_name}")
city_name = weather_desc["location"]['name']
print(f"city name : {city_name}")
time_zone = weather_desc["location"]['tz_id']
print(f"time zone : {time_zone}")
temperature_c = weather_desc["current"]["temp_c"]
print(f"temperature in celsius : {temperature_c}")
temperature_f = weather_desc['current']["temp_f"]
print(f"temperature in fahrenheit : {temperature_f}")
last_updated = weather_desc['current']["last_updated"]
print(f"last updated date : {last_updated}")
condition = weather_desc['current']["condition"]['text']
print(f"Weather condition : {condition}")


