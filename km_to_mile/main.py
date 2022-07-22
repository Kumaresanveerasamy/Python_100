from tkinter import *

def button_clicked():
    label.config(text= dialog.get())
def button1_clicked():
    label.config(text= "Arigatho")

window = Tk()
window.minsize(height=300, width=500)
window.title("My First GUI")

label = Label()
label.grid(column=0, row=0)

button = Button(text="repeat text", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="thank me", command=button1_clicked)
button1.grid(column=2, row=0)

dialog = Entry()
dialog.grid(column= 3, row = 3)



window.mainloop()