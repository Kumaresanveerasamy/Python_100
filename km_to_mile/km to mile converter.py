5
from tkinter import *


def convert():
    km_data = float(dialog.get())
    miles_data = km_data / 1.608
    label1.config(text=miles_data)


window = Tk()
window.minsize(height=150, width=300)
window.title("KM to MILES Converter")
window.config(padx=50, pady=50)

label1 = Label(text="0")
label1.grid(column=2, row=3)

label2 = Label(text="KM")
label2.grid(column=3, row=1)

calculate = Button(text="calculate", command=convert)
calculate.grid(column=2, row=2)

label3 = Label(text="Miles")
label3.grid(column=3, row=3)

dialog = Entry()
dialog.grid(column=2, row=1)

window.mainloop()
