#twilio recover code: PKCBN1ZZQJE83BM1GQ71L4HZ
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

N_TIMELAPSE = 4
#Porto Alegre Coordinate
weather_params = {
    "lat": -30.033056,
    "lon": -51.230000,
     "appid": os.getenv("API_KEY"),
     "cnt": N_TIMELAPSE

}

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=OWM_ENDPOINT, params=weather_params)  
response.raise_for_status()
weather_data = response.json()

will_rain = False
#print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    message = client.messages.create(
    body="It is going to rain today. 🌧️ Bring an umbrella. ☂️",
    from_='+13253089916',
    to='+5551991600284'
    )

print(message.status)

