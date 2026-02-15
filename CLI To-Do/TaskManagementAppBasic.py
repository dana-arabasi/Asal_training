def main():
    tasks = []
    task_id = 0

    
    while True:
        print("\nWhat do you want to do?")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Remove a task")
        print("4. Mark Task as Completed / Pending")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            add_task(tasks, task_id)
            task_id += 1

        elif choice == 2:
            list_tasks(tasks)

        elif choice == 3:
            remove_task(tasks)

        elif choice == 4:
            toggle_task_status(tasks)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")

def add_task(tasks, task_id):
    title = input("Enter your task's title: ")
    description = input("Enter your task's description: ")
    tasks.append({
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    })
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "completed" if task["completed"] else "pending"
        print(f'{task["id"]}: {task["title"]} - {task["description"]} [{status}]')


def remove_task(tasks):
    try:
        task_id = int(input("Enter task ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task removed.")
            return
    print("Task not found.")


def toggle_task_status(tasks):
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            print("Task status updated.")
            return
    print("Task not found.")

if __name__ == "__main__":
    main()
