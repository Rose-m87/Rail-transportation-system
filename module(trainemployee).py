#Rose , Behesht , Farzad

#Delete line 3
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

#View lines list 4
def view_line_list(self):
        print("\n--- Lines List ---")
        if not self.lines_list:
            print("No Lines available.")
            return
        for line in self.lines_list:
            print(line)

#Delete train 6
def delete_train(self):
        print("\n---Delete Train section---")
        delete_train_name = input("Enter train name to delete (or 0 to go panel): ")
        if delete_train_name == "0":
            return
        
        for train in self.trains_list:
            if train[0] == delete_train_name:
                self.trains_list.remove(train)
                print(f"Train '{delete_train_name}' deleted successfully!")
                return
        print("Train not found")

#Show trains list 7
def show_trains_list(self):
        print("\n--- Trains List ---")
        if not self.trains_list:
            print("No Trains available.")
            return
        for Train in self.trains_list:
            print(f"Train: {train[0]}, Line: {train[1]}")