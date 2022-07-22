import pandas

data = pandas.read_csv("Squirrel_Data.csv")
data_list = data["Primary Fur Color"].to_list()

grey = 0
red = 0
black = 0

for color in data_list:
    if color == "Gray":
        grey += 1
    if color == "Cinnamon":
        red += 1
    if color == "Black":
        black += 1

color_data = {
    "fur color":['Grey','Red','Black'],
    "count":[grey,red,black]
}

Colours = pandas.DataFrame(color_data)
Colours.to_csv("colors_data.csv")

