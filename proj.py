print("=============================")
print("WELCOME TO HAMZI'S CAFE")
print("=============================")

menu = {
    "Pizza": 3500,
    "Burger": 1000,
    "Shawarma": 800,
    "Tea": 150,
    "Coffee": 250,
    "Samosa": 50,
    "Chicken Roll": 80,
    "Cold Drink": 150,
    "Ice-Cream": 250
}

current_order = {}

while True:

    print("\n1. View Menu")
    print("2. Place Order")
    print("3. View Bill")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        print("\n========= MENU =========")
        for item, price in menu.items():
            print(item, "Rs.", price)

    elif choice == 2:

        item_name = input("Enter Item Name: ")

        if item_name in menu:

            quantity = int(input("Enter Quantity: "))

            if item_name in current_order:
                current_order[item_name] += quantity
            else:
                current_order[item_name] = quantity

            print(item_name, "Added Successfully!")

        else:
            print("Item Not Available!")

    elif choice == 3:

        if len(current_order) == 0:
            print("No Order Yet!")

        else:
            print("\n========== BILL ==========")

            total_bill = 0

            for item, quantity in current_order.items():

                price = menu[item]
                item_total = price * quantity

                print(item)
                print("Price    :", price)
                print("Quantity :", quantity)
                print("Total    :", item_total)
                print("------------------------")

                total_bill += item_total

            print("Grand Total = Rs.", total_bill)

    elif choice == 4:

        print("Thank You For Visiting Hamzi's Cafe ❤️")
        break

    else:
        print("Invalid Choice!")