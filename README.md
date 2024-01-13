# Task Manager 📋

## Project Description
The provided Python script is a simple task management system with user authentication. Users can log in, view tasks, add tasks, edit tasks, mark tasks as complete, and generate reports. The system supports an "admin" user with additional functionalities such as user registration, report generation, and statistical analysis.

## Features 🚀

### User Authentication 🔐

- User credentials are stored in a file (`user.txt`).
- Users need to log in with their username and password.

### Task Management 📝

- Users can add tasks, view all tasks, and view tasks assigned to them.
- Admin users have additional options such as user registration and generating reports.

### Task Editing ✏️

- Users can edit tasks, including changing the assigned user and due date.
- Tasks can be marked as complete.

### User Registration (Admin Only) 🤝

- Admin users can register new users, with username and password stored in the user file.

### Reports and Statistics (Admin Only) 📊

- Admin users can generate reports on task statistics.
- Reports include total tasks, completed tasks, uncompleted tasks, and percentage calculations.
- User-specific statistics are also generated and stored in a separate file.

### Data Persistence 💾

- User data and tasks are stored in text files (`user.txt` and `task.txt`, respectively).
- Reports are generated and saved to text files (`task_overview.txt` and `user_overview.txt`).

## Instructions for Use 📌

### User Authentication

1. Run the script, and it will prompt for a username and password.
2. If the credentials are correct, the user will be logged in.

### Task Management

- Users can add tasks, view tasks, and edit their tasks.
- Admin users have additional options like user registration and generating reports.

### Reports and Statistics (Admin Only)

- Admin users can choose the "Generate Reports" and "Display Statistics" options to view task statistics.
- Reports will be saved to text files (task_overview.txt and user_overview.txt).

### How to run
1. Clone the repository:
  Git clone 
