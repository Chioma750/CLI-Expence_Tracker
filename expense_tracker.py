def main_menu():
    print("\n==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total")
    print("4. Quit")

    choice = input("Enter a choice from the listed above: ")
    return choice
    print()

expenses = []
def add_expense():
    description = input("Enter a description: ")
    amount = input("Enter an amount: ")
    amount = float(amount)

    expense = {
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print()

    print(expense["description"])
    print(expense["amount"])

add_expense()
add_expense()
print(expenses)

def main():
    while True:
        choice = main_menu()

        if choice == "4":
            print("Quitting...")
            break
        
        elif choice == "1":
            add_expense()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice, choose from 1, 2, 3 and 4.")


if __name__ == "__main__":
    main()
