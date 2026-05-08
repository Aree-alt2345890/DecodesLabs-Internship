import json

# File name for storage
FILE_NAME = "tasks.json"

# Load existing data from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data to file (Persistence)
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add new task (INSERT INTO)
def add_task(tasks):
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    status = input("Enter Status (Pending/Done): ")

    task = {
        "id": task_id,        # Primary Key
        "title": title,
        "status": status
    }

    tasks.append(task)       # INSERT INTO
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks (SELECT *)
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

# Search task by ID
def search_task(tasks):
    search_id = input("Enter Task ID to search: ")
    for task in tasks:
        if task["id"] == search_id:
            print("Task Found:", task)
            return
    print("Task not found.")

# Main program
tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        search_task(tasks)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
    # Expense Tracker

print("=== Expense Tracker ===")

total = 0  # Accumulator to store total expenses

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == 'done':
        break

    try:
        amount = float(expense)   # Convert input to number
        total = total + amount    # Accumulation logic
        print("Added! Current Total:", total)
    except:
        print("Invalid input! Please enter a valid number.")

print("\nFinal Total Spent:", total)
print("Thank you for using Expense Tracker!")
