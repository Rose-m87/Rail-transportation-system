from shopping import Shopping
from wallet import Wallet

users = []

def register():
    while True:
        name = input("Name: ").strip()
        if name.lower() == "back": return
        email = input("Email: ").strip()
        if email.lower() == "back": return
        username = input("Username: ").strip()
        if username.lower() == "back": return
        print("password! Must include letters, numbers, and @ or &")
        password = input("Password: ").strip()
        if password.lower() == "back": return

        if '@' not in email or '.' not in email.split('@')[1]:
            print("Invalid email!")
            continue

        has_letter = any(c.isalpha() for c in password)
        has_number = any(c.isdigit() for c in password)
        has_special = any(c in '@&' for c in password)
        if not (has_letter and has_number and has_special):
            print("Invalid password! Must include letters, numbers, and @ or &.")
            continue

        if any(u["username"] == username or u["email"] == email for u in users):
            print("Username or email already exists!")
            continue

        wallet = Wallet()
        users.append({
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "wallet": wallet
        })
        print("Registration successful!")
        return

def login():
    username = input("Username: ").strip()
    print("password! Must include letters, numbers, and @ or &")
    password = input("Password: ").strip()
    for u in users:
        if u["username"] == username and u["password"] == password:
            print(f"Welcome {u['name']}!")
            return u
    print("Wrong username or password!")
    return None

def edit_user_info(user):
    while True:
        print("\nEdit User Info")
        print("1) Change Name")
        print("2) Change Email")
        print("3) Change Password")
        print("4) Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            new_name = input("New name: ").strip()
            if new_name:
                user["name"] = new_name
                print("Name updated!")
        elif choice == "2":
            new_email = input("New email: ").strip()
            if '@' not in new_email or '.' not in new_email.split('@')[1]:
                print("Invalid email!")
                continue
            if any(u["email"] == new_email and u != user for u in users):
                print("Email already exists!")
                continue
            user["email"] = new_email
            print("Email updated!")
        elif choice == "3":
            new_pass = input("New password: ").strip()
            has_letter = any(c.isalpha() for c in new_pass)
            has_number = any(c.isdigit() for c in new_pass)
            has_special = any(c in '@&' for c in new_pass)
            if not (has_letter and has_number and has_special):
                print("Invalid password! Must include letters, numbers, and @ or &.")
                continue
            user["password"] = new_pass
            print("Password updated!")
        elif choice == "4":
            return
        else:
            print("Invalid choice!")

def purchase_panel(user, manager):
    shop = Shopping(manager.trains_dict, user["wallet"], user["username"])

    while True:
        print("\nPurchase Panel")
        print("1) Show Trains")
        print("2) Buy Ticket")
        print("3) Add Balance")
        print("4) Edit Info")
        print("5) Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            shop.show_trains()
        elif choice == "2":
            shop.buy_ticket()
        elif choice == "3":
            amount = float(input("Enter amount to add: ").strip())
            card = input("Card number: ").strip()
            exp_month = input("Exp month: ").strip()
            exp_month = int(exp_month)
            exp_year = input("Exp year: ").strip()
            exp_year = int(exp_year)
            password = input("Card password: ").strip()
            cvv2 = input("CVV2: ").strip()
            user["wallet"].add_balance(amount, card, exp_month, exp_year, password, cvv2)
        elif choice == "4":
            edit_user_info(user)
        elif choice == "5":
            print("Logged out!")
            return
        else:
            print("Invalid choice!")

def user_menu(manager):
    while True:
        print("\nUser Panel")
        print("1) Register")
        print("2) Login")
        print("3) Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                purchase_panel(user, manager)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")