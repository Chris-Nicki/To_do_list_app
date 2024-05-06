# To Do List Application

"""In this project, you will apply your Python programming skills to create a functional To-Do List 
Application from scratch. The objective of this project is to reinforce your understanding of Python 
syntax, data types, control structures, functions, and error handling while building a practical and 
interactive application.
"""

# below creates lists
to_do_list = [] 
completed_task = [] 
removed_tasks = []

# define functions for each interaction that a task can have with the list 
""" use if and else statements to either complete the interaction or guide the user to enter an 
appropriate response
"""
# .append will add input to the appropriate parameter
# .remove will remove input from appropriate parameter
# try will try to do the appropriate action, except if an unrecognized input is given
# ValueError will give an error code if the user gives an unrecognized user input
# another set of if elif is introduced to take input and guide the user appropriately

def add_task(list):
    task= input("What would you like to add to the list? ").lower()
    if task not in list: 
        list.append(task)
        print("Task added to list, get after it!")
    else:
        print("We dont have time to do this more than once, get it right!")
def remove_task(list, removed):
    task = input("What would you like to take off the list? ").lower()
    if task in list:
        removed.append(task)
        list.remove(task)
        print("Task removed, lets not make a habit of this!")
    else:
       print("Task not on list, we can not remove that which does not exist.")
    
def mark_completed(list, completed):
    task = input("What did you crush today? ").lower()
    try:
        list.remove(task)
        completed.append(task)
        print("Great job, keep it up!")
    except ValueError:
        response = input("Whoaaa there buddy! The task wasn't on your list are you sure you did this? ").lower()
        if response == "yes":
                completed.append(task)
                print("Way to go above and beyond!")
        elif response == "no":
                print("May be next weekend...")
def view_list(list, completed, remove):
    return f""""Keep going we still need to {list}."
"Great Job! You completed {completed}, keep up the good work!"
"You removed {remove}, lets not make a habit of this."
"""
# The below function runs all the above functions based off of user input of what they would like to do
# print will print the text in menu being the guide for the application
# while True will keep that application running until the user selects quit, because it is followed with break
""" if and elif guide user responses to navigate the application and use user input to complete the 
appropriate action within application.
"""
# else will force the user to give an appropriate response if a prompt from the menu is not entered
# Using the if and elif create a user input to complete the functions
# run_app() calls the above function and runs it
def run_app():
    print("Welcome to the To-Do List App!")
    print()
    while True:
        response = input("""What would you like to do?
    1. Add a task
    2. View tasks
    3. Mark completed
    4. Remove a task
    5. Quit
                         
    I would like to """).lower()
        if response == "1":
            add_task(to_do_list)
            print()
        elif response == "2":
            print(view_list(to_do_list, completed_task, removed_tasks))
            print()
        elif response == "3":
            mark_completed(to_do_list, completed_task)
            print()
        elif response == "4":
            remove_task(to_do_list, removed_tasks)
            print()
        elif response == "5":
            print("GREAT JOB WITH YOUR TASKS TODAY!")
            print()
            break
        else:
            print("Please enter a valid response")
            print()
run_app()
