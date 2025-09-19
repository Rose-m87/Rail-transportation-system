#Rose , Behesht , Farzad

#Add line 1
def add_line(self, lines_name, origin, destination, stations):
        if lines_name == "":
            print("name is empty")
            return
        if origin == "":
            print("origin is empty")
            return
        if destination == "":
            print("destination is empty")
            return
        if not stations:
            print("stations list is empty")
            return
        for line in self.lines_listt:
            if line[0].lower() == lines_name.lower():
                print("This name exists, enter another name")
                return
        line_record = [lines_name, origin, destination, stations]
        self.lines_listt.append(line_record)
        print(f"line '{lines_name}' added successfully")

#Update line 2
def update_lines_info(self, lines_name=None):
        while True:
            if not lines_name:
                lines_name = input("enter line name (or type 'back' to return): ").strip()
                if lines_name.lower() == "back":
                    return
            record = None
            for key in self.lines_dict:
                if key.lower() == lines_name.lower():
                    record = self.lines_dict[key]
                    lines_name = key
                    break
            if not record:
                print("Line name not found.")
                lines_name = None
                continue
            while True:
                print(f"1) name: {record[0]}")
                print(f"2) origin: {record[1]}")
                print(f"3) destination: {record[2]}")
                print(f"4) stations: {', '.join(record[3])}")
                choice = input("which one do you want to update? (1/2/3/4 or b): ").strip().lower()
                if choice in ("b"):
                    return
                if choice == "1":
                    new_name = input("enter new name: ").strip()
                    if new_name == "":
                        print("name cannot be empty")
                        continue
                    if any(k.lower() == new_name.lower() and k.lower() != lines_name.lower() for k in self.lines_dict):
                        print("this name exists")
                        continue
                    record[0] = new_name
                    self.all_info()
                    lines_name = new_name
                    print("name updated")
                elif choice == "2":
                    new_origin = input("enter new origin: or back ").strip()
                    if new_origin.lower() == "back":
                        return
                    if new_origin == "":
                        print("origin cannot be empty")
                        continue
                    record[1] = new_origin
                    self.all_info()
                    print("origin updated")
                elif choice == "3":
                    new_destination = input("enter new destination: or back ").strip()
                    if new_destination.lower() == "back":
                        return
                    if new_destination == "":
                        print("destination cannot be empty")
                        continue
                    record[2] = new_destination
                    self.all_info()
                    print("destination updated")
                elif choice == "4":
                    new_stations = input("enter stations separated by commas: ").strip().split(",")
                    if not new_stations:
                        print("stations cannot be empty")
                        continue
                    record[3] = new_stations
                    self.all_info()
                    print("stations updated")
                else:
                    print("invalid choice")


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
