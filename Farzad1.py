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
        print("---Add line section---")
        print("--To return to the panel, press 0.--")
        print("-Press 1 to continue.-")
        login_sec = input()
        for choice in login_sec:
            if login_sec != "0" or login_sec != "1":
                return
            if login_sec == "0":
                return TrainEmployeePanel()
            elif login_sec == "1":
                continue

        lines_name=input("Enter line name :")
        origin=input("Enter origin: ")
        destination=input("Enter destination: ")
        stations=input("Enter stations separated by cammas: ").split(",")
        #exit add line = 0        
        if lines_name=="":
            return
        if origin=="":
            return
        if destination=="":
            return
        if not stations:
            return
        for line in self.lines_list:
            if line[0]==lines_name:
                print("This name exists, enter another name")
                return

        line_record=[lines_name,origin,destination,stations]
        self.lines_list.append(line_record)
        print(f"line'{lines_name}'added successfully")
        return TrainEmployeePanel()

        #حذف خط

    def delete_line(self):
        print("---Delete line section---")
        print("-For back to panel: Enter 0")
        delete_line_name = input("Enter line name: ")
        if delete_line_name=="":
            return
        elif delete_line_name == "0":
            return TrainEmployeePanel()
        for line in self.lines_list:
            if line[0]==delete_line_name:
                print("--Your chosen line is available.--")
                continue
            else:
                print("--The line you selected does not exist.--")
        if delete_line_name in self.lines_list:
            self.lines_list.remove(delete_line_name)
            print("--Your selected line has been deleted.--")
            return TrainEmployeePanel()
        elif delete_line_name == "0":
            return TrainEmployeePanel()
        
        # مشاهده لیست خطوط

    def view_line_list(self):
        for item in self.lines_list:
            print(item)
        return TrainEmployeePanel()
