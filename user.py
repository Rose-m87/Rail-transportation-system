user = []


def register():
    print('\nRegister')
    name = input('Enter your name:')
    email = input('Enter your email:')
    username = input ('Enter your username:')
    password = input('Enter your password:')

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
        return
    elif not email_ok:
        print('Invalid email! Must have @ and a domain with .')
        return
    elif not password_ok:
        print('Invalid password! Must include English letters, numbers, and @ or &.')
        return
     
    for u in user: 
        if u['username'] == username or u['email'] == email:
            print('Username or email already exsist!')
            return
        
    user.append({'name': name, 'email': email, 'username': username, 'password': password})  
    print('Registration successful!')  

def login():
    print('\nLogin')
    username = input('Ente your username:')
    password = input('Enter your password:')

    for u in user:
        if u ['username'] == username and u['password'] == password: 
            print(f"Welcome {u['name']}! Login succesful.")
            return
    print('Wrong username or password')

while True: 
    print('\n1) Register')
    print('2) Login')
    print('3) Back to start menu')
    choice = input('choose:')
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice =='3':
        break
    else: 
        print('Invalid choice')