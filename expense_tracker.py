# expense_tracker.py
import sys

expenses = []

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    print("Expense added successfully.\n")

def view_expenses():
    if not expenses:
        print("\nNo expenses recorded.\n")
    else:
        print("\n--- All Expenses ---")
        for idx, exp in enumerate(expenses, start=1):
            print(f"{idx}. Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']:.2f} | Desc: {exp['description']}")
        print()

def total_by_category():
    print("\n--- Total by Category ---")
    category = input("Enter category: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total spent on '{category}': ${total:.2f}\n")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        idx = int(input("Enter entry number to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            print(f"Deleted expense: {removed}")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
