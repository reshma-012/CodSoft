# To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    show_tasks()
    task_no = int(input("Enter task number to update: ")) - 1
    if 0 <= task_no < len(tasks):
        new_task = input("Enter updated task: ")
        tasks[task_no] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        removed = tasks.pop(task_no)
        print(f"Task '{removed}' deleted successfully!")
    else:
        print("Invalid task number!")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")