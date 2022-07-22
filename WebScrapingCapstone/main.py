from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# BeautifulSoup to extract data from zillow:

URL = "https://www.zillow.com/brooklyn-new-york-ny/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Brooklyn%2C%20New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.2075667415702%2C%22east%22%3A-73.66786337242958%2C%22south%22%3A40.58598386981961%2C%22north%22%3A40.72402785222149%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37607%2C%22regionType%22%3A17%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22price%22%3A%7B%22max%22%3A906182%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "html.parser")

all_prices = [price.getText() for price in soup.select(selector=".list-card-heading div")]
print(all_prices)

all_addresses = [address.getText() for address in soup.select(selector="div ul li a address ")]
print(all_addresses)

all_links = [link.get("href") for link in soup.select(selector=".list-card-info a")]
print(all_links)

all_spaces = [space.getText() for space in soup.select(selector=".list-card-details li ")]
all_spaces = all_spaces[2::4]
print(all_spaces)

# Selenium to automate entry in Google responses:

s = Service("C:\\Users\\satven\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

for n in range(len(all_spaces)):

    driver.get("https://forms.gle/2PBcpiBe61RwwKRH8")
    sleep(5)

    q1 = driver.find_element(By.XPATH,"//div[@class='freebirdFormviewerViewFormContent']//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    q2 = driver.find_element(By.XPATH,"//div[@role='list']//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    q3 = driver.find_element(By.XPATH,"//div[@class='freebirdFormviewerViewCenteredContent']//div[3]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    q4 = driver.find_element(By.XPATH,"//div[4]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    submit = driver.find_element(By.XPATH,"//span[contains(text(),'Submit')]")

    q1.send_keys(all_addresses[n])
    q2.send_keys(all_spaces[n])
    q3.send_keys(all_prices[n])
    q4.send_keys(all_links[n])
    submit.click()
