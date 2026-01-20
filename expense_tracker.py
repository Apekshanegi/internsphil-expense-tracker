import csv


def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    file = open("expenses.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow([amount, category, description])
    file.close()

    print("Expense saved successfully")


def view_expenses():
    file = open("expenses.csv", "r")
    reader = csv.reader(file)

    print("\nYour Expenses:")
    for row in reader:
        print(row)

    file.close()


def main():
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting program")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
