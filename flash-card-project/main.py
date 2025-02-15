import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)
def is_known():
    to_learn.remove(current_card)
    data =pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
window =Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=802, height=530)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
check_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")
card_image = canvas.create_image(403, 267, image=card_front)
card_title = canvas.create_text(403, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(403, 267, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
next_card()



window.mainloop()