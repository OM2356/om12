# To-Do List using Dictionary with Status
todo_list = {}
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")
def add_task():
    task = input("Enter task description: ")
    if task in todo_list:
        print("Task already exists.")
    else:
        todo_list[task] = "Pending"
        print("Task added successfully!")
def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, (task, status) in enumerate(todo_list.items(), 1):
            print(f"{i}. {task} - [{status}]")
def mark_done():
    view_tasks()
    task_name = input("Enter the task to mark as done: ")
    if task_name in todo_list:
        todo_list[task_name] = "Done"
        print("Task marked as done.")
    else:
        print("Task not found.")
def remove_task():
    view_tasks()
    task_name = input("Enter the task to remove: ")
    if task_name in todo_list:
        del todo_list[task_name]
        print("Task removed.")
    else:
        print("Task not found.")
# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
