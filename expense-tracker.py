total = 0
print("Expense Tracker")
print("Enter your expenses one by one. Type 'quit' to stop.")
while True:
    entry=input("Enter expense amount: ")
    if entry=="quit":
        break
    try:
        expense=int(entry)
        total=total+expense
        print("Added. Running total:", total)
    except ValueError:
        print("Invalid input! Please enter a number.")
print("Total Spent:", total)
