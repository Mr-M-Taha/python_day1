def main():
    print("""Shopping Cart Menu:
    1. Add item
    2. Remove item
    3. Update quantity
    4. View cart
    5. Checkout
    6. Exit""")
    choice = input("Choose an option: ").strip()
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("❌ Invalid choice. Please enter again...")
        choice = input("Choose an option: ").strip()
    match choice:
        case "1":
            name = input("entre item name: ")
            price = float(input("entre item's price: "))
            quantity = int(input("enter quantity: "))
        case "2":
            remove_item(i)
        # case "3":

        case "4":
            view_cart()
        # case "5":

        # case "6":
        #     pass


cart = []


def add_item(name, price, quantity):
    cart.append(
        {
            name: {"price": price, "qty": quantity},
        }
    )


def remove_item(index):
    cart.pop(index)


def update_qty():
    pass


def view_cart():
    for item in cart:
        print(item["name"])


main()
