# CONTACT BOOK APPLICATION
def add_contact():#FUNCTION TO ADD CONTACT
    while True:#LOOP TO VALIDATE THE NAME OF CONTACT
        name=input("Enter the name of contact:").strip().lower()
        if name in contacts:
            print("CONTACT ALREADY EXISTS!........\n")
            continue
        if name == "":
            print("NAME CANNOT BE EMPTY!........\n")
            continue
        break
    while True:#LOOP TO VALIDATE THE PHONE NUMBER OF CONTACT
        phone = input(f"Enter the phone number of {name.capitalize()}:")
        if phone == "":
            print("PHONE NUMBER CANNOT BE EMPTY!........\n")
            continue
        if not phone.isdigit():
            print("INVALID PHONE NUMBER!........\n")
            continue
        contacts[name]=phone
        print(f"Contact {name.capitalize()} added successfully!\n")
        break


def view_contacts():#FUNCTION TO VIEW ALL CONTACTS
    if len(contacts) == 0:
        print("NO CONTACTS FOUND!.........\n")
    else:       
        print("CONTACTS:\n")
        for name,phone in contacts.items():
            print(f"{name.capitalize()}: {phone}")


def search_contact():#FUNCTION TO SEARCH FOR A CONTACT
    name=input("ENTER THE NAME OF CONTACT TO SEARCH:").lower().strip()
    if name in contacts:
        print(f"{name.capitalize()}:{contacts[name]}")
    else:
        print("NO CONTACTS FOUND!........\n") 



def update_contact():#FUNCTION TO UPDATE A CONTACT
    name=input("Enter the name of contact to update:").strip().lower()  
    if name in contacts:
      while True:#LOOP TO VALIDATE THE NEW PHONE NUMBER OF CONTACT
        phone=input(f"Enter the new phone number of {name.capitalize()}:")
        if phone == "":#VALIDATION TO CHECK IF THE PHONE NUMBER IS EMPTY
            print("PHONE NUMBER CANNOT BE EMPTY!........\n")
            continue
        if not phone.isdigit():#VALIDATION TO CHECK IF THE PHONE NUMBER CONTAINS ONLY DIGITS
            print("INVALID PHONE NUMBER!........\n")
            continue
        contacts[name]=phone
        print(f"Contact {name.capitalize()} updated successfully!\n")
        break
    else:
        print("NO CONTACTS FOUND!........\n")

def delete_contact():#FUNCTION TO DELETE A CONTACT
    name=input("Enter the name of contact to delete:").strip().lower()
    if name in contacts:#VALIDATION TO CHECK IF THE CONTACT EXISTS
      while True:#LOOP TO CONFIRM THE DELETION OF CONTACT
        confirm=input(f"Are you sure you want to delete {name.capitalize()}? (yes/no):").strip().lower()
        if confirm == "yes":              
            del contacts[name]
            print(f"Contact {name.capitalize()} deleted successfully!\n")
            break
        elif confirm == "no":
            print("Deletion cancelled!........\n")
            break   

    else:
        print("NO CONTACTS FOUND!........\n")        

contacts={}

while True:
    print("-" * 20, "WELCOME TO CONTACT BOOK", "-" * 20)

    print("MAIN MENU")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("-" * 60, "\n")

    try:
        choice = int(input("ENTER YOUR CHOICE (1-6):"))
    except ValueError:
        print("INVALID INPUT! Please enter a number between 1 and 6.\n")
        continue

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("THANK YOU FOR USING CONTACT BOOK!........QUITTING THE PROGRAM...")
        break
    else:
        print("INVALID CHOICE!........PLEASE ENTER A VALID CHOICE (1-6)....\n")