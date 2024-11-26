from tkinter import *
from tkinter import messagebox

from MealOrder import MealOrder

# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#fffacd"
FONT_NAME = "Courier"
ORANGE = "#ffdab9"
PALE_ORANGE = "#ffc04c"

# ---------------------------- Commands ------------------------------- #

def set_regular():
    show_all_regular()

def set_deluxe():
    show_all_deluxe()



def show_all_regular():
    canvas1.delete("all")
    canvas2.delete("all")
    window.geometry("1100x450")
    order_regular()

def show_all_deluxe():
    canvas1.delete("all")
    canvas2.delete("all")
    window.geometry("1100x450")
    order_deluxe()


def get_selected_items(listbox_cheese, listbox_meat, listbox_special):
    def clean_selection(selection):
        # Extragem doar numele topping-ului (partea înainte de ":")
        return [item.split(":")[0].strip() for item in selection]

    cheese_selection = clean_selection([listbox_cheese.get(i) for i in listbox_cheese.curselection()])
    meat_selection = clean_selection([listbox_meat.get(i) for i in listbox_meat.curselection()])
    special_selection = clean_selection([listbox_special.get(i) for i in listbox_special.curselection()])

    # Returnează selecțiile ca dicționar
    return {
        "cheese": cheese_selection,
        "meat": meat_selection,
        "special": special_selection,
    }



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Bill's Burger Order")
window.geometry("650x400")
window.config(bg=YELLOW)
window.grid_rowconfigure(1, minsize=50)


canvas1 = Canvas(window, width=800, height=600, bg=YELLOW, highlightthickness=0)
canvas1.place(x=-180, y=60)  # Poziționăm pe întreaga fereastră

# Încărcăm imaginea
image = PhotoImage(file="regular.png")
canvas1.create_image(325, 200, image=image)  # Centrăm imaginea (jumătatea lățimii și înălțimii)




canvas2 = Canvas(window, width=800, height=600, bg=YELLOW, highlightthickness=0)
canvas2.place(x=270, y=55)  # Poziționăm pe întreaga fereastră

# Încărcăm imaginea
icon_image = PhotoImage(file="deluxe.png")
canvas2.create_image(200, 200, image=icon_image)  # Centrăm imaginea (jumătatea lățimii și înălțimii)




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
    font=("Arial", 12,'bold'),
    bg=YELLOW,
    command= set_regular
)
radio_regular.place(x=110,y=70)


radio_deluxe = Radiobutton(
    window,
    text="Deluxe",
    variable=burger_type,
    value="Deluxe",
    font=("Arial", 12,'bold'),
    bg=YELLOW,
    command= set_deluxe
)
radio_deluxe.place(x= 430, y = 70)


def order_regular():


    topping_label = Label(
        text="Select your extra toppings",
        font=("Arial", 18, "bold"),
        bg=PALE_ORANGE,
        fg="black",
        padx=10,
        pady=5,
        relief="ridge",
        bd=3,
        width= 42
    )
    topping_label.place(y=110)  # Ajustăm coordonatele





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

    selected_drink = StringVar()
    selected_drink.set("Select a drink")
    dropdown_drink = OptionMenu(window, selected_drink, "Coke", "Sprite", "Water", "Orange Juice", "Iced Tea")
    dropdown_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_drink.place(x=30, y=330)



    selected_garnish = StringVar()
    selected_garnish.set("Select a garnish")
    dropdown_garnish = OptionMenu(window, selected_garnish, "Fries", "Sweet Potato Fries", "Coleslaw", "Pickles",
                                  "Onion Rings")
    dropdown_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_garnish.place(x=380, y=330)


    selected_size_drink = StringVar()
    selected_size_drink.set("Select a drink size")
    dropdown_size_drink = OptionMenu(window,selected_size_drink,"MEDIUM","SMALL","LARGE")
    dropdown_size_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_size_drink.place(x=30 ,y= 370)

    selected_size_garnish = StringVar()
    selected_size_garnish.set("Select a garnish size")
    dropdown_size_garnish = OptionMenu(window, selected_size_garnish, "MEDIUM", "SMALL", "LARGE")
    dropdown_size_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_size_garnish.place(x=380, y=370)




    # Creăm Listbox-urile pentru topping-uri
    cheese_option = ["Cheddar : 1.0$", "Gouda : 1.0$"]
    listbox_cheese = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=14,
                             exportselection=False)
    listbox_cheese.place(x=20, y=200)
    for option in cheese_option:
        listbox_cheese.insert(END, option)




    meat_option = ["Bacon : 1.5$", "Ham : 1.5$"]
    listbox_meat = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=14,
                           exportselection=False)

    listbox_meat.place(x=240, y=200)
    for option in meat_option:
        listbox_meat.insert(END, option)




    special_option = ["Avocado : 1.0$", "Jalapeños : 1.0$"]
    listbox_special = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=16,
                              exportselection=False)
    listbox_special.place(x=460, y=200)
    for option in special_option:
        listbox_special.insert(END, option)

    def generate_bill_regular():
        # Obține selecțiile din Listbox-uri
        selections = get_selected_items(listbox_cheese, listbox_meat, listbox_special)
        cheese = selections["cheese"]
        meat = selections["meat"]
        special = selections["special"]

        # Obține selecțiile din dropdown-uri
        drink = selected_drink.get()
        garnish = selected_garnish.get()
        size_drink = selected_size_drink.get()
        size_garnish = selected_size_garnish.get()

        # Verificăm dacă toate selecțiile sunt făcute

        if drink == "Select a drink":
            messagebox.showwarning("Incomplete Selection", "Please select a drink!")
            return
        if garnish == "Select a garnish":
            messagebox.showwarning("Incomplete Selection", "Please select a garnish!")
            return
        if size_drink == "Select the drink size":
            messagebox.showwarning("Incomplete Selection", "Please select a drink size!")
            return
        if size_garnish == "Select the drink size":
            messagebox.showwarning("Incomplete Selection", "Please select a garnish size!")
            return

        # Creăm un obiect MealOrder
        order = MealOrder("Regular", drink, garnish)
        burger_price = order.get_burger_price()

        # Adăugăm toppingurile individual, iterând prin liste
        for topping in cheese:
            order.add_burger_toppings(topping)
        for topping in meat:
            order.add_burger_toppings(topping)
        for topping in special:
            order.add_burger_toppings(topping)

        order.set_drink_size(size_drink)
        order.set_side_size(size_garnish)

        # Calculăm totalul
        total_price = order.get_total_price()

        # Actualizăm zona de factură ("Bill Area")
        bill_area.config(state=NORMAL)  # Permitem editarea temporară
        bill_area.delete("1.0", END)  # Ștergem conținutul anterior
        bill_area.insert(END, "       Welcome Customer\n")
        bill_area.insert(END, "       Bill Number: 001\n")
        bill_area.insert(END, "------------------------------\n")
        bill_area.insert(END, "Product               Price\n")
        bill_area.insert(END, "------------------------------\n")

        # Afișăm selecțiile în "Bill Area"
        bill_area.insert(END, f"Regular burger: ${burger_price}\n")
        for item in cheese:
            bill_area.insert(END, f"{item} : $1.0\n")
        for item in meat:
            bill_area.insert(END, f"{item}: $1.5\n")
        for item in special:
            bill_area.insert(END, f"{item}: $1.0\n")
        if drink != "Select a drink":
            bill_area.insert(END, f"{drink} : ${order.drink.get_adjusted_price():.2f}\n")
        if garnish != "Select a garnish":
            bill_area.insert(END, f"{garnish} : ${order.side.get_adjusted_price():.2f}\n")

        bill_area.insert(END, "------------------------------\n")
        bill_area.insert(END, f"Total Price: ${total_price:.2f}\n")
        bill_area.config(state=DISABLED)  # Blochează editarea din nou

    # Butonul "Generate Bill"
    bill_button = Button(
        window,
        text="Generate Bill",
        font=("Arial", 14, "bold"),
        bg=ORANGE,
        fg="black",
        width=15,  # Lățimea butonului
        height=2,  # Înălțimea butonului
        command=generate_bill_regular  # Apelează funcția generate_bill
    )
    bill_button.place(x=800, y=385)  # Poziționăm butonul în partea dreaptă jos

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
    bill_area.insert(END, "       Welcome Customer\n")
    bill_area.insert(END, "       Bill Number: 001\n")
    bill_area.insert(END, "------------------------------\n")
    bill_area.insert(END, "Product               Price\n")
    bill_area.insert(END, "------------------------------\n")
    bill_area.config(state=DISABLED)  # Blochează editarea manuală

    # Creăm un Canvas pentru linia verticală
    separator = Canvas(window, width=5, height=600, bg=PALE_ORANGE, highlightthickness=1)
    separator.place(x=670, y=0)  # Poziționăm linia între cele două secțiuni



def order_deluxe():
    topping_label = Label(
        text="Select your extra toppings",
        font=("Arial", 18, "bold"),
        bg=PALE_ORANGE,
        fg="black",
        padx=10,
        pady=5,
        relief="ridge",
        bd=3,
        width=42
    )
    topping_label.place(y=110)  # Ajustăm coordonatele

    cheese_label = Label(
        window,
        text="Cheese:",
        font=("Arial", 16, "bold"),
        fg="black",
        bg="#fffacd"
    )
    cheese_label.place(x=50, y=160)  # Poziționat cu padding vertical

    meat_label = Label(
        window,
        text="Meat:",
        font=("Arial", 16, "bold"),
        fg="black",
        bg="#fffacd"
    )
    meat_label.place(x=280, y=160)  # Poziționat cu padding vertical

    special_label = Label(
        window,
        text="Special:",
        font=("Arial", 16, "bold"),
        fg="black",
        bg="#fffacd"
    )
    special_label.place(x=500, y=160)  # Poziționat cu padding vertical

    selected_drink = StringVar()
    selected_drink.set("Select a drink")
    dropdown_drink = OptionMenu(window, selected_drink, "Coke", "Sprite", "Water", "Orange Juice", "Iced Tea")
    dropdown_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_drink.place(x=30, y=330)

    selected_garnish = StringVar()
    selected_garnish.set("Select a garnish")
    dropdown_garnish = OptionMenu(window, selected_garnish, "Fries", "Sweet Potato Fries", "Coleslaw", "Pickles",
                                  "Onion Rings")
    dropdown_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_garnish.place(x=380, y=330)

    selected_size_drink = StringVar()
    selected_size_drink.set("Select a drink size")
    dropdown_size_drink = OptionMenu(window, selected_size_drink, "MEDIUM", "SMALL", "LARGE")
    dropdown_size_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_size_drink.place(x=30, y=370)

    selected_size_garnish = StringVar()
    selected_size_garnish.set("Select a garnish size")
    dropdown_size_garnish = OptionMenu(window, selected_size_garnish, "MEDIUM", "SMALL", "LARGE")
    dropdown_size_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_size_garnish.place(x=380, y=370)

    # Creăm Listbox-urile pentru topping-uri
    cheese_option = ["Cheddar : 1.0$", "Gouda : 1.0$"]
    listbox_cheese = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=14,
                             exportselection=False)
    listbox_cheese.place(x=20, y=200)
    for option in cheese_option:
        listbox_cheese.insert(END, option)

    meat_option = ["Bacon : 1.5$", "Ham : 1.5$"]
    listbox_meat = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=14,
                           exportselection=False)

    listbox_meat.place(x=240, y=200)
    for option in meat_option:
        listbox_meat.insert(END, option)

    special_option = ["Avocado : 1.0$", "Jalapeños : 1.0$"]
    listbox_special = Listbox(window, selectmode="multiple", font=(FONT_NAME, 12), bg=ORANGE, height=2, width=16,
                              exportselection=False)
    listbox_special.place(x=460, y=200)
    for option in special_option:
        listbox_special.insert(END, option)

    def generate_bill_deluxe():
        # Obține selecțiile din Listbox-uri
        selections = get_selected_items(listbox_cheese, listbox_meat, listbox_special)
        cheese = selections["cheese"]
        meat = selections["meat"]
        special = selections["special"]

        # Calculăm numărul total de toppinguri selectate
        total_toppings = len(cheese) + len(meat) + len(special)

        # Verificăm dacă numărul total de toppinguri este exact 5
        if total_toppings != 5:
            messagebox.showwarning("Incomplete Selection", "You must select exactly 5 toppings!")
            return

        # Obține selecțiile din dropdown-uri
        drink = selected_drink.get()
        garnish = selected_garnish.get()
        size_drink = selected_size_drink.get()
        size_garnish = selected_size_garnish.get()

        # Verificăm dacă băutura și garnitura sunt selectate
        if drink == "Select a drink":
            messagebox.showwarning("Incomplete Selection", "Please select a drink!")
            return
        if garnish == "Select a garnish":
            messagebox.showwarning("Incomplete Selection", "Please select a garnish!")
            return
        if size_drink == "Select the drink size":
            messagebox.showwarning("Incomplete Selection", "Please select a drink size!")
            return
        if size_garnish == "Select the garnish size":
            messagebox.showwarning("Incomplete Selection", "Please select a garnish size!")
            return

        # Creăm un obiect MealOrder
        order = MealOrder("Deluxe", drink, garnish)
        burger_price = order.get_burger_price()

        # Adăugăm toppingurile individual, iterând prin liste
        for topping in cheese:
            order.add_burger_toppings(topping)
        for topping in meat:
            order.add_burger_toppings(topping)
        for topping in special:
            order.add_burger_toppings(topping)

        order.set_drink_size(size_drink)
        order.set_side_size(size_garnish)

        # Calculăm totalul
        total_price = order.get_total_price()

        # Actualizăm zona de factură ("Bill Area")
        bill_area.config(state=NORMAL)  # Permitem editarea temporară
        bill_area.delete("1.0", END)  # Ștergem conținutul anterior
        bill_area.insert(END, "       Welcome Customer\n")
        bill_area.insert(END, "       Bill Number: 001\n")
        bill_area.insert(END, "------------------------------\n")
        bill_area.insert(END, "Product               Price\n")
        bill_area.insert(END, "------------------------------\n")

        # Afișăm selecțiile în "Bill Area"
        bill_area.insert(END, f"Deluxe burger:         ${burger_price:.2f}\n")
        for item in cheese:
            if item == "Cheddar":
                bill_area.insert(END, f"{item} :              $0.00\n")
            else:
                bill_area.insert(END, f"{item} :                $0.00\n")

        for item in meat:
            if item == "Ham":
                bill_area.insert(END, f"{item}:                   $0.00\n")
            else:
                bill_area.insert(END, f"{item}:                 $0.00\n")

        for item in special:
            if item == "Avocado":
                bill_area.insert(END, f"{item}:               $0.00\n")
            else:
                bill_area.insert(END, f"{item}:                 $0.00\n")

        if drink != "Select a drink":
            if drink == "Coke":
                bill_area.insert(END, f"{drink} :                 ${order.drink.get_adjusted_price():.2f}\n")
            else:
                pass
        if garnish != "Select a garnish":
            bill_area.insert(END, f"{garnish} :                ${order.side.get_adjusted_price():.2f}\n")

        bill_area.insert(END, "------------------------------\n")
        bill_area.insert(END, f"Total Price:           ${total_price:.2f}\n")
        bill_area.config(state=DISABLED)  # Blochează editarea din nou

    # Butonul "Generate Bill"
    bill_button = Button(
        window,
        text="Generate Bill",
        font=("Arial", 14, "bold"),
        bg=ORANGE,
        fg="black",
        width=15,  # Lățimea butonului
        height=2,  # Înălțimea butonului
        command=generate_bill_deluxe  # Apelează funcția generate_bill
    )
    bill_button.place(x=800, y=385)  # Poziționăm butonul în partea dreaptă jos

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
    bill_area.insert(END, "       Welcome Customer\n")
    bill_area.insert(END, "       Bill Number: 001\n")
    bill_area.insert(END, "------------------------------\n")
    bill_area.insert(END, "Product               Price\n")
    bill_area.insert(END, "------------------------------\n")
    bill_area.config(state=DISABLED)  # Blochează editarea manuală

    # Creăm un Canvas pentru linia verticală
    separator = Canvas(window, width=5, height=600, bg=PALE_ORANGE, highlightthickness=1)
    separator.place(x=670, y=0)  # Poziționăm linia între cele două secțiuni




window.mainloop()

