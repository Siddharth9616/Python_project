menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

print("Welcome to PYTHON Restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80 ")

order_total = 0

while True:
    item = input("Enter the name of item you want to order = ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Order item {item} is not available yet!")

    another_order = input("Do you want to add another item? (Yes/No) ")
    if another_order.lower() != "yes":
        break

print(f"The total amount of item to pay is {order_total}")