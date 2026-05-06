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
