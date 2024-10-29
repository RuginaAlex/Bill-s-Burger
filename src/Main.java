public class Main {
    public static void main(String[] args) {
        Burger burger = new Burger("regular",4.00);
        burger.addToppings("Bacon","CHEESE", "MAYO");
        burger.printItem();
    }
}
