def expense_tracker():
    expenses = []
    while True:
        print("\nExpense Tracker Menu")
        print("1, Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Exit")


        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter expense item: ")
            amount = float(input("Enter amount: "))
            expenses.append((item, amount))
            print(f"Added: {item} - ${amount:.2f}")
        elif choice == "2":
            if not expenses:
                print("No expenses recorded.")
            else:
                for item, amount in expenses:
                    print(f"{item}: ${amount:.2f}")
        elif choice == "3":
            total = sum(amount for _, amount in expenses)
            print(f"Total Expenses: ${total:.2f}")
        elif choice == "4":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    expense_tracker()