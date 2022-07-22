import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 13.204184
MY_LONG = 80.175126
email = "yyyyyy@gmail.com"
password = "xxxxxxxx"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data=response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
iss_position= (latitude,longitude)

parameters = {
    "lat": MY_LAT,
    "lng" : MY_LONG,
    "formatted":0
}
response = requests.get(url = "https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset =float(data["results"]["sunset"].split("T")[1].split(":")[0])

if sunrise == 0:
    sunrise=24

time_now= datetime.now()

while True:
    time.sleep(60)
    if time_now.hour < sunrise and time_now.hour > sunset:
        if latitude >= 8 and latitude <=18 and longitude <= 85 and longitude>= 75:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email,password=password)
                connection.sendmail(to_addrs="xxxxxx@hotmail.com",from_addr=email,
                                    msg = f"Subject: ISS Overwatch \n\n"
                                          f"ISS is currently above you")



