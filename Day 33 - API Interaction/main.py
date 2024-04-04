import requests
from datetime import datetime     
import smtplib


MY_LAT = 51.5073
MY_LNG = -0.1277
TIME_FORMATED = 0
MY_EMAIL = "kuhn.python@gmail.com"
PASSWORD = "jijdcdzqrnkizysr"

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

    

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": TIME_FORMATED
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunset = int(data["results"]["sunset"].split("T").split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T").split(":")[0])

    time_now = datetime.now().hour
    
    if time_now <= sunrise or time_now >=sunset:
        return True
    

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs=MY_EMAIL, 
                        msg=f"Subject: Look Up!\n\nThe ISS is above you in the sky!")


if is_overhead() and is_night():
    send_email()