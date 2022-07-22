from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

headings = soup.find_all(name="a", class_="titlelink")

article_titles = []
article_links = []
article_scores = []

for head in headings:
    article_titles.append(head.getText())
    article_links.append(head.get("href"))


# print(article_titles)
# print(article_links)
# print(article_scores)


article_scores_int=[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_score = max(article_scores_int)
max_index =article_scores_int.index(max_score)

print(article_titles[max_index])
print(article_links[max_index])
print(article_scores_int[max_index])

