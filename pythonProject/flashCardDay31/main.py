from tkinter import *
import pandas
import random

# ____________________ NEXT CARD ___________________#

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# _______________________ FLIP CARD __________________________________#
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ___________________ REMOVE KNOWN WORDS _____________________________#
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    rem_data = pandas.DataFrame(to_learn)
    rem_data.to_csv("data/words_to_learn")
    next_card()




# _____________________________ UI ___________________________________#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("poppins", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("poppins", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)
unknown_button.config(highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)

tick_image = PhotoImage(file="images/right.png")
known_button = Button(image=tick_image)
known_button.grid(row=1, column=1)
known_button.config(highlightthickness=0, background=BACKGROUND_COLOR, command=is_known)

next_card()
window.mainloop()
