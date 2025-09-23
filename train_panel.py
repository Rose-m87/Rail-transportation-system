class RailwayManager:
    def __init__(self):
        self.lines_dict = {}
        self.trains_dict = {}

    def add_line(self, line_name, origin, destination, stations):
        if not line_name or not origin or not destination or not stations:
            print("All fields are required!")
            return
        if line_name in self.lines_dict:
            print("Line exists!")
            return
        self.lines_dict[line_name] = [line_name, origin, destination, stations]
        print(f"Line '{line_name}' added!")

    def update_line_info(self, line_name):
        record = self.lines_dict.get(line_name)
        if not record:
            print("Line not found!")
            return
        print("for exit: Enter")
        print("1) Name\n2) Origin\n3) Destination\n4) Stations\n")
        choice = input("Choose: ").strip()
        if choice == "1":
            new_name = input("New name: ").strip()
            if new_name and new_name not in self.lines_dict:
                self.lines_dict[new_name] = self.lines_dict.pop(line_name)
                self.lines_dict[new_name][0] = new_name
        elif choice == "2":
            record[1] = input("New origin: ").strip()
        elif choice == "3":
            record[2] = input("New destination: ").strip()
        elif choice == "4":
            record[3] = input("Stations (comma): ").strip().split(",")
            print("Line updated!")
    

        
    

    def delete_line(self, line_name):
        if line_name in self.lines_dict:
            del self.lines_dict[line_name]
            print("Line deleted!")
        else:
            print("Line not found!")

    def view_lines(self):
        if not self.lines_dict:
            print("No lines!")
            return
        print("\n--- Lines ---")
        for l, info in self.lines_dict.items():
            print(f"Name: {info[0]}, Origin: {info[1]}, Destination: {info[2]}, Stations: {', '.join(info[3])}")

    def add_train(self, name, line, avg_speed, stop_time, quality, ticket_price, capacity):
        if not (name and line and avg_speed and stop_time and quality and ticket_price and capacity):
            print("All fields are required!")
            return
        if name in self.trains_dict:
            print("Train name already exists!")
            return
        if line not in self.lines_dict:
            print("Line doesn't exist!")
            return
        try:
            self.trains_dict[name] = {
                "line": line,
                "avg_speed": float(avg_speed),
                "stop_time": float(stop_time),
                "quality": int(quality),
                "ticket_price": float(ticket_price),
                "capacity": int(capacity)
            }
        except ValueError:
            print("Numeric values are invalid!")
            return
        print(f"Train '{name}' added!")

    def update_train(self, name):
        record = self.trains_dict.get(name)
        if not record:
            print("Train not found!")
            return
        print("\nCurrent train info:")
        for k, v in record.items():
            print(f"{k}: {v}")
        print("\nEnter new values (press Enter to skip):")
        line = input("Line: ").strip()
        if line and line in self.lines_dict:
            record["line"] = line
        try:
            avg_speed = input("Average speed: ").strip()
            if avg_speed:
                record["avg_speed"] = float(avg_speed)
            stop_time = input("Stop time: ").strip()
            if stop_time:
                record["stop_time"] = float(stop_time)
            quality = input("Quality: ").strip()
            if quality:
                record["quality"] = int(quality)
            ticket_price = input("Ticket price: ").strip()
            if ticket_price:
                record["ticket_price"] = float(ticket_price)
            capacity = input("Capacity: ").strip()
            if capacity:
                record["capacity"] = int(capacity)
        except ValueError:
            print("Invalid input! Update aborted.")
            return
        print(f"Train '{name}' updated!")

    def delete_train(self, name):
        if name in self.trains_dict:
            del self.trains_dict[name]
            print("Train deleted!")
        else:
            print("Train not found!")

    def show_trains(self):
        if not self.trains_dict:
            print("No trains!")
            return
        print("\n--- Trains ---")
        for t, info in self.trains_dict.items():
            print(f"Name: {t}, Line: {info['line']}, Speed: {info['avg_speed']}, Stop time: {info['stop_time']}, "
                  f"Quality: {info['quality']}, Ticket price: {info['ticket_price']}, Capacity: {info['capacity']}")