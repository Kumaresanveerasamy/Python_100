from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
print(soup.find_all(name="h3",class_="jsx-4245974604"))

# movies_list = [movie.getText() for movie in soup.find_all(name="h3",class_="jsx-4245974604")]
# print(movies_list)