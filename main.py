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
    # Repoziționează butoanele mai sus
    radio_regular.place(x=110, y=65)  # Mută butonul "Regular" mai sus
    radio_deluxe.place(x=430, y=65)  # Mută butonul "Deluxe" mai sus

    show_all_regular()
    menu_button.place_forget()


def set_deluxe():
    # Repoziționează butoanele mai sus
    radio_regular.place(x=110, y=65)  # Mută butonul "Regular" mai sus
    radio_deluxe.place(x=430, y=65)  # Mută butonul "Deluxe" mai sus

    show_all_deluxe()
    menu_button.place_forget()




def show_all_regular():
    canvas1.delete("all")
    canvas2.delete("all")
    menu_button.place_forget()
    window.geometry("1100x450")
    order_regular()

def show_all_deluxe():
    canvas1.delete("all")
    canvas2.delete("all")
    menu_button.place_forget()
    window.geometry("1100x450")
    order_deluxe()


def get_selected_items(listbox_cheese, listbox_meat, listbox_special):
    def clean_selection(selection):

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


def open_menu_window():
    # Creează o nouă fereastră
    menu_window = Toplevel(window)
    menu_window.title("Menu")
    menu_window.geometry("900x500")

    # Creează un canvas pentru a afișa imaginea de fundal
    bg_canvas = Canvas(menu_window, width=900, height=500, highlightthickness=0)
    bg_canvas.pack(fill="both", expand=True)

    # Încarcă imaginea de fundal
    bg_image = PhotoImage(file="background.png")
    bg_canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Adaugă un titlu pentru fereastra meniu
    menu_label = Label(
        menu_window,
        text="Bill's Burger Menu",
        font=("Arial", 24, "bold"),
        bg=ORANGE,
        fg="black",
        pady=10,
        padx=10
    )
    bg_canvas.create_window(375, 50, window=menu_label)

    # Adaugă detalii despre produsele disponibile într-un Label transparent
    menu_content = """
    Welcome to Bill's Burger Menu!

    Regular Burger: $4.00
    Deluxe Burger: $8.50 (includes 5 free toppings)

    Toppings:
    - Cheese: Cheddar ($1.00), Gouda ($1.00)
    - Meat: Bacon ($1.50), Ham ($1.50)
    - Special: Avocado ($1.00), Jalapeños ($1.00)

    Drinks:
    - Coke, Sprite, Water, Orange Juice, Iced Tea ($1.00)

    Garnishes:
    - Fries, Sweet Potato Fries, Coleslaw, Pickles, Onion Rings ($1.50)
    """

    menu_text_label = Label(
        menu_window,
        text=menu_content,
        font=("Courier", 12),
        bg="grey",  # Eliminăm fundalul
        fg="white",
        justify="left",
        wraplength=700
    )
    bg_canvas.create_window(310, 300, window=menu_text_label)

    # Stochează referința imaginii pentru a preveni garbage collection
    menu_window.bg_image = bg_image



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Bill's Burger Order")
window.geometry("650x400")
window.config(bg=YELLOW)
window.grid_rowconfigure(1, minsize=50)


canvas1 = Canvas(window, width=800, height=600, bg=YELLOW, highlightthickness=0)
canvas1.place(x=-180, y=100)

# Încărcăm imaginea
image = PhotoImage(file="regular.png")
canvas1.create_image(325, 200, image=image)



canvas2 = Canvas(window, width=800, height=600, bg=YELLOW, highlightthickness=0)
canvas2.place(x=270, y=100)


icon_image = PhotoImage(file="deluxe.png")
canvas2.create_image(200, 200, image=icon_image)




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
radio_regular.place(x=110,y=170)


radio_deluxe = Radiobutton(
    window,
    text="Deluxe",
    variable=burger_type,
    value="Deluxe",
    font=("Arial", 12,'bold'),
    bg=YELLOW,
    command= set_deluxe
)
radio_deluxe.place(x= 430, y = 170)

menu_button = Button(
    window,
    text="Menu",
    font=("Arial", 14, "bold"),
    bg=ORANGE,
    fg="black",
    width=15,
    height=2,
    command=open_menu_window
)
menu_button.place(x=220, y=70)


