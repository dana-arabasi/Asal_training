def main():
    id = 0
    mts = TasksManagement()
    factory = TaskFactory()
    while True:
        print("\nWhat do you want to do?")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                title = input("Enter your task's title: ")
                description = input("Enter your task's description: ")
                task = factory.create_task(id, title, description)
                mts.addTask(task)
                id += 1
            case 2:
                mts.listTasks()
            case 3:
                task_id = int(input("Enter your task's id: "))
                mts.removeTask(task_id)
            case 4:
                print("Exiting...")
                exit()
            case _:
                print("Invalid choice, try again.")


class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


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

    def addTask(self, task):
        self.__task.append(task)

    def listTasks(self):
        if not self.__task:
            print("No tasks available.")
        for task in self.__task:
            print(f"{task.id}: {task.title} - {task.description}")

    def removeTask(self, id):
        for task in self.__task:
            if task.id == id:
                self.__task.remove(task)
                print(f"Task {id} removed.")
                return
        print(f"No task found with id {id}.")


if __name__ == '__main__':
    main()
