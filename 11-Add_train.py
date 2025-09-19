#Add_Train
    def __init__(self):
        self.lines = {}
        self.trains = {}

    def add_train(self):
        while True:
            name = input("Enter name or back")
            if name.lower() == "back":
                print("Returning to the panel")
                return

            if name in self.trains:
                print("The name already exists")
                continue

            line = input("Enter line name or back")
            if line.lower() == "back":
                print("Returning to the panel")
                return
            if line not in self.lines:
                print("The Line doesn't exist")
                continue

            while True:
                avr_speed = input("Enter average speed or back")
                if avr_speed.lower() == "back":
                    print("Returning to the panel")
                    return
                if avr_speed.isdigit():
                    speed = float(avr_speed)
                    break
                else:
                    print("Please enter a valid number")

            while True:
                stop_time = input("Enter stop time or back")
                if stop_time.lower() == "back":
                    print("Returning to the panel")
                    return
                if stop_time.isdigit():
                    stop = float(stop_time)
                    break
                else:
                    print("Please enter a valid number")

            while True:
                Quality = input("Enter quality or back")
                if Quality.lower() == "back":
                    print("Returning to the panel")
                    return
                if Quality.isdigit():
                    quality = int(Quality)
                    break
                else:
                    print("Please enter a valid number")

            while True:
                ticket_price = input("Enter price or back")
                if ticket_price.lower() == "back":
                    print("Returning to the panel")
                    return
                if ticket_price.isdigit():
                    price = float(ticket_price)
                    break
                else:
                    print("Please enter a valid number")

            while True:
                train_capacity = input("Enter train capacity or back")
                if train_capacity.lower() == "back":
                    print("Returning to the panel")
                    return
                if train_capacity.isdigit():
                    capacity = int(train_capacity)
                    break
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

            self.trains[name] = train_info

            print(f"Train '{name}' added successfully!")
            return
