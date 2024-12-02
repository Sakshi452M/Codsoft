import datetime

# To-Do List Storage
tasks = []

# Function to Display the Tasks
def show_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} (Priority: {task['priority']}, Due: {task['deadline']})")

# Function to Add a Task
def add_task():
    task = input("\nEnter the task: ").strip()
    priority = input("Enter priority (low, medium, high): ").strip().lower()
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
    
    # Validate date
    try:
        datetime.datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks.append({"task": task, "priority": priority, "deadline": deadline})
    print("Task added successfully!")

# Function to Update a Task
def update_task():
    show_tasks()
    if not tasks:
        return

    task_number = int(input("\nEnter the task number to update: "))
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_number - 1]
    print(f"Updating task: {task['task']}")
    task['task'] = input("Enter the new task description: ").strip()
    task['priority'] = input("Enter the new priority (low, medium, high): ").strip().lower()
    task['deadline'] = input("Enter the new deadline (YYYY-MM-DD): ").strip()
    print("Task updated successfully!")

# Function to Delete a Task
def delete_task():
    show_tasks()
    if not tasks:
        return

    task_number = int(input("\nEnter the task number to delete: "))
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    tasks.pop(task_number - 1)
    print("Task deleted successfully!")

# Main Menu
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
