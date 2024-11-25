from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#fffacd"
FONT_NAME = "Courier"
ORANGE = "#ffdab9"
PALE_ORANGE = "#ffc04c"

# ---------------------------- Commands ------------------------------- #

def set_regular():
    # print("regular")
    pass
def set_deluxe():
    # print("deluxe")
    pass



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Bill's Burger Order")
window.geometry("1100x400")
window.config(bg=YELLOW)
window.grid_rowconfigure(1, minsize=50)



# canvas = Canvas(window, width=800, height=600, bg=YELLOW, highlightthickness=0)
# canvas.place(x=0, y=0)  # Poziționăm pe întreaga fereastră
#
# # Încărcăm imaginea
# icon_image = PhotoImage(file="icon.png")
# canvas.create_image(325, 200, image=icon_image)  # Centrăm imaginea (jumătatea lățimii și înălțimii)




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
# radio_regular.grid(column=0, row=1, pady=15, padx=20)
radio_regular.place(x=130,y=70)


radio_deluxe = Radiobutton(
    window,
    text="Deluxe",
    variable=burger_type,
    value="Deluxe",
    font=("Arial", 12),
    bg=YELLOW,
    command= set_deluxe
)
# radio_deluxe.grid(column=2, row=1, pady=15, padx=2)
radio_deluxe.place(x= 420, y = 70)


topping_label = Label(
    text="Select your extra toppings",
    font=("Arial", 18, "bold"),
    bg=PALE_ORANGE,
    fg="black",
    padx=10,  # Reducem padding-ul
    pady=5,   # Reducem padding-ul
    relief="ridge",
    bd=3,
    width= 42
)
topping_label.place(y=110)  # Ajustăm coordonatele



cheese_option = ["Cheddar : 1.0$", "Gouda : 1.0$"]

# Crearea Listbox-ului
listbox_cheese = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=14, exportselection=False)
listbox_cheese.place(x=20, y=200)

# Adăugăm opțiunile în Listbox
for option in cheese_option:
    listbox_cheese.insert(END, option)


meat_option = ["Bacon : 1.5$", "Ham : 1.5$"]

# Crearea Listbox-ului
listbox_meat = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=14, exportselection=False)
listbox_meat.place(x=240, y=200)


# Adăugăm opțiunile în Listbox
for option in meat_option:
    listbox_meat.insert(END, option)


special_option = ["Avocado : 1.0$", "Jalapeños : 1.0$"]




# Crearea Listbox-ului
listbox_special = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=16, exportselection=False)
listbox_special.place(x=460, y=200)

# Adăugăm opțiunile în Listbox
for option in special_option:
    listbox_special.insert(END, option)








cheese_label = Label(
    window,
    text="Cheese:",
    font=("Arial", 16, "bold"),
    fg="black",
    bg="#fffacd"
)
cheese_label.place( x = 50, y = 160)  # Poziționat cu padding vertical

meat_label = Label(
    window,
    text="Meat:",
    font=("Arial", 16, "bold"),
    fg="black",
    bg="#fffacd"
)
meat_label.place( x = 280, y = 160)  # Poziționat cu padding vertical


special_label = Label(
    window,
    text="Special:",
    font=("Arial", 16, "bold"),
    fg="black",
    bg="#fffacd"
)
special_label.place( x = 500, y = 160)  # Poziționat cu padding vertical




drink_options = ["Coke", "Sprite", "Water", "Orange Juice", "Iced Tea"]
selected_drink = StringVar()
selected_drink.set("Select a drink")
dropdown_drink = OptionMenu(window, selected_drink, *drink_options)
dropdown_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
dropdown_drink.place(x=30, y=330)

# Dropdown pentru Garnish
garnish_options = ["Fries", "Sweet Potato Fries", "Coleslaw", "Pickles", "Onion Rings"]
selected_garnish = StringVar()
selected_garnish.set("Select a garnish")
dropdown_garnish = OptionMenu(window, selected_garnish, *garnish_options)
dropdown_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
dropdown_garnish.place(x=380 , y= 330)


topping_label = Label(
    text="Select your items",
    font=("Arial", 18, "bold"),
    bg=PALE_ORANGE,
    fg="black",
    padx=10,  # Reducem padding-ul
    pady=5,   # Reducem padding-ul
    relief="ridge",
    bd=3,
    width= 42
)
topping_label.place(y=260)  # Ajustăm coordonatele

# ---------------------------- BILL AREA ------------------------------- #


bill_area_label = Label(
    window,
    text="Bill Area",
    bg=ORANGE,
    font=(FONT_NAME, 31),
    fg="black",
    width=10  # Lățimea extinsă pentru a arăta mai bine
)
bill_area_label.place(x=750, y=0)  # Poziționăm eticheta în partea dreaptă

bill_area = Text(
    window,
    font=("Courier", 12),
    width=30,  # Extindem lățimea zonei de text
    height=17,  # Ajustăm înălțimea
    bg="white",
    relief="ridge",
    bd=3
)
bill_area.place(x=730, y=70)  # Poziționăm textul în partea dreaptă

# Adăugăm antetul în "Bill Area"
bill_area.insert(END, "Welcome Customer\n")
bill_area.insert(END, "Bill Number: 001\n")
bill_area.insert(END, "------------------------------\n")
bill_area.insert(END, "Product       Qty     Price\n")
bill_area.insert(END, "------------------------------\n")

# Dezactivăm editarea manuală a zonei de text
bill_area.config(state=DISABLED)


# Creăm un Canvas pentru linia verticală
separator = Canvas(window, width=5, height=400, bg=PALE_ORANGE, highlightthickness=1)
separator.place(x=670, y=0)  # Poziționăm linia între cele două secțiuni


window.mainloop()

