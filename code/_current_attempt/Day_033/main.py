import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
SMTP_SERVER_ADDRESS = "smtp.gmail.com"
PORT = 587
my_email = "" #Your email goes here
my_password = "" #Your email app password goes here


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = abs(MY_LAT - iss_latitude)
    lng_diff = abs(MY_LONG - iss_longitude)

    if lat_diff <= 5 and lng_diff <= 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise_data = response.json()
    sunrise_hour = int(sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sunrise_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset_hour or time_now.hour <= sunrise_hour:
        return True

while True:
    time.sleep(60)
    if iss_is_overhead() and is_dark():
        connection = smtplib.SMTP(SMTP_SERVER_ADDRESS, PORT)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="SUBJECT:Look UP\n\nThe ISS is overhead and its dark"
        )
