from admin_panel import admin_login
from train_panel import RailwayManager
from train_menu_panel import TrainEmployeePanel
from user_panel import user_menu

railway_manager = RailwayManager()

while True:
    print("\n--- Start Menu ---")
    print("1) Chief Admin")
    print("2) Train Employee")
    print("3) Normal User")
    print("4) Exit")

    choice = input("Please select an option (1-4): ").strip()

    if choice == "1":
        print("\nEntering Admin Panel...")
        admin_login()
        print("\nReturning to Start Menu...")
    elif choice == "2":
        print("\nEntering Train Employee Panel...")
        train_panel = TrainEmployeePanel()
        train_panel.manager = railway_manager
        train_panel.show_menu()
        print("\nReturning to Start Menu...")
    elif choice == "3":
        print("\nEntering User Panel...")
        user_menu(railway_manager)
        print("\nReturning to Start Menu...")
    elif choice == "4":
        print("\nGoodbye! The program has been closed.")
        break
    else:
        print("Invalid option! Please enter a number between 1 and 4.")