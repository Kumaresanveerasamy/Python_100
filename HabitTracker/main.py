import requests
from datetime import date

today = date.today().strftime("%Y%m%d")

TOKEN = "asdjadjdsohojiks"
USER_NAME = "kishore"
pixela_endpoint = "https://pixe.la/v1/users"
user_parmeters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url="pixel_endpoint", json=user_parmeters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Pythoning",
    "unit": "minutes",
    "color": "ajisai",
    "type": "float"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

plot_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"

plot_config = {
    "date": today,
    "quantity": input("How much time did you practiced today?")
}

response = requests.post(url=plot_endpoint, json=plot_config, headers=headers)
print(response.text)
