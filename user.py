user = []

def register():
    while True:
        print('\nRegister')
        print('Type "back" anytime to return to menu')
        name = input('Enter your name (or "back"): ')
        if name.lower() == 'back':
            return
        
        email = input('Enter your email (or "back"): ')
        if email.lower() == 'back':
            return
            
        username = input('Enter your username (or "back"): ')
        if username.lower() == 'back':
            return
        
        password = input('Enter your password (or "back"): ')
        if password.lower() == 'back':
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
     
        username_exists = False
        email_exists = False
        for u in user:
            if u['username'] == username:
                username_exists = True
            if u['email'] == email:
                email_exists = True
        
        error_messages = []
        if username_exists:
            error_messages.append('Username already exists! Please choose another.')
        if email_exists:
            error_messages.append('Email already exists! Please use another email.')
        
        if error_messages:
            print('\nErrors:')
            for msg in error_messages:
                print(msg)
            continue
        
        user.append({'name': name, 'email': email, 'username': username, 'password': password, 'wallet': 0})  
        print('Registration successful!')  
        break

def login():
    while True:
        print('\nLogin')
        print('Type "back" anytime to return to menu')
        username = input('Enter your username (or "back"): ')
        if username.lower() == 'back':
            return
        
        password = input('Enter your password (or "back"): ')
        if password.lower() == 'back':
            return

        for u in user:
            if u['username'] == username and u['password'] == password: 
                print(f"Welcome {u['name']}! Login successful.")
                return u['username']
        print('Wrong username or password')
        back_choice = input('Try again or type "back" to return: ').strip().lower()
        if back_choice == 'back':
            return None

def edit_user_info(username):
    user_info = None
    for u in user:
        if u['username'] == username:
            user_info = u
            break
    
    if not user_info:
        print("User not found!")
        return
    
    while True:
        print("\nCurrent Information")
        print(f"Name: {user_info['name']}")
        print(f"Email: {user_info['email']}")
        print(f"Username: {user_info['username']} (Cannot be changed)")
        print(f"Wallet: {user_info['wallet']}")
        
        print("\nEdit Options")
        print("1. Change Name")
        print("2. Change Email")
        print("3. Change Password")
        print("4. Back to Purchase Panel")
        
        choice = input("Choose option: ").strip()
        
        if choice == '1':
            new_name = input("Enter new name (or press Enter to cancel): ").strip()
            if new_name:
                user_info['name'] = new_name
                print(f"Name changed to: {new_name}")
            else:
                print("Name change cancelled.")
                
        elif choice == '2':
            new_email = input("Enter new email (or press Enter to cancel): ").strip()
            if new_email:
                if '@' not in new_email:
                    print('Invalid email! Must have @ and a domain with .')
                    continue
                parts = new_email.split('@')
                if len(parts) != 2 or '.' not in parts[1]:
                    print('Invalid email! Must have @ and a domain with .')
                    continue
                
                email_exists = False
                for u in user:
                    if u['email'] == new_email and u['username'] != username:
                        email_exists = True
                        break
                
                if email_exists:
                    print('This email is already registered!')
                    continue
                
                user_info['email'] = new_email
                print(f"Email changed to: {new_email}")
            else:
                print("Email change cancelled.")
                
        elif choice == '3':
            new_password = input("Enter new password (or press Enter to cancel): ").strip()
            if new_password:
                has_letter = False
                has_number = False
                has_special = False
                
                for char in new_password:
                    if char.isalpha():
                        has_letter = True
                    elif char.isdigit():
                        has_number = True
                    elif char in '@&':
                        has_special = True
                
                if not (has_letter and has_number and has_special):
                    print('Invalid password! Must include English letters, numbers, and @ or &.')
                    continue
                
                user_info['password'] = new_password
                print("Password changed successfully!")
            else:
                print("Password change cancelled.")
                
        elif choice == '4':
            print("\nUpdated Information")
            print(f"Name: {user_info['name']}")
            print(f"Email: {user_info['email']}")
            print(f"Username: {user_info['username']}")
            print(f"Wallet: {user_info['wallet']}")
            print("Returning to Purchase Panel...")
            return
        
        else:
            print("Invalid choice! Please try again.")

def purchase_panel(username):
    while True:
        print("\nPurchase Panel")
        print("1. Buy Ticket")
        print("2. Edit User Information")
        print("3. Logout")
        choice = input("Choose: ").strip()
        
        if choice == '1':
            print("Buy ticket")
        elif choice == '2':
            edit_user_info(username)
        elif choice == '3':
            print("Logged out successfully!")
            return
        else:
            print("Invalid choice!")

while True: 
    print('\nUser Panel')
    print('1) Register')
    print('2) Login')
    print('3) Back to start menu')
    choice = input('choose:')
    if choice == '1':
        register()
    elif choice == '2':
        logged_in_user = login()
        if logged_in_user:
            purchase_panel(logged_in_user)
    elif choice =='3':
        break
    else: 
        print('Invalid choice')
