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
            print("Welcome! Your in Train employee panel")
            print("-------------")
            print(
            "Select the option"
            "1- Add line"
            "2- Update line"
            "3- Delete line"
            "4- Show lines list"
            "5- Add Train"
            "6- Delete Train"
            "7- Show trains list"
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
                self.show_lines_list()
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
        lines_name=input("inter line name :")
        origin=input("enter origin: ")
        destination=input("enter destination: ")
        stations=input("enter stations separated by cammas: ").split(",")
                
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
        
Train_employee("", "")
