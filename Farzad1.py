class Train_employee:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #Admin User and pass
        print("Hi!")
        print("------")

        while True:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

            if username == "Farzad" and password == "1234": #Admin user and pass
                self.panel = TrainEmployeePanel()
                self.panel.show_menu()
                break
            #elif برای بازگشت به پنل شروع
            else:
                print("Wrong username or password. Try again.")

class TrainEmployeePanel:
    def __init__(self):
        self.lines_list = []
        self.trains_list = []
    
    def show_menu(self):
        while True:
            print("\nWelcome! Your in Train employee panel")
            print("-------------")
            print(
            "\nSelect the option"
            "1- Add line\n"
            "2- Update line\n"
            "3- Delete line\n"
            "4- View lines list\n"
            "5- Add Train\n"
            "6- Delete Train\n"
            "7- Show trains list\n"
            "8- Exit")
            print("-------------------")
                    
            choice = input("Please enter your option: ")
            if choice == "1":
                self.add_line()
            elif choice == "2":
                self.update_line()
                break
            elif choice == "3":
                self.delete_line()
                break
            elif choice == "4":
                self.view_line_list()
                break
            elif choice == "5":
                self.add_train()
                break
            elif choice == "6":
                self.delete_train()
                break
            elif choice == "7":
                self.show_trains_list()
                break
            #elif choice == "8":
                #return #پنل شروع
            else:
                print("Wrong choice, try again.")
                return
    def add_line(self):
        print("\n---Add line section---")

        line_name=input("Enter line name (or 0 to go panel): ")
        if line_name == "0":
            return
        origin=input("Enter origin: ")
        destination=input("Enter destination: ")
        stations=input("Enter stations separated by cammas: ").split(",")
        #exit add line = 0        
        if not line_name or not origin or not destination or not stations:
            print("Invalid input")
            return
        
        for line in self.lines_list:
            if line[0]==line_name:
                print("This name exists, enter another name")
                return

        line_record=[line_name,origin,destination,stations]
        self.lines_list.append(line_record)
        print(f"line'{line_name}'added successfully")
    

        #حذف خط

    def delete_line(self):
        print("\n---Delete line section---")
        delete_line_name = input("Enter line name to delete (or 0 to go panel): ")
        if delete_line_name == "0":
            return
        
        for line in self.lines_list:
            if line[0] == delete_line_name:
            self.lines_list.remove(line)
            print(f"Line '{delete_line_name}' deleted successfully!")
            return
        print("Line not found")
        
        # مشاهده لیست خطوط

    def view_line_list(self):
        print("\n--- Lines List ---")
        if not self.lines_list:
            print("No Lines available.")
            return
        for line in self.lines_list:
            print(line)
