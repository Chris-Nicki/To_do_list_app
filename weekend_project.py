# Project Requirements


# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
# ```
# Welcome to the To-Do List App!
#     Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit

#     ```
# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task
# Viewing the list of tasks with from Incomplete and Complete tasks.
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
# User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.
# Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and docstrings for clarity.
# Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.
# Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.
# Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include a link to your GitHub repository in your project documentation.

# Submission

# Submit your project, including all source code files and the README, to your instructor or designated platform.

# Project Tips

# Start by designing a simple user interface and plan the program's structure.
# Test your code frequently as you build each feature to ensure everything works as expected.
# Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!

# By completing this project, you'll gain practical experience in Python programming and have a useful To-Do List Application to help you stay organized in your own life.


# Happy coding! 📋🐍

to_do_list = []
completed_task = []
removed_tasks = []

def add_task(list):
    task= input("What would you like to add to the list? ")
    if task not in list:
        list.append(task)
        print("Task added to list, get after it!")
    else:
        print("We dont have time to do this more than once, get it right!")

def remove_task(list, removed):
    task = input("What would you like to take off the list? ")
    if task in list:
        removed.append(task)
        list.remove(task)
        print("Task removed, lets not make a habit of this!")
    else:
        print("Task not on list, lets get that added!")
def mark_completed(list, completed):
    task = input("What did you crush today?")
    try:
        list.remove(task)
        completed.append(task)
        print("Great job, keep it up!")
    except ValueError:
        print("Whoaaa there buddy! Can't complete things that aren't on the list!")
def view_list(list, completed, remove):
    return f""""Keep going we still need to {list}."
"Great Job! You {completed}, keep up the good work!"
"You removed {remove}, lets not make a habit of this"
"""

def run_app():
    print("""Welcome to the To-Do List App!
     Menu:
     1. Add a task
     2. View tasks
     3. Mark completed
     4. Remove a task
     5. Quit""")
    while True:
        response = input("What would you like to do? ")
        if response == "Add a task":
            add_task(to_do_list)
        elif response == "View tasks":
            print(view_list(to_do_list, completed_task, removed_tasks))
        elif response == "Mark completed":
            mark_completed(to_do_list, completed_task)
        elif response == "Remove a task":
            remove_task(to_do_list, removed_tasks)
        elif response == "Quit":
            print("GREAT JOB WITH YOUR TASKS TODAY!")
            break
        else:
            print("Please enter a valid response")

run_app()
