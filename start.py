while True:
    print("\nStart Menu")
    print("1) Chief Admin")
    print("   - Description: Full system management, adding/deleting employees, viewing employee list.")
    print("2) Train Employee")
    print("   - Description: Access to the employee panel for managing tasks and train schedules.")
    print("3) Normal User")
    print("   - Description: Registration, login, ticket purchasing, and editing personal information.")
    print("4) Exit")
    print("   - Description: Close the program and exit the system.")

    choice = input("Please select an option (1-4): ").strip()
    
    if choice == "1":
        print("\nYou selected Chief Admin!")
        print("This section includes full system management, adding/deleting employees, and viewing employee list.")
    elif choice == "2":
        print("\nYou selected Train Employee!")
        print("This section provides access to the employee panel for managing tasks and train schedules.")
    elif choice == "3":
        print("\nYou selected Normal User!")
        print("This section includes registration, login, ticket purchasing, and editing personal information.")
    elif choice == "4":
        print("\nGoodbye! The program has been closed.")
        break
    else:
        print("\nInvalid option! Please enter a number between 1 and 4.")