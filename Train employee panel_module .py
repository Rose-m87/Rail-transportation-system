#from ... import ...

class TrainEmployeePanel:
    def __init__(self):
        self.manager = RailwayManager()

    def show_menu(self):
        while True:
            print("--- Train Employee Panel ---\n")
            print("1. Add Line\n")
            print("2. Update Line Info\n")
            print("3. Delete Line\n")
            print("4. View Lines\n")
            print("5. Add Train\n")
            print("6. Update Train Info\n")
            print("7. Delete Train\n")
            print("8. Show Trains\n")
            print("9. Exit")

            choice = input("Select option: ").strip()
            
            if choice == "1":
                print("\n---Add line section---")
                line_name = input("Enter line name: ").strip()
                origin = input("Enter origin: ").strip()
                destination = input("Enter destination: ").strip()
                stations = input("Enter stations separated by commas: ").strip().split(",")
                self.manager.add_line(line_name,origin,destination,stations)

            elif choice == "2":
                print("\n---Update line info section---")
                line_name = input("enter line name (or type 'back' to return): ").strip()
                if line_name.lower() == "back":
                    return
                self.manager.update_lines_info(line_name)

            elif choice == "3":
                print("\n---Delete line section---")
                delete_line_name = input("Enter line name to delete (or 0 to go panel): ")
                if delete_line_name == "0":
                    return
                self.manager.delete_line(delete_line_name)

            elif choice == "4":
                self.manager.view_line_dict(self)

            elif choice == "5":
                print("\n---Add Train section---")
                name = input("Enter name or back").strip()
                if name.lower() == "back":
                    print("Returning to the panel")
                    return
                
                line = input("Enter line name or back").strip()
                if line.lower() == "back":
                    print("Returning to the panel")
                    return
                
                avr_speed = input("Enter average speed or back")
                if avr_speed.lower() == "back":
                    print("Returning to the panel")
                    return
                
                stop_time = input("Enter stop time or back")
                if stop_time.lower() == "back":
                    print("Returning to the panel")
                    return
                
                Quality = input("Enter quality or back")
                if Quality.lower() == "back":
                    print("Returning to the panel")
                    return
                
                ticket_price = input("Enter price or back")
                if ticket_price.lower() == "back":
                    print("Returning to the panel")
                    return
                
                train_capacity = input("Enter train capacity or back")
                if train_capacity.lower() == "back":
                    print("Returning to the panel")
                    return
                
                self.manager.add_train(name,line,avr_speed,stop_time,Quality,ticket_price,train_capacity)

            elif choice == "6":
                print("\n---Update Train Info section---")
                name = input("Enter name or back: ").strip()
                if name.lower() == "back":
                    print("Returning to the panel")
                    return
                self.manager.update_train(name)

            elif choice == "7":
                print("\n---Delete Train section---")
                delete_train_name = input("Enter train name to delete (or 0 to go panel): ")
                if delete_train_name == "0":
                    return
                self.manager.delete_train(delete_train_name)

            elif choice == "8":
                self.manager.show_trains_dict(self)

            #elif choice == "9":
                #print("Exiting panel...")
                #break
            else:
                print("Invalid choice")
