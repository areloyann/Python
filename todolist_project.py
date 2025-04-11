import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("\nEnter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Bye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()