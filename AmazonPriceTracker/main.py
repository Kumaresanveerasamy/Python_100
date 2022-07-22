from bs4 import BeautifulSoup
import smtplib
import requests

email = "d2dpuzzles@gmail.com"
password = "Kishorekums007@"

URL = "https://www.amazon.in/Logitech-Multi-Device-Bluetooth-Keyboard-Black/dp/B00MUTWLW4/ref=sr_1_5?keywords=keyboard+for+ipad+air+4&qid=1638032643&s=computers&sr=1-5"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept-Language": "en-US,en;q=0.5"
}
response = requests.get(URL, headers=header)
content = response.text
soup = BeautifulSoup(content, "html.parser")

current_price = soup.find(name="span", id="priceblock_ourprice").getText().split("₹")[1].split(".")[0]
product_name = soup.find(name="span", id="productTitle").getText().strip()
formatted_price = int(current_price.replace(",",""))


if formatted_price <= 1800:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="kishorekumaran007@gmail.com",
                            msg=f"Subject : Price Alert .\n\nThe price of {product_name} is now Rs. {formatted_price}.. Order Now")
