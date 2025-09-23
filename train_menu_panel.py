from train_panel import RailwayManager

class TrainEmployeePanel:
    def __init__(self):
        self.manager = RailwayManager()

    def show_menu(self):
        while True:
            print("\n--- Train Employee Panel ---")
            print("1) Add Line\n2) Update Line\n3) Delete Line\n4) View Lines")
            print("5) Add Train\n6) Update Train\n7) Delete Train\n8) Show Trains\n9) Exit")
            choice = input("Select: ").strip()
            if choice == "1":
                name = input("Line name: ").strip()
                origin = input("Origin: ").strip()
                dest = input("Destination: ").strip()
                if origin == dest:
                    print("The origin and destination are the same.")
                    continue
                stations = input("Stations (comma): ").strip().split(",")
                self.manager.add_line(name, origin, dest, stations)
            
                

            elif choice == "2":
                name = input("Line to update: ").strip()
                self.manager.update_line_info(name)
            elif choice == "3":
                name = input("Line to delete: ").strip()
                self.manager.delete_line(name)
            elif choice == "4":
                self.manager.view_lines()
            elif choice == "5":
                name = input("Train name: ").strip()
                line = input("Line: ").strip()
                avg_speed = input("Speed: ").strip()
                stop_time = input("Stop time: ").strip()
                quality = input("Quality: ").strip()
                price = input("Ticket price: ").strip()
                capacity = input("Capacity: ").strip()
                self.manager.add_train(name, line, avg_speed, stop_time, quality, price, capacity)
            elif choice == "6":
                name = input("Train to update: ").strip()
                self.manager.update_train(name)
            elif choice == "7":
                name = input("Train to delete: ").strip()
                self.manager.delete_train(name)
            elif choice == "8":
                self.manager.show_trains()
            elif choice == "9":
                break
            else:
                print("Invalid choice!")
            return