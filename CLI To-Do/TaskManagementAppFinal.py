def main():
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
                title = input("Enter your task's title: ").strip()
                if not title:
                    print("Task title cannot be empty.")
                    continue

                description = input("Enter your task's description: ").strip()
                task = factory.create_task(title, description)
                mts.add_task(task)

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
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def toggle_status(self):
        self.completed = not self.completed

    def status_text(self):
        return "Completed" if self.completed else "Pending"


class TaskFactory:
    def __init__(self):
        self._task_id_counter = 0

    def create_task(self, title, description):
        task = Task(self._task_id_counter, title, description)
        self._task_id_counter += 1
        return task


class TasksManagement:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__tasks = []
        return cls._instance

    def add_task(self, task):
        for existing_task in self.__tasks:
            if existing_task.id == task.id:
                print("Task with this ID already exists.")
                return

        self.__tasks.append(task)
        print("Task added.")

    def list_tasks(self):
        if not self.__tasks:
            print("No tasks available.")
            return

        for task in self.__tasks:
            print(
                f"{task.id}: {task.title} - {task.description} "
                f"[{task.status_text()}]"
            )

    def remove_task(self, task_id):
        for task in self.__tasks:
            if task.id == task_id:
                self.__tasks.remove(task)
                print(f"Task {task_id} removed.")
                return

        print(f"No task found with id {task_id}.")

    def toggle_task_status(self, task_id):
        for task in self.__tasks:
            if task.id == task_id:
                task.toggle_status()
                print(
                    f"Task {task_id} marked as {task.status_text()}."
                )
                return

        print("Task not found.")


if __name__ == '__main__':
    main()
