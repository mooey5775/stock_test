from tkinter import *

window = Tk()

# Get buy/sell data here
buy = True

if buy:
    txt = "Buy"
    color = "green"
else:
    txt = "Sell"
    color = "red"

label = Label(window, text=txt, bg=color, font=("Arial", 50), padx=20, pady=20)
label.pack()

window.mainloop()