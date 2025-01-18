import json
from datetime import datetime

# File to store tasks
task_file = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low/Medium/High): ")
    
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {task['status']}\n")

# Update an existing task
def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            print("Leave fields blank to keep the current value.")
            title = input(f"New title ({task['title']}): ") or task['title']
            description = input(f"New description ({task['description']}): ") or task['description']
            due_date = input(f"New due date ({task['due_date']}): ") or task['due_date']
            priority = input(f"New priority ({task['priority']}): ") or task['priority']
            status = input(f"New status ({task['status']}): ") or task['status']

            task.update({
                "title": title,
                "description": description,
                "due_date": due_date,
                "priority": priority,
                "status": status
            })
            save_tasks(tasks)
            print("Task updated successfully!\n")
            return

    print("Task not found.\n")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!\n")
            return

    print("Task not found.\n")

# Mark a task as completed
def mark_completed(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!\n")
            return

    print("Task not found.\n")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
