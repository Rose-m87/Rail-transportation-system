from railway_module import RailwayManager

class TrainEmployeePanel:
    def __init__(self):
        self.manager = RailwayManager()

    def show_menu(self):
        while True:
            print("\n--- Train Employee Panel ---")
            print("1) Add Line")
            print("2) Update Line Info")
            print("3) Delete Line")
            print("4) View Lines")
            print("5) Add Train")
            print("6) Update Train Info")
            print("7) Delete Train")
            print("8) Show Trains")
            print("9) Exit")

            choice = input("Select option: ").strip()

            if choice == "1":
                name = input("Line name: ").strip()
                origin = input("Origin: ").strip()
                destination = input("Destination: ").strip()
                stations = input("Stations (comma separated): ").strip().split(",")
                self.manager.add_line(name, origin, destination, stations)

            elif choice == "2":
                name = input("Line name to update: ").strip()
                self.manager.update_line_info(name)

            elif choice == "3":
                name = input("Line name to delete: ").strip()
                self.manager.delete_line(name)

            elif choice == "4":
                self.manager.view_lines()

            elif choice == "5":
                name = input("Train name: ").strip()
                line = input("Line: ").strip()
                avg_speed = input("Average speed: ").strip()
                stop_time = input("Stop time: ").strip()
                quality = input("Quality: ").strip()
                ticket_price = input("Ticket price: ").strip()
                capacity = input("Capacity: ").strip()
                self.manager.add_train(name, line, avg_speed, stop_time, quality, ticket_price, capacity)

            elif choice == "6":
                name = input("Train name to update: ").strip()
                self.manager.update_train(name)

            elif choice == "7":
                name = input("Train name to delete: ").strip()
                self.manager.delete_train(name)

            elif choice == "8":
                self.manager.show_trains()

            elif choice == "9":
                print("Exiting panel...")
                break

            else:
                print("Invalid choice!")
