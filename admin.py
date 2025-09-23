employees = []

ADMIN_USER = "Train_Admin"
ADMIN_PASS = "Train_Pass"

def admin_login():
    while True:
        print("\nAdmin Login")
        print("Enter 'back' anytime to return to Start Menu")
        username = input("Enter admin username: ").strip()
        if username.lower() == "back":
            return
        password = input("Enter admin password: ").strip()
        if password.lower() == "back":
            return
        if username == ADMIN_USER and password == ADMIN_PASS:
            print("Welcome Admin!")
            admin_panel()
            return
        else:
            print("Wrong username or password!")

def add_employee():
    while True:
        print("\nAdd Employee")
        print("Enter 'back' anytime to return to Admin Panel")
        name = input("Enter name: ").strip()
        if name.lower() == "back":
            return
        family = input("Enter family: ").strip()
        if family.lower() == "back":
            return
        email = input("Enter email: ").strip()
        if email.lower() == "back":
            return
        username = input("Enter username: ").strip()
        if username.lower() == "back":
            return
        password = input("Enter password: ").strip()
        if password.lower() == "back":
            return
        if '@' not in email:
            email_ok = False  
        else:
            parts = email.split('@')
            domain = parts[1] 
            email_ok = '.' in domain
        has_letter = False
        has_number = False
        has_special = False
        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True
            elif char in '@&':
                has_special = True
        password_ok = has_letter and has_number and has_special
        if not email_ok and not password_ok:
            print('Errors:')
            print('Invalid email! Must have @ and a domain with .')
            print('Invalid password! Must include English letters, numbers, and @ or &.')
            continue
        elif not email_ok:
            print('Invalid email! Must have @ and a domain with .')
            continue
        elif not password_ok:
            print('Invalid password! Must include English letters, numbers, and @ or &.')
            continue
        for e in employees:
            if e["username"] == username or e["email"] == email:
                print("Username or email already exists!")
                break
        else:
            employees.append({"name": name, "family": family, "email": email, "username": username, "password": password})
            print("Employee added successfully!")
            return

def delete_employee():
    while True:
        print("\nDelete Employee")
        print("Enter 'back' anytime to return to Admin Menu")
        username = input("Enter username to delete: ").strip()
        if username.lower() == "back":
            return
        for e in employees:
            if e["username"] == username:
                employees.remove(e)
                print("Employee deleted successfully!")
                return
        print("Employee not found!")

def view_employees():
    while True:
        print("\nEmployees List")
        if not employees:
            print("No employees found.")
        else:
            for e in employees:
                print(e)
        choice = input("Type 'back' to return: ").strip()
        if choice.lower() == "back":
            return

def admin_panel():
    while True:
        print("\nAdmin Panel")
        print("1) Add Employee")
        print("2) Delete Employee")
        print("3) View Employees")
        print("4) Logout to Start Menu")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            print("Back to Start Menu")
            return
        else:
            print("Invalid choice!")

while True:
    admin_login()
    if input("Press 'back' to return to Start Menu or any key to continue: ").lower() == "back":
        break