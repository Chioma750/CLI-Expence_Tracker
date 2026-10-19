def main_menu():
    print("\n==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total")
    print("4. Quit")

    choice = input("Enter a choice from the listed above: ")
    return choice
    #print()

expenses = []

def add_expense():
    description = input("Enter a description: ")

    if not description.strip():
        print("Description cannot be empty")
        return

    try:
        amount = float(input("Enter an amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
        
    expense = {
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print()

    print(expense["description"])
    print(expense["amount"])

def view_expenses():
    if not expenses:
        print("No expenses recorded yet")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(
                f"{number}. {expense['description']} - "
                f"₦{expense['amount']:.2f}"
            )

def show_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print(f"Total: ₦{total:.2f}")

def main():
    while True:
        choice = main_menu()

        if choice == "4":
            print("Quitting...")
            break
        
        elif choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total() 
        else:
            print("Invalid choice, choose from 1, 2, 3 and 4.")


if __name__ == "__main__":
    main()
