employees = []

ADMIN_USER = "Train_Admin"
ADMIN_PASS = "Train_Pass"

def admin_login():
    while True:
        print("\nAdmin Login (type 'back' to return)")
        username = input("Enter admin username: ").strip()
        if username.lower() == "back":
            return
        password = input("Enter admin password: ").strip()
        if password.lower() == "back":
            return
        if username == ADMIN_USER and password == ADMIN_PASS:
            print(f"Welcome {ADMIN_USER}!")
            admin_panel()
            return
        else:
            print("Wrong username or password!")

def add_employee():
    while True:
        print("\nAdd Employee (type 'back' to return)")
        name = input("Name: ").strip()
        if name.lower() == "back":
            return
        family = input("Family: ").strip()
        if family.lower() == "back":
            return
        email = input("Email: ").strip()
        if email.lower() == "back":
            return
        username = input("Username: ").strip()
        if username.lower() == "back":
            return
        print("password! Must include letters, numbers, and @ or &")
        password = input("Password: ").strip()
        if password.lower() == "back":
            return

        if '@' not in email or '.' not in email.split('@')[1]:
            print("Invalid email! Must include '@' and domain.")
            continue

        has_letter = any(c.isalpha() for c in password)
        has_number = any(c.isdigit() for c in password)
        has_special = any(c in '@&' for c in password)
        if not (has_letter and has_number and has_special):
            print("Invalid password! Must include letters, numbers, and @ or &.")
            continue

        if any(e["username"] == username or e["email"] == email for e in employees):
            print("Username or email already exists!")
            continue

        employees.append({
            "name": name,
            "family": family,
            "email": email,
            "username": username,
            "password": password
        })
        print(f"Employee '{name} {family}' added successfully!")
        return

def delete_employee():
    while True:
        print("\nDelete Employee (type 'back' to return)")
        username = input("Username to delete: ").strip()
        if username.lower() == "back":
            return
        for e in employees:
            if e["username"] == username:
                employees.remove(e)
                print(f"Employee '{username}' deleted successfully!")
                return
        print("Employee not found!")

def view_employees():
    print("\nEmployees List")
    if not employees:
        print("No employees found.")
    else:
        for e in employees:
            print(e)
    input("Press Enter to return.")

def admin_panel():
    while True:
        print("\nAdmin Panel")
        print("1) Add Employee")
        print("2) Delete Employee")
        print("3) View Employees")
        print("4) Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            print("Logging out...")
            return
        else:
            print("Invalid choice!")