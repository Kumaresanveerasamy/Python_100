from bs4 import BeautifulSoup
import requests

time_travel_date = input("Enter the Date you want to travel to , in this Format YYYY-MM-DD......")
URL = f"https://www.billboard.com/charts/hot-100/{time_travel_date}/"

response = requests.get(URL)

content = response.text

soup = BeautifulSoup(content, "html.parser")

movie_titles = [movie.getText().strip() for movie in soup.find_all(name="h3", id="title-of-a-story")]
song_titles = movie_titles[3:103]

with open(f"playlist_{time_travel_date}.txt",mode="w") as file:
    for song in song_titles:
        file.write(f"{song}\n")



