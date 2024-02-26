def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("To-Do List:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("No tasks found")
    except FileNotFoundError:
        print("Error: No file found")

def delete_task(task_index):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for idx, task in enumerate(tasks, start=1):
                if idx != task_index:
                    file.write(task)
        print("Task deleted successfully!")
    except FileNotFoundError:
        print("No tasks found!")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()