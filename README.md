#===== Importing Libraries =====
from datetime import datetime

# Function to load users from user.txt
def load_users():
    users = {}
    with open("user.txt", "r") as user_file:
        for line in user_file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users

# Function to check login
def login(users):
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("\nLogin successful!")
            return username  # Return logged-in username
        else:
            print("Invalid username or password. Try again.")

# Function to register a new user (only admin can do this)
def register_user(users):
    if current_user != "admin":
        print("Only admin can register new users.")
        return

    new_username = input("Enter new username: ")
    if new_username in users:
        print("Username already exists.")
        return

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        with open("user.txt", "a") as user_file:
            user_file.write(f"{new_username}, {new_password}\n")
        print("User registered successfully!")
    else:
        print("Passwords do not match.")

# Function to add a task
def add_task():
    task_user = input("Enter username to assign task to: ")
    task_title = input("Enter task title: ")
    task_desc = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    assigned_date = datetime.today().strftime("%Y-%m-%d")  # Current date
    completion_status = "No"

    with open("tasks.txt", "a") as task_file:
        task_file.write(f"{task_user}, {task_title}, {task_desc}, {assigned_date}, {due_date}, {completion_status}\n")

    print("Task added successfully!")

# Function to display all tasks
def view_all_tasks():
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()

    for task in tasks:
        task_data = task.strip().split(", ")
        print(f"\nAssigned To: {task_data[0]}")
        print(f"Title: {task_data[1]}")
        print(f"Description: {task_data[2]}")
        print(f"Assigned Date: {task_data[3]}")
        print(f"Due Date: {task_data[4]}")
        print(f"Completed: {task_data[5]}")
        print("-" * 40)

# Function to display tasks assigned to current user
def view_my_tasks(username):
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()

    for task in tasks:
        task_data = task.strip().split(", ")
        if task_data[0] == username:  # Check if task belongs to current user
            print(f"\nTitle: {task_data[1]}")
            print(f"Description: {task_data[2]}")
            print(f"Assigned Date: {task_data[3]}")
            print(f"Due Date: {task_data[4]}")
            print(f"Completed: {task_data[5]}")
            print("-" * 40)

# Function to display statistics (only for admin)
def display_statistics():
    if current_user != "admin":
        print("Only admin can view statistics.")
        return

    with open("user.txt", "r") as user_file:
        total_users = sum(1 for _ in user_file)

    with open("tasks.txt", "r") as task_file:
        total_tasks = sum(1 for _ in task_file)

    print(f"\nTotal Users: {total_users}")
    print(f"Total Tasks: {total_tasks}")

#===== Main Program =====
users = load_users()  # Load user data
current_user = login(users)  # Login user

while True:
    print("\nMenu:")
    print("r - Register a user")
    print("a - Add task")
    print("va - View all tasks")
    print("vm - View my tasks")
    if current_user == "admin":
        print("s - View statistics")
    print("e - Exit")

    menu_choice = input("\nChoose an option: ").lower()

    if menu_choice == "r":
        register_user(users)
    elif menu_choice == "a":
        add_task()
    elif menu_choice == "va":
        view_all_tasks()
    elif menu_choice == "vm":
        view_my_tasks(current_user)
    elif menu_choice == "s" and current_user == "admin":
        display_statistics()
    elif menu_choice == "e":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
