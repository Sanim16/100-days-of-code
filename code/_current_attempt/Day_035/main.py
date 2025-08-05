import os
import requests
# from twilio.rest import Client


# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# twilio_number = ""
# my_number = ""


api_key = os.environ.get('OWM_API_KEY')
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

CURRENT_WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
FIVE_DAY_3_HR_API = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(FIVE_DAY_3_HR_API, parameters)
response.raise_for_status()

weather_data = response.json()
weather_id = [item["weather"][0]["id"] for item in weather_data["list"]]


if min(weather_id) < 700:
    print("Its going to rain")
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today, Take an Umbrella",
    #     from_=twilio_number,
    #     to=my_number,
    # )
