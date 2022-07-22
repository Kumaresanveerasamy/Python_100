from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

all_anchors = soup.find_all(name="a")

for tag in all_anchors:
    print(tag.getText())
    print(tag.get("href"))

all_headings = soup.find_all(name="h3", class_="heading")

for head in all_headings:
    print(head.getText())

print(soup.select(selector="p a"))

print(soup.select(".heading"))