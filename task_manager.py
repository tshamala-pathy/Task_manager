import datetime
import os

# Read user datas from a file and store it in a dictionary for efficient lookup.
user_data = {}  # Store usernames and passwords
with open("user.txt", 'r') as file:
    for line in file:
        username, password = line.strip().split(', ')
        user_data[username] = password

# Initialize the logged-in user name.
logged_in_user = None

# Define the main function to manage the program's flow.
def main():
    global logged_in_user
    print("LOGIN")

    # Login loop to authenticate users.
    while True:
        user_name = input("Please enter your username:")
        user_password = input("Please enter your password:")

        if user_name in user_data and user_data[user_name] == user_password:
            print("Login successful.")
            print()
            logged_in_user = user_name  # Set the logged-in user
            break
        print("Sorry! Your username and password do not match. Please try again.")

    # Main menu loop for user interaction.
    while True:
        if logged_in_user == "admin":
            menu = input('''Select one of the following options:
r - Register a user
a - Add task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit
:''').lower()  # Convert user input to lowercase for easier comparison
        else:
            menu = input('''Select one of the following options:
a - Add task
va - View all tasks
vm - View my tasks
e - Exit
:''').lower()

        # Handle user menu choices based on input.
        if menu == 'r' and logged_in_user == "admin":
            register_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks()
        elif menu == 'gr' and logged_in_user == "admin":
            generate_reports()
        elif menu == 'ds' and logged_in_user == "admin":
            display_statistics()
        elif menu == 'e':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select a valid option.")

# Function to register a new user.
def register_user():
    new_username = input("Enter a new username:")
    new_password = input("Enter a new password:")
    confirm_password = input("Please confirm your password: ")

    if new_username in user_data:
        print("Username already exists. Please try another.")
        print()
    elif new_password == confirm_password:
        with open("user.txt", 'a') as file:
            file.write(f"\n{new_username}, {new_password}")
        # Update the user_data dictionary with the new user
        user_data[new_username] = new_password
        print("User registered successfully!")
    else:
        print("Passwords do not match. User registration failed.")

# Function to add a new task.
def add_task():
    assigned = input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task:")
    task_description = input("Enter the description of the task:")
    due_date = input("Enter the due date of the task (e.g. 09 Oct 2023):")
    current_date = datetime.datetime.now().strftime("%d %b %Y")

    with open("task.txt", 'a') as task_file:
        task_file.write(f"\n{assigned}, {task_title}, {task_description}, {due_date}, {current_date}, No")

    print("Task added successfully")

# Function to view all tasks.
def view_all_tasks():
    with open("task.txt", 'r') as task_file:
        for line in task_file:
            temp = line.strip().split(', ')
            print(f"Assigned: {temp[0]}")
            print(f"Task Title: {temp[1]}")
            print(f"Task Description: {temp[2]}")
            print(f"Due Date: {temp[3]}")
            print(f"Current Date: {temp[4]}")
            print(f"Status: {temp[5]}\n")

# Function to view tasks assigned to the logged-in user.
def view_my_tasks():
    tasks = []
    with open("task.txt", 'r') as task_file:
        tasks = task_file.readlines()

    print(f"Hello {logged_in_user}!")
    print("Here are your tasks:")
    for i, task in enumerate(tasks):
        temp2 = task.strip().split(', ')
        if temp2[0] == logged_in_user:
            print(f"{i + 1}. Assigned: {temp2[0]}, Task Title: {temp2[1]}, Due Date: {temp2[3]}, Status: {temp2[5]}")

    print()
    print("0. Cancel")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Edit a task")
    print("4. Mark a task as complete")
    print()

    choice = input("Please enter your choice:")

    if choice == "0":
        return
    elif choice == "1":
        add_task()
    elif choice == "2":
        remove_task(tasks)
    elif choice == "3":
        edit_task(tasks)
    elif choice == "4":
        mark_task_as_complete(tasks)
    else:
        print("You have entered an invalid input.")

# Function to edit a task.
def edit_task(tasks):
    task_number = input("Enter the number of the task you want to edit: ")

    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks) and tasks[task_number - 1].startswith(logged_in_user):
            assigned, task_title, task_description, due_date, current_date, status = tasks[task_number - 1].strip().split(', ')

            if status == "No":
                print("Editing options:")
                print("1. Edit the username of the person the task is assigned to")
                print("2. Edit the due date of the task")
                print("3. Cancel")

                edit_choice = input("Enter your choice: ")

                if edit_choice == "1":
                    new_assigned = input("Enter the new username for the task: ")
                    tasks[task_number - 1] = f"{new_assigned}, {task_title}, {task_description}, {due_date}, {current_date}, {status}\n"
                    with open("task.txt", 'w') as file:
                        file.writelines(tasks)
                    print("Task updated successfully.")
                elif edit_choice == "2":
                    new_due_date = input("Enter the new due date for the task (e.g., 09 Oct 2023): ")
                    tasks[task_number - 1] = f"{assigned}, {task_title}, {task_description}, {new_due_date}, {current_date}, {status}\n"
                    with open("task.txt", 'w') as file:
                        file.writelines(tasks)
                    print("Task updated successfully.")
                elif edit_choice == "3":
                    print("Task edit canceled.")
                else:
                    print("Invalid choice. Task edit canceled.")
            else:
                print("Task cannot be edited as it is marked as complete.")
        else:
            print("Invalid task number. Please enter a valid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to mark a task as complete.
def mark_task_as_complete(tasks):
    task_number = input("Enter the number of the task you want to mark as complete: ")

    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks) and tasks[task_number - 1].startswith(logged_in_user):
            assigned, task_title, task_description, due_date, current_date, status = tasks[task_number - 1].strip().split(', ')

            if status == "No":
                tasks[task_number - 1] = f"{assigned}, {task_title}, {task_description}, {due_date}, {current_date}, Yes\n"
                with open("task.txt", 'w') as file:
                    file.writelines(tasks)
                print("Task marked as complete.")
            else:
                print("Task is already marked as complete.")
        else:
            print("Invalid task number. Please enter a valid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to generate reports.
def generate_reports():
    tasks = []

    # Initialize variables for statistics
    total_tasks = 0
    total_tasks_completed = 0
    total_tasks_uncompleted = 0
    total_tasks_overdue_uncompleted = 0

    # Calculate statistics from task data
    with open("task.txt", 'r') as task_file:
        for line in task_file:
            task = line.strip().split(', ')
            
            assigned = task[0]
            due_date = task[3]
            status = task[5]
            
            due_date = datetime.datetime.strptime(due_date, "%d %b %Y")
            current_date = datetime.datetime.now()
            
            tasks.append({
                'assigned': assigned,
                'status': status,
                'due_date': due_date,
                'current_date': current_date
            })

            total_tasks += 1

            if status == "Yes":
                total_tasks_completed += 1
            else:
                total_tasks_uncompleted += 1

            if current_date > due_date and status == "No":
                total_tasks_overdue_uncompleted += 1

    # Calculate percentages
    uncompleted_tasks_percentage = (total_tasks_uncompleted / total_tasks) * 100
    overdue_task_percentage = (total_tasks_overdue_uncompleted / total_tasks) * 100

    with open("task_overview.txt", 'w') as task_overview_file:
        task_overview_file.write(f"Total Tasks generated: {total_tasks}\n")
        task_overview_file.write(f"Total Tasks Completed: {total_tasks_completed}\n")
        task_overview_file.write(f"Total tasks Uncompleted: {total_tasks_uncompleted}\n")
        task_overview_file.write(f"Total Tasks Overdue Uncompleted: {total_tasks_overdue_uncompleted}\n")
        task_overview_file.write(f"Uncompleted Task Percentage: {uncompleted_tasks_percentage:.2f}%\n")
        task_overview_file.write(f"Overdue Task Percentage: {overdue_task_percentage:.2f}%\n")

    # Now, let's calculate user-specific statistics
    user_task_counts = {}  # Dictionary to store task counts for each user

    for task in tasks:
        assigned_user = task['assigned']
        status = task['status']

        if assigned_user not in user_task_counts:
            user_task_counts[assigned_user ] = {
                'total_tasks_assigned': 0,
                'total_tasks_completed': 0,
                'total_tasks_uncompleted': 0,
                'total_tasks_overdue_uncompleted': 0
            }

        user_task_counts[assigned_user]['total_tasks_assigned'] += 1

        if status == "Yes":
            user_task_counts[assigned_user]['total_tasks_completed'] += 1
        else:
            user_task_counts[assigned_user]['total_tasks_uncompleted'] += 1

        if task['current_date'] > task['due_date'] and status == "No":
            user_task_counts[assigned_user]['total_tasks_overdue_uncompleted'] += 1

    # Write user-specific statistics to a file
    with open("user_overview.txt", 'w') as user_file:
        total_users = len(user_data)
        user_file.write(f"Total users: {total_users}\n")
        user_file.write(f"Total tasks: {total_tasks}\n")

        for username, stats in user_task_counts.items():
            total_tasks_assigned = stats['total_tasks_assigned']
            total_tasks_completed = stats['total_tasks_completed']
            total_tasks_uncompleted = stats['total_tasks_uncompleted']
            total_tasks_overdue_uncompleted = stats['total_tasks_overdue_uncompleted']

            total_task_assigned_percentage = (total_tasks_assigned / total_tasks) * 100
            task_completed_percentage = (total_tasks_completed / total_tasks_assigned) * 100
            task_uncompleted_percentage = (total_tasks_uncompleted / total_tasks_assigned) * 100
            task_overdue_uncompleted_percentage = (total_tasks_overdue_uncompleted / total_tasks_assigned) * 100

            user_file.write(f"\nUser: {username}\n")
            user_file.write(f"Total task assigned: {total_tasks_assigned}\n")
            user_file.write(f"Total task assigned percentage: {total_task_assigned_percentage:.2f}%\n")
            user_file.write(f"Task completed percentage: {task_completed_percentage:.2f}%\n")
            user_file.write(f"Task uncompleted percentage: {task_uncompleted_percentage:.2f}%\n")
            user_file.write(f"Percentage Overdue_uncompleted Tasks: {task_overdue_uncompleted_percentage:.2f}%\n")

    print("Reports generated successfully.")


# Function to display statistics.
def display_statistics():
    
    task_overview_filename = "task_overview.txt"
    user_overview_filename = "user_overview.txt"

    # Check if the reports exist and generate them if they don't
    if not os.path.exists(task_overview_filename) or not os.path.exists(user_overview_filename):
        generate_reports()

    with open(task_overview_filename, 'r') as task_overview_file:
        task_overview = task_overview_file.read()
    with open(user_overview_filename, 'r') as user_overview_file:
        user_overview = user_overview_file.read()

    print("Task Overview:")
    print(task_overview)
    print("\nUser Overview:")
    print(user_overview)

# Function to remove a task.
def remove_task(tasks):
    while True:
        print(f"Hello {logged_in_user}!")
        print("Here are your tasks:")
        for i, task in enumerate(tasks):
            temp4 = task.strip().split(', ')
            if temp4[0] == logged_in_user:
                print(f"{i + 1}. Assigned: {temp4[0]}, Task Title: {temp4[1]}, Due Date: {temp4[3]}, Status: {temp4[5]}")

        print("0. Cancel")
        task_number = input("Please enter the number of the task you want to remove: ")

        if task_number == "0":
            break

        try:
            task_number = int(task_number)
            if 1 <= task_number <= len(tasks) and tasks[task_number - 1].startswith(logged_in_user):
                removed_task = tasks.pop(task_number - 1)
                with open("task.txt", 'w') as task_file:
                    task_file.writelines(tasks)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

# Entry point of the program.
if __name__ == "__main__":
    main()

