from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
pick_card = {}
german_cards= {}

try:
    data = pandas.read_csv("wordstolearn.csv")
except:
    data = pandas.read_csv("words_list.csv")
    german_cards = data.to_dict(orient="records")
else:
    german_cards = data.to_dict(orient="records")


def next_card():
    global pick_card, card_timer
    window.after_cancel(card_timer)
    pick_card = random.choice(german_cards)
    canvas.itemconfig(title_text, text="German", fill="black")
    canvas.itemconfig(word_text, text=pick_card["German"], fill="black")
    canvas.itemconfig(bgimage, image=german_side)
    card_timer = window.after(3000, func=flipcard)


def flipcard():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=pick_card["English"], fill="white")
    canvas.itemconfig(bgimage, image=english_side)


def known_card():
    german_cards.remove(pick_card)
    next_card()
    data = pandas.DataFrame(german_cards)
    data.to_csv("wordstolearn.csv", index=False)


window = Tk()
window.title("Flash cards -German")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_timer = window.after(3000, func=flipcard)

canvas = Canvas(width=800, height=526)
german_side = PhotoImage(file="images/card_front.png")
english_side = PhotoImage(file="images/card_back.png")
bgimage = canvas.create_image(400, 263, image=german_side)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title_text = canvas.create_text(400, 150, text="", font=("ariel", 30, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
