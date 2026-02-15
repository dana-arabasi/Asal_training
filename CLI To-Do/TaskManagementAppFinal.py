def main():
    task_id_counter = 0
    mts = TasksManagement()
    factory = TaskFactory()


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
                task = factory.create_task(task_id_counter, title, description)
                mts.add_task(task)
                task_id_counter += 1
                print("Task added.")

            case 2:
                mts.list_tasks()

            case 3:
                try:
                    task_id = int(input("Enter your task's id: "))
                    mts.remove_task(task_id)
                except ValueError:
                    print("Invalid ID.")

            case 4:
                try:
                    task_id = int(input("Enter your task's id: "))
                    mts.toggle_task_status(task_id)
                except ValueError:
                    print("Invalid ID.")

            case 5:
                print("Exiting...")
                break

            case _:
                print("Invalid choice, try again.")


class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def toggle_status(self):
        self.completed = not self.completed


class TaskFactory:
    def create_task(self, id, title, description):
        return Task(id, title, description)


class TasksManagement:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__task = []
        return cls._instance

    def add_task(self, task):
        self.__task.append(task)

    def list_tasks(self):
        if not self.__task:
            print("No tasks available.")
            return

        for task in self.__task:
            status = "completed" if task.completed else "pending"
            print(f"{task.id}: {task.title} - {task.description} [{status}]")

    def remove_task(self, id):
        for task in self.__task:
            if task.id == id:
                self.__task.remove(task)
                print(f"Task {id} removed.")
                return
        print(f"No task found with id {id}.")

    def toggle_task_status(self, task_id):
        for task in self.__task:
            if task.id == task_id:
                task.toggle_status()
                print("Task status updated.")
                return
        print("Task not found.")


if __name__ == '__main__':
    main()
