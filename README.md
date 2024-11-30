# 🍔 Bill's Burger Ordering System

**Bill's Burger Ordering System** is a desktop application that allows users to customize and order burgers along with sides and drinks. Designed with **Object-Oriented Programming (OOP)** principles, this project showcases modularity, clean code structure, and a dynamic user interface built with **Tkinter**.

---

## 🌟 Features
- 🥪 **Burger Customization**: Choose between Regular and Deluxe burgers, and select toppings, sides, and drinks.
- 🛠️ **Dynamic Pricing**: The total price updates in real-time based on user selections.
- 🧾 **Bill Generation**: A detailed breakdown of the order, including itemized costs, is displayed in the bill area.
- ✅ **Input Validation**: Ensures all required selections are made before generating the bill.
- 💻 **Interactive GUI**: A clean and user-friendly interface for a seamless ordering experience.

---

## 📸 Screenshot
### Main Menu
![Main Menu](screenshots/main_menu.png)  

### Regular/Deluxe Ordering
![Ordering Screen](screenshots/ordering_screen.png)  

---

## 🚀 Getting Started
Follow these steps to set up and run the application locally.

### ✅ Prerequisites
- **Python** (version 3.x)
- **Tkinter** (comes pre-installed with Python)

### 🛠️ Installation
1. **Clone the repository**: `git clone https://github.com/RuginaAlex/BillsBurger.git`
2. **Navigate into the project directory**: `cd BillsBurger`
3. **Run the application**: `python main.py`

---

## 🎮 How to Use
1. **Main Menu**:
   - Choose between **Regular** and **Deluxe** burgers using the radio buttons.
2. **Customization**:
   - Select toppings (optional for Regular, free for Deluxe up to 5).
   - Choose a side and drink, along with their sizes.
3. **Generate Bill**:
   - Click the "Generate Bill" button to see the breakdown of your order.
4. **Start Over**:
   - Restart the application to place a new order.

---

## 🛠️ Code Structure
This application is built using **Object-Oriented Programming (OOP)** to ensure modularity and scalability.
- **`Item` Class** (`Item.py`): Represents individual items like toppings, sides, and drinks, handling their properties and sizes.
- **`Burger` Class** (`Burger.py`): Manages the type of burger, pricing, and toppings.
- **`DeluxeBurger` Class** (`DeluxeBurger.py`): Extends the `Burger` class to include free toppings and additional restrictions.
- **`MealOrder` Class** (`MealOrder.py`): Orchestrates the entire order, combining the burger, side, and drink, and calculates the total price.
- **Tkinter Main Script** (`main.py`): Handles the GUI and integrates all classes.

---

## 📜 Development History

### 1️⃣ Initial Setup
The initial version focused on creating the basic structure for a single burger type and displaying it in a text-based interface.

---

### 2️⃣ Adding a Graphical Interface
The application was transformed into a GUI using **Tkinter**, providing a visually appealing way for users to interact with the ordering system.

---

### 3️⃣ Toppings and Dynamic Pricing
Functionality for selecting toppings and dynamically updating the total price was added, making the ordering process more interactive.

---

### 4️⃣ Input Validation and Final Bill
Implemented validation to ensure all required inputs are selected before generating the bill, along with a detailed itemized receipt.

---

## 📚 Key Concepts Demonstrated
- **Object-Oriented Programming (OOP)**: Organized code into reusable and independent classes.
- **Encapsulation**: Each class encapsulates specific functionalities and properties.
- **Event-Driven Programming**: Handled button clicks and user input dynamically with Tkinter.

---

## 🤝 Contributions

Contributions are welcome! If you encounter any issues or have ideas for new features, feel free to open an issue or submit a pull request. 

If you use this code, a simple credit or mention would be greatly appreciated. Thank you for supporting open-source projects!
