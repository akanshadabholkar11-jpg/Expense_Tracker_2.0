import csv


# Add expense
def add_expense():
    desc = input("Enter expense description: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    month = input("Enter month (YYYY-MM): ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc, amount, category, month])

    print("Expense Added Successfully!")


# View all expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\n----- All Expenses -----")

            for row in reader:

                # skip broken/old rows
                if len(row) != 4:
                    continue

                print(
                    "Item:", row[0],
                    "| Amount: ₹" + row[1],
                    "| Category:", row[2],
                    "| Month:", row[3]
                )

    except FileNotFoundError:
        print("No expenses found!")


# Search by category
def search_category():
    search = input("Enter category to search: ")

    found = False

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\nMatching Expenses:")

            for row in reader:

                if len(row) != 4:
                    continue

                if row[2].lower() == search.lower():

                    print(
                        row[0],
                        "| ₹" + row[1],
                        "|",
                        row[2],
                        "|",
                        row[3]
                    )

                    found = True

            if found == False:
                print("No expenses found!")

    except FileNotFoundError:
        print("No expenses found!")


# Total per category
def total_per_category():

    totals = {}

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) != 4:
                    continue

                if row[1] == "":
                    continue

                category = row[2]
                amount = int(row[1])

                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

        print("\n----- Category Wise Total -----")

        for category in totals:
            print(category, "₹", totals[category])

    except FileNotFoundError:
        print("No expenses found!")
# Monthly total
def monthly_total():

    month = input("Enter month (YYYY-MM): ")

    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if len(row) != 4:
                    continue

                if row[1] == "":
                    continue

                if row[3] == month:
                    total += int(row[1])

        print("\nMonthly Total: ₹", total)

    except FileNotFoundError:
        print("No expenses found!")


# Menu
def menu():

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Total Per Category")
        print("5. Monthly Total")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_category()

        elif choice == "4":
            total_per_category()

        elif choice == "5":
            monthly_total()

        elif choice == "6":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice! Please try again.")
            

menu()
