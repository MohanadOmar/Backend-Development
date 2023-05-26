from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
new_word = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


# ------------------------generate new word----------------------- #
def generate_new_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(words_to_learn)

    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_word["French"], fill="black")
    canvas.itemconfig(canvas_img, image=front_card_img)
    flip_timer = window.after(3000, flip_card)


# ----------------------Flip Card----------------- #
def flip_card():
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_word["English"], fill="white")


# -------------------------- is Known ----------------- #
def is_known():
    words_to_learn.remove(new_word)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_new_word()

# --------------------------GUI-------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(highlightthickness=0)
card_language = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))


# Buttons
wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, borderwidth=0, command=generate_new_word)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(column=1, row=1)

generate_new_word()

window.mainloop()