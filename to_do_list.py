
def add_task():
    task = input("Enter the task you want to add:")
    to_do_list.append(task)
    print("Task added successfully!")



def view_task():
    if len(to_do_list) == 0:
        print("No pending tasks in the list......")
    else:
        print("Tasks in the list:")
        for index,task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")



def remove_task():
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

def mark_task_completed():  
    if len(to_do_list) == 0:
        print("No pending tasks in the list......")
        return
    view_task()
    try:      
        task_number = int(input("Enter the task number you want to mark as completed:"))
        if 1 <= task_number <= len(to_do_list):
            completed_task = to_do_list.pop(task_number - 1)
            print(f"Task '{completed_task}' has been marked as completed and removed from the list.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid task number.")  

    print("Task marked as completed successfully!")

    
to_do_list=[]


while True:
 print("-"*5,"WELCOME TO THE TO DO LIST APPLICATION!","-"*5)
 print("SELCT THE OPTION YOU WANT TO PERFORM:")

 print("1. Add a Task")
 print("2. View Tasks")
 print("3. Remove a Task")
 print("4. Mark a Task as Completed")
 print("5. Exit")
 print("-"*50)
 
 choice=int(input("Enter your choice (1-5):").strip())
 
 if choice==1:
     add_task()
 elif choice==2:
     view_task()
 elif choice==3:
     remove_task()
 elif choice==4:
     mark_task_completed()
 elif choice==5:
     print("Exiting application.")
     break
 else:
     print("Please enter a valid choice (1-5).")


