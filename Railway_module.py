class RailwayManager:
    def __init__(self):
        self.lines_dict = {}
        self.trains_dict = {}

    # Add line
    def add_line(self, line_name, origin, destination, stations):
        if not line_name or not origin or not destination or not stations:
            print("Error: All fields are required")
            return

        if line_name in self.lines_dict:
            print("This line name already exists!")
            return

        self.lines_dict[line_name] = [line_name, origin, destination, stations]
        print(f"Line '{line_name}' added successfully!")

    # Update line info
    def update_line_info(self, line_name):
        record = self.lines_dict.get(line_name)
        if not record:
            print("Line not found!")
            return

        print(f"1) Name: {record[0]}")
        print(f"2) Origin: {record[1]}")
        print(f"3) Destination: {record[2]}")
        print(f"4) Stations: {', '.join(record[3])}")

        choice = input("Choose field to update (1/2/3/4 or 'b' to back): ").strip().lower()
        if choice == "b":
            return
        elif choice == "1":
            new_name = input("Enter new name: ").strip()
            if new_name and new_name not in self.lines_dict:
                self.lines_dict[new_name] = self.lines_dict.pop(line_name)
                self.lines_dict[new_name][0] = new_name
                print("Name updated!")
            else:
                print("Invalid or existing name!")
        elif choice == "2":
            new_origin = input("Enter new origin: ").strip()
            if new_origin:
                record[1] = new_origin
                print("Origin updated!")
        elif choice == "3":
            new_destination = input("Enter new destination: ").strip()
            if new_destination:
                record[2] = new_destination
                print("Destination updated!")
        elif choice == "4":
            new_stations = input("Enter stations separated by commas: ").strip().split(",")
            if new_stations:
                record[3] = new_stations
                print("Stations updated!")
        else:
            print("Invalid choice!")

    # Delete line
    def delete_line(self, line_name):
        if line_name in self.lines_dict:
            del self.lines_dict[line_name]
            print(f"Line '{line_name}' deleted!")
        else:
            print("Line not found!")

    # View lines
    def view_lines(self):
        if not self.lines_dict:
            print("No lines available!")
            return
        print("\n--- Lines ---")
        for line in self.lines_dict:
            print(line)

    # Add train
    def add_train(self, name, line, avg_speed, stop_time, quality, ticket_price, capacity):
        if name in self.trains_dict:
            print("Train name already exists!")
            return
        if line not in self.lines_dict:
            print("Line doesn't exist!")
            return

        try:
            avg_speed = float(avg_speed)
            stop_time = float(stop_time)
            quality = int(quality)
            ticket_price = float(ticket_price)
            capacity = int(capacity)
        except ValueError:
            print("Invalid numeric input!")
            return

        self.trains_dict[name] = {
            "line": line,
            "avg_speed": avg_speed,
            "stop_time": stop_time,
            "quality": quality,
            "ticket_price": ticket_price,
            "capacity": capacity,
            "id": f"{name}_{capacity}"
        }
        print(f"Train '{name}' added successfully!")

    # Update train
    def update_train(self, name):
        record = self.trains_dict.get(name)
        if not record:
            print("Train not found!")
            return

        print(record)
        print("1) Line\n2) Avg Speed\n3) Stop Time\n4) Quality\n5) Ticket Price\n6) Capacity\n7) Back")
        choice = input("Choose field to update: ").strip()
        if choice == "7":
            return
        elif choice == "1":
            line = input("Enter new line: ").strip()
            if line in self.lines_dict:
                record["line"] = line
        elif choice == "2":
            val = input("Enter new average speed: ").strip()
            if val.replace(".", "", 1).isdigit():
                record["avg_speed"] = float(val)
        elif choice == "3":
            val = input("Enter new stop time: ").strip()
            if val.replace(".", "", 1).isdigit():
                record["stop_time"] = float(val)
        elif choice == "4":
            val = input("Enter new quality: ").strip()
            if val.isdigit():
                record["quality"] = int(val)
        elif choice == "5":
            val = input("Enter new ticket price: ").strip()
            if val.replace(".", "", 1).isdigit():
                record["ticket_price"] = float(val)
        elif choice == "6":
            val = input("Enter new capacity: ").strip()
            if val.isdigit():
                record["capacity"] = int(val)
        print(f"Train '{name}' updated!")

    # Delete train
    def delete_train(self, name):
        if name in self.trains_dict:
            del self.trains_dict[name]
            print(f"Train '{name}' deleted!")
        else:
            print("Train not found!")

    # Show trains
    def show_trains(self):
        if not self.trains_dict:
            print("No trains available!")
            return
        print("\n--- Trains ---")
        for train in self.trains_dict.values():
            print(train)
