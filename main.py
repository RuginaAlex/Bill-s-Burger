from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#fffacd"
FONT_NAME = "Courier"
ORANGE = "#ffdab9"
PALE_ORANGE = "#ffc04c"

# ---------------------------- Commands ------------------------------- #

def set_regular():
    print("regular")

def set_deluxe():
    print("deluxe")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Bill's Burger Order")
window.geometry("650x400")
window.config(bg=YELLOW)
window.grid_rowconfigure(1, minsize=50)

img = PhotoImage(file="icon.png")
window.iconphoto(False, img)

title_label = Label(
    text="Bill's Burger Order System",
    bg=ORANGE,
    font=(FONT_NAME, 31),
    fg="black"
)
title_label.grid(column=0, row=0, columnspan=3, sticky="ew")




burger_type = StringVar(value="set this name to random , because I don't want any button to be selected when you "
                              "run the program.")


radio_regular = Radiobutton(
    window,
    text="Regular",
    variable=burger_type,
    value="Regular",
    font=("Arial", 12),
    bg=YELLOW,
    command= set_regular
)
radio_regular.grid(column=0, row=1, pady=20, padx=10)


radio_deluxe = Radiobutton(
    window,
    text="Deluxe",
    variable=burger_type,
    value="Deluxe",
    font=("Arial", 12),
    bg=YELLOW,
    command= set_deluxe
)
radio_deluxe.grid(column=1, row=1, pady=20, padx=10)



topping_label = Label(
    text="Select your Toppings",
    font=("Arial", 18, "bold"),
    bg=PALE_ORANGE,
    fg="black",
    padx=20,
    pady=10,
    relief="ridge",
    bd=3
)
topping_label.grid(column=0, row=2, columnspan=3, pady=20, sticky="ew")

window.mainloop()

