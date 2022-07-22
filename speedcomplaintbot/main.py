from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from twilio.rest import Client
import os

account_sid = "AC2587ddfd0e51a154e8112e12faf2485a"
auth_token = "188a073234a206baa1645ec9c4dafa03"
client = Client(account_sid, auth_token)


s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.speedtest.net/")
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

sleep(60)
download_speed = driver.find_element(By.XPATH,
                                     "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
upload_speed = driver.find_element(By.XPATH,
                                   "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text

msg = f" Download Speed: {download_speed} Mbps, Upload Speed: {upload_speed} Mbps"

message = client.messages.create(
    from_="+19363104368",
    to='+917305297732',
    body=msg)
print(message.sid)