def order_regular():


    topping_label = Label(
        text="Select your extra toppings (Optional)",
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
    dropdown_garnish = OptionMenu(window, selected_garnish, "Fries", "Sweet Potato Fries", "Coleslaw", "Potato Wedges",
                                  "Onion Rings")
    dropdown_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_garnish.place(x=380, y=330)


    selected_size_drink = StringVar()
    selected_size_drink.set("Select a drink size")
    dropdown_size_drink = OptionMenu(window, selected_size_drink, "SMALL", "MEDIUM", "LARGE")
    dropdown_size_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_size_drink.place(x=30 ,y= 370)

    selected_size_garnish = StringVar()
    selected_size_garnish.set("Select a garnish size")
    dropdown_size_garnish = OptionMenu(window, selected_size_garnish, "SMALL", "MEDIUM", "LARGE")
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
            elif item == "Jalapeños":
                bill_area.insert(END, f"{item}:             $0.00\n")

        if drink != "Select a drink":
            if drink == "Coke":
                bill_area.insert(END, f"{drink} :                 ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Sprite":
                bill_area.insert(END, f"{drink} :               ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Water":
                bill_area.insert(END, f"{drink} :                ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Orange Juice":
                bill_area.insert(END, f"{drink} :         ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Iced Tea":
                bill_area.insert(END, f"{drink} :             ${order.drink.get_adjusted_price():.2f}\n")

        if garnish != "Select a garnish":
            if garnish == "Sweet Potato Fries":
                bill_area.insert(END, f"{garnish} :   ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Fries":
                bill_area.insert(END, f"{garnish} :                ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Coleslaw":
                bill_area.insert(END, f"{garnish} :             ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Potato Wedges":
                bill_area.insert(END, f"{garnish} :        ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Onion Rings":
                bill_area.insert(END, f"{garnish} :          ${order.side.get_adjusted_price():.2f}\n")

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
        text="Select your extra toppings (5 FREE)",
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
    dropdown_garnish = OptionMenu(window, selected_garnish, "Fries", "Sweet Potato Fries", "Coleslaw", "Potato Wedges",
                                  "Onion Rings")
    dropdown_garnish.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_garnish.place(x=380, y=330)

    selected_size_drink = StringVar()
    selected_size_drink.set("Select a drink size")
    dropdown_size_drink = OptionMenu(window, selected_size_drink, "SMALL", "MEDIUM", "LARGE")
    dropdown_size_drink.config(font=("Arial", 12), bg=ORANGE, width=20)
    dropdown_size_drink.place(x=30, y=370)

    selected_size_garnish = StringVar()
    selected_size_garnish.set("Select a garnish size")
    dropdown_size_garnish = OptionMenu(window, selected_size_garnish, "SMALL", "MEDIUM", "LARGE")
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


        if total_toppings < 5:
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

        number = 0
        for item in cheese:

            if item == "Cheddar":
                bill_area.insert(END, f"{item} :              ${order.burger.get_topping_price(item,number)}\n")
                number +=1
            else:
                bill_area.insert(END, f"{item} :                ${order.burger.get_topping_price(item,number)}\n")
                number +=1


        for item in meat:
            if item == "Ham":
                bill_area.insert(END, f"{item}:                   ${order.burger.get_topping_price(item,number)}\n")
                number +=1

            else:
                bill_area.insert(END, f"{item}:                 ${order.burger.get_topping_price(item,number)}\n")
                number +=1


        for item in special:
            if item == "Avocado":
                bill_area.insert(END, f"{item}:               ${order.burger.get_topping_price(item,number)}\n")
                number +=1

            elif item == "Jalapeños":
                bill_area.insert(END, f"{item}:             ${order.burger.get_topping_price(item,number)}\n")
                number +=1


        if drink != "Select a drink":
            if drink == "Coke":
                bill_area.insert(END, f"{drink} :                 ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Sprite":
                bill_area.insert(END, f"{drink} :               ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Water":
                bill_area.insert(END, f"{drink} :                ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Orange Juice":
                bill_area.insert(END, f"{drink} :         ${order.drink.get_adjusted_price():.2f}\n")
            elif drink == "Iced Tea":
                bill_area.insert(END, f"{drink} :             ${order.drink.get_adjusted_price():.2f}\n")





        if garnish != "Select a garnish":
            if garnish == "Sweet Potato Fries":
                bill_area.insert(END, f"{garnish} :   ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Fries":
                bill_area.insert(END, f"{garnish} :                ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Coleslaw":
                bill_area.insert(END, f"{garnish} :             ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Potato Wedges":
                bill_area.insert(END, f"{garnish} :        ${order.side.get_adjusted_price():.2f}\n")
            elif garnish == "Onion Rings":
                bill_area.insert(END, f"{garnish} :          ${order.side.get_adjusted_price():.2f}\n")




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

