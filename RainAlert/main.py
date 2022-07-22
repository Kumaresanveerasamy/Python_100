import requests
import os
from twilio.rest import Client

api_key = "9017150741f39ed36595980c988aac1f"
parameters = {
    "lat": 13.170984,
    "lon": 80.199112,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

hourly_data = data["hourly"][:12]

for info in hourly_data:
    weather_data = info["weather"]
    weather_id = weather_data[0]["id"]
    if weather_id > 700:
        
        account_sid = "AC2587ddfd0e51a154e8112e12faf2485a"
        auth_token = "188a073234a206baa1645ec9c4dafa03"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_="+15709895091",
            to='+917305297732',
            body="It's Gonna rain today, Don't forget to bring an Umbrella"
        )
        print(message.sid)
        break
