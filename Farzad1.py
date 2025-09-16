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
                self.Train_employee_panel()
                break
            #elif برای بازگشت به پنل شروع
            else:
                print("Wrong username or password. Try again.")

    class Train_employee_panel:
        def __init__(self,add_line,update_line,delete_line,show_lines_list,add_train,delete_train,show_trains_list,):
            self.add_line = add_line
            self.update_line = update_line
            self.delete_line = delete_line
            self.show_lines_list = show_lines_list
            self.add_train = add_train
            self.delete_train = delete_train
            self.show_trains_list = show_trains_list
           
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
            "8- Exit"
            )
            print("-------------------")
            
            while True:
                choice = input("Please enter your option: ")
                if choice == "1":
                    self.add_line()
                    break
                elif choice == "2":
                    self.Update_line()
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
        
        class Update_line:
            def __init__(self,):