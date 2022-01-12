from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# create canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
# image in canvas
front_img = PhotoImage(file="./images/card_front.png")
# back_img = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=back_img)
canvas.create_image(400, 263, image=front_img)
# text in canvas
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Trouve", font=("Ariel", 60, "bold"))


canvas.grid(row=0, column=0, columnspan=2)

# create buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
