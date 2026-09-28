# 1) Build a program that:
# • Displays a list of snacks and drinks with item numbers and prices.
# • Ask the user to choose items by number in a loop.
# • Keeps track of selected items and their prices.
# • Ends when the user types "done".
# • Finally prints a receipt showing: List of selected items with prices and total cost

menu = [
    {"id": 1, "name": "Chips", "price": 1.50, "category": "Snack"},
    {"id": 2, "name": "Cookies", "price": 2.00, "category": "Snack"},
    {"id": 3, "name": "Soda", "price": 2.50, "category": "Drink"},
    {"id": 4, "name": "Juice", "price": 3.00, "category": "Drink"},
]

selected_items = []
total_cost = 0.0

print("Welcome to the Snack Bar!")
print("Menu:")
for item in menu:
    print(f"{item['id']}. {item['name']} ({item['category']}) - ${item['price']:.2f}")

while True:
    choice = input("Choose an item by number or type 'done' to finish: ").strip().lower()

    if choice == "done":
        break

    if not choice.isdigit():
        print("Invalid input. Please enter a valid item number or 'done'.")
        continue

    item_number = int(choice)
    selected_item = next((item for item in menu if item["id"] == item_number), None)

    if selected_item is None:
        print("That item number does not exist. Please choose a valid option.")
        continue

    selected_items.append(selected_item)
    total_cost += selected_item["price"]
    print(f"Added {selected_item['name']} for ${selected_item['price']:.2f}.")

print("\nReceipt")
print("---------")

if not selected_items:
    print("No items were selected.")
else:
    for item in selected_items:
        print(f"{item['name']} - ${item['price']:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
