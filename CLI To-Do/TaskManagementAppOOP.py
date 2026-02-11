def main():
    id = 0
    mts = TasksManagement()
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
                task = Task(id, title, description)
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

class TasksManagement:
    def __init__(self):
        self.__task = []

    def addTask(self, task):
        self.__task.append(Task(task.id, task.title, task.description))

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
