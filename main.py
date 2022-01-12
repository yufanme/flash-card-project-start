from tkinter import *
import pandas
import random

# get df_data
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


# ---------------------------------- get random word ------------------------------- #
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=front_image_path)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(3000, change_card, current_card)


# ---------------------------------- change to English card ------------------------ #
def change_card(current_card):
    canvas.itemconfig(canvas_img, image=back_image_path)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


BACKGROUND_COLOR = "#B1DDC6"

# create window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# image in canvas
front_image_path = PhotoImage(file="./images/card_front.png")
back_image_path = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_image_path)


# text in canvas
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create buttons
check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=0)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()

window.mainloop()
