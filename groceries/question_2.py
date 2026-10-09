# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user “add” items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.


groceries = {
    1: {"name": "apple", "price": 1.50},
    2: {"name": "banana", "price": 0.75},
    3: {"name": "orange", "price": 2.00}
}

cart = {}

while True:
    print("\nAvailable Groceries:")
    for item_id, details in groceries.items():
        print(f"{item_id}. {details['name'].capitalize()} - ${details['price']:.2f}")

    choice = input("\nEnter item ID or 'checkout': ").strip().lower()

    if choice == "checkout":
        break

    if not choice.isdigit() or int(choice) not in groceries:
        print("Invalid item ID. Please try again.")
        continue

    item_id = int(choice)

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                continue

            break
        except ValueError:
            print("Please enter a valid integer.")

    if item_id in cart:
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

# Display final bill
print("\n--- Final Bill ---")

total = 0

for item_id, quantity in cart.items():
    name = groceries[item_id]["name"]
    price = groceries[item_id]["price"]
    subtotal = price * quantity

    print(
        f"{name.capitalize()}: {quantity} x "
        f"${price:.2f} = ${subtotal:.2f}"
    )

    total += subtotal

print(f"\nTotal: ${total:.2f}")
print("Thank you for shopping with us!")
