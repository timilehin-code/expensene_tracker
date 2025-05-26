import random
random_number = random.randint(0, 100)
print(random_number)
# expense tracker
# creating a list for expensese
expenses = []

# function to display menu
def menu():
    print("\n ===== expense tracker menu =====")
    print("1. add a new expense")
    print("2. view all expenses")
    print("3.show expense summary")
    print("4.save and exit")


# function to add new expenses and details


def add_expense():
    try:
        amount = float(input("Enter the amount: NGN"))
        category = input("enter category e.g'internet,rent,cloth'")
        description = input("enter a short description")
        expenses_details = {
            "amount": amount,
            "category": category,
            "description": description,
        }
        expenses.append(expenses_details)
        print("expenses added successfully!")
    except ValueError:
        print("please enter a valid amount of the item")


def display_expense():
    if not expenses:
        print("no expense added yet")
        return
    print("\n===== all expenses=====")
    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. NGN{expense['amount']} - {expense['category']} - {expense['description']}"
        )


def expense_summary():
    if not expenses:
        print("no expense added yet")
        return
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary["category"] = summary.get(category, 0) + expense["amount"]
    print("\n====== expensence summmary by category======")
    for category, total in summary.items():
        print(f"{category} - NGN{total:.2F}")


def save_expense():
    name = input("enter your name:")
    with open(f"c:/Users/HP/Downloads/{name}-expenses{random_number}.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"NGN{expense['amount']}, {expense['category']}, {expense['description']}\n"
            )
    print("expense saved sucessfully")


while True:
    menu()
    choice = input("choose option (1-4):")
    if choice == "1":
        add_expense()
    elif choice == "2":
        display_expense()
    elif choice == "3":
        expense_summary()
    elif choice == "4":
        save_expense()
        print("thanks for using our service!")
    else:
        print("wrong input!")
