#Rose , Behesht , Farzad

class RailwayManager:
    def __init__(self):
        self.lines_dict = {}
        self.trains_dict = {}

    #Add line 1
    def add_line(self,line_name,origin,destination,stations):

        if not line_name:
            print("name is empty")
            return
        if  not origin:
            print("origin is empty")
            return
        if not destination:
            print("destination is empty")
            return
        if not stations:
            print("stations list is empty")
            return
        if line_name in self.lines_dict:
                print("This name exists, enter another name")
                return
        self.lines_dict[line_name] = [line_name,origin,destination,stations]
        print(f"line '{line_name}' added successfully")

    #Update line info 2
    def update_lines_info(self,line_name):
        record = self.lines_dict.get(line_name)
        if not record:
            print("Line name not found.")
            return
        
        print(f"1) name: {record[0]}")
        print(f"2) origin: {record[1]}")
        print(f"3) destination: {record[2]}")
        print(f"4) stations: {', '.join(record[3])}")

        choice = input("which one do you want to update? (1/2/3/4 or b): ").strip().lower()
        if choice == "b":
            return
        elif choice == "1":
            new_name = input("enter new name: ").strip()
            if new_name == "":
                print("name cannot be empty")
                return
            if new_name and new_name not in self.lines_dict:
                self.lines_dict[new_name] = self.lines_dict.pop(line_name)
                self.lines_dict[new_name][0] = new_name
            print("name updated")
        elif choice == "2":
            new_origin = input("enter new origin: or back ").strip()
            if new_origin.lower() == "back":
                return
            if new_origin == "":
                print("origin cannot be empty")
                return
            if new_origin:
                record[1] = new_origin
                print("origin updated")
        elif choice == "3":
            new_destination = input("enter new destination: or back ").strip()
            if new_destination.lower() == "back":
                return
            if new_destination == "":
                print("destination cannot be empty")
                return
            if new_destination:
                record[2] = new_destination
                print("destination updated")
        elif choice == "4":
            new_stations = input("enter stations separated by commas: ").strip().split(",")
            if not new_stations:
                print("stations cannot be empty")
                return
            if new_stations:
                record[3] = new_stations
            print("stations updated")
        else:
            print("invalid choice")


    #Delete line 3
    def delete_line(self,delete_line_name):       
            if delete_line_name in self.lines_dict:
                del self.lines_dict[delete_line_name]
                print(f"Line '{delete_line_name}' deleted successfully!")
            else:
                print("Line not found")

    #View lines list 4
    def view_line_dict(self):
            print("\n--- Lines List ---")
            if not self.lines_dict:
                print("No Lines available.")
                return
            for line in self.lines_dict:
                print(line)

    #Add Train 5
    def add_train(self,name,line,avr_speed,stop_time,Quality,ticket_price,train_capacity):

        if name in self.trains_dict:
            print("The name already exists")
            yy = input("Wanna try again?")
            if yy.lower() == "no":
                print("Returning to the panel")
                return
            elif yy.lower() == "yes":
                return

        if line not in self.lines_dict:
            print("The Line doesn't exist")
            zz = input("Wanna try again?")
            if zz.lower() == "no":
                print("Returning to the panel")
            elif zz.lower() == "yes":
                return

        if avr_speed.isdigit():
            speed = float(avr_speed)
        else:
            print("Please enter a valid number")


        if stop_time.isdigit():
            stop = float(stop_time)
        else:
            print("Please enter a valid number")


        if Quality.isdigit():
            quality = int(Quality)
        else:
            print("Please enter a valid number")


        if ticket_price.isdigit():
            price = float(ticket_price)
        else:
            print("Please enter a valid number")


        if train_capacity.isdigit():
            capacity = int(train_capacity)
        else:
            print("Please enter a valid number")

        train_info = {
            "line": line,
            "speed": speed,
            "stop_time": stop,
            "quality": quality,
            "ticket_price": price,
            "capacity": capacity,
            "id": f"{name}_{capacity}"
        }

        self.trains_dict[name] = train_info

        print(f"Train '{name}' added successfully!")
        return

    #Update train info 6
    def update_train(self,name):
       
        record = self.trains_dict.get(name)
        if not record:
            print("Train doesn't exist")
            return
        print("Current Train Info:", record)
        print("1) {}\n2), {}\n3) {}\n4) {}\n5) {}\n6) {}\n7) Back")

        choice = input("Enter your choice").strip()

        if choice == "7":
            return
        elif choice == "1":
            line = input("Enter new line name or back: ").strip()
            if line.lower() == "back":
                print("Returning to the panel")
                return
            line = input("Enter new line name: ").strip()
            if line in self.lines_dict:
                record[1] = line
        elif choice == "2":
            avr_speed = input("Enter new average speed or 0 for back: ").strip().isdigit()
            if avr_speed == "0":
                print("Returning to the panel")
                return
            record[2] = float(avr_speed)
        elif choice == "3":
            stop_time = input("Enter new stop time or 0 for back: ").strip().isdigit()
            if stop_time == "0":
                print("Returning to the panel")
                return
            record[3] = int(stop_time)
        elif choice == "4":
            Quality = input("Enter new quality or 0 for back: ").strip().isdigit()
            if Quality == "0":
                print("Returning to the panel")
                return
            record[4] = int(Quality)
        elif choice == "5":
            ticket_price = input("Enter new ticket price or 0 for back: ").strip().isdigit()
            if ticket_price == "0":
                print("Returning to the panel")
                return
            record[5] = float(ticket_price)
        elif choice == "6":
            train_capacity = input("Enter new train capacity or 0 for back: ").strip().isdigit()
            if train_capacity == "0":
                print("Returning to the panel")
                return
            record[6] = int(train_capacity)
        print(f"Train '{name}' updated successfully!")

    #Delete train 7
    def delete_train(self,delete_train_name):
            
            if delete_train_name in self.trains_dict:
                del self.trains_dict[delete_train_name]
                print(f"Train '{delete_train_name}' deleted successfully!")
            else:
                print("Train not found")

    #Show trains list 8
    def show_trains_dict(self):
            print("\n--- Trains List ---")
            if not self.trains_dict:
                print("No Trains available.")
                return
            for train in self.trains_dict.values:
                print(train)