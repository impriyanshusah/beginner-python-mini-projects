def printMenu():
    print("\nTo-Do List menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")


def getChoice():
    while True:
        choice = input("Enter your choice (1-4): ")
        validChoices = ["1", "2", "3", "4"]
        if choice in validChoices:
            return choice
        else:
            print("Invalid Choice.Please try again.")
            continue


def viewTasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return

    for index, tasks in enumerate(tasks, start=1):
        print(f"{index}. {tasks}")


def addTask(tasks):
    while True:
        task = input("\nEnter the task to add: ").strip()
        if task != "":
            tasks.append(task)
            break
        else:
            print("\nTask cannot be empty. Please try again.")
            continue


def removeTask(tasks):
    viewTasks(tasks)

    while True:
        try:
            taskNumber = int(input("Enter the task number to remove: "))
            if 1 <= taskNumber <= len(tasks):
                tasks.pop(taskNumber - 1)
                break
            else:
                raise ValueError

        except ValueError:
            print("Invalid task number. Please try again.")


def main():
    tasks = []
    while True:
        printMenu()
        choice = getChoice()
        if choice == "1":
            print("\nYour current tasks are:")
            viewTasks(tasks)
        elif choice == "2":
            addTask(tasks)
        elif choice == "3":
            print("\nYour current tasks are:")
            removeTask(tasks)
        elif choice == "4":
            print("\nExiting the program.")
            exit(0)
        else:
            continue


if __name__ == "__main__":
    main()
