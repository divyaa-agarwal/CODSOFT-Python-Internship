
# To-Do List Application
# This application allows users to manage their tasks by adding, viewing, removing, and marking tasks as completed.
def add_task():# Function to add a task to the to-do list
    task = input("Enter the task you want to add:")
    to_do_list.append(task)
    print("Task added successfully!")



def view_task():# Function to view all tasks in the to-do list
    if len(to_do_list) == 0:
        print("No pending tasks in the list......")
    else:
        print("Tasks in the list:")
        for index,task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")



def remove_task():# Function to remove a task from the to-do list
    if len(to_do_list) == 0:
        print("No pending tasks in the list......")
        return
    view_task()
    try:
        task_number = int(input("Enter the task number you want to remove:"))
        if 1 <= task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number - 1)
            print(f"Task '{removed_task}' has been removed from the list.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid task number.")
    
    print("Task removed successfully!")

def mark_task_completed(): # Function to mark a task as completed and remove it from the to-do list
    if len(to_do_list) == 0:
        print("No pending tasks in the list......")
        return
    view_task()
    try: # Get the task number from the user and validate it
        task_number = int(input("Enter the task number you want to mark as completed:"))
        if 1 <= task_number <= len(to_do_list):
            completed_task = to_do_list.pop(task_number - 1)
            print(f"Task '{completed_task}' has been marked as completed and removed from the list.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:# Handle the case where the user input is not a valid integer
        print("Please enter a valid task number.")  

    print("Task marked as completed successfully!")

    
to_do_list=[]# Initialize an empty list to store the tasks

# Main loop to display the menu and perform actions based on user input
while True:
 print("-"*5,"WELCOME TO THE TO DO LIST APPLICATION!","-"*5)
 print("SELCT THE OPTION YOU WANT TO PERFORM:")

# Display the menu options to the user
 print("1. Add a Task")
 print("2. View Tasks")
 print("3. Remove a Task")
 print("4. Mark a Task as Completed")
 print("5. Exit")
 print("-"*50)
 
 # Get the user's choice and validate it
 choice=int(input("Enter your choice (1-5):").strip())
 
 if choice==1:
     add_task()# Call the function to add a task to the to-do list
 elif choice==2:
     view_task()# Call the function to view all tasks in the to-do list
 elif choice==3:
     remove_task()# Call the function to remove a task from the to-do list
 elif choice==4:
     mark_task_completed()# Call the function to mark a task as completed and remove it from the to-do list
 elif choice==5:
     print("Exiting application.")# Exit the application
     break
 else:
     print("Please enter a valid choice (1-5).")# Handle the case where the user input is not a valid choice



