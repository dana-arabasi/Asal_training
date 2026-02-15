def main():
    task_id_counter = 0
    manager = TasksManagement()

    
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

        match choice:
            case 1:
                title = input("Enter your task's title: ")
                description = input("Enter your task's description: ")
                task = Task(task_id_counter, title, description)
                manager.add_task(task)
                task_id_counter += 1
                print("Task added.")

            case 2:
                manager.list_tasks()

            case 3:
                try:
                    task_id = int(input("Enter your task's id: "))
                    manager.remove_task(task_id)
                except ValueError:
                    print("Invalid ID.")

            case 4:
                try:
                    task_id = int(input("Enter your task's id: "))
                    manager.toggle_task_status(task_id)
                except ValueError:
                    print("Invalid ID.")

            case 5:
                print("Exiting...")
                break

            case _:
                print("Invalid choice, try again.")

class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def toggle_status(self):
        self.completed = not self.completed


class TasksManagement:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "completed" if task.completed else "pending"
            print(f"{task.id}: {task.title} - {task.description} [{status}]")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} removed.")
                return
        print("Task not found.")

    def toggle_task_status(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.toggle_status()
                print("Task status updated.")
                return
        print("Task not found.")

if __name__ == '__main__':
    main()
