# Update_Train
def update_train(self):
    while True:
        name = input("Enter name or back")
        if name.lower() == "back":
            print("Returning to the panel")
            return

        if name not in self.trains:
            print("Train doesn't exist")
            continue

        train_info = self.trains[name]

        print("Current Train Info")
        for key, value in train_info.items():
            print(f"{key}: {value}")

        print("Select the field number to update")
        print("1. Line")
        print("2. Average Speed")
        print("3. Stop Time")
        print("4. Quality")
        print("5. Ticket Price")
        print("6. Capacity")
        print("7. Back")

        choice = input("Enter your choice")

        if choice == "1":
            line = input("Enter new line name or back: ")
            if line.lower() == "back":
                print("Returning to the panel")
                return
            if line not in self.lines:
                print("The Line doesn't exist")
                continue
            train_info["line"] = line

        elif choice == "2":
            while True:
                avr_speed = input("Enter new average speed or back: ")
                if avr_speed.lower() == "back":
                    print("Returning to the panel")
                    return
                if avr_speed.isdigit():
                    train_info["speed"] = float(avr_speed)
                    break
                else:
                    print("Please enter a valid number")

        elif choice == "3":
            while True:
                stop_time = input("Enter new stop time or back: ")
                if stop_time.lower() == "back":
                    print("Returning to the panel")
                    return
                if stop_time.isdigit():
                    train_info["stop_time"] = float(stop_time)
                    break
                else:
                    print("Please enter a valid number")

        elif choice == "4":
            while True:
                Quality = input("Enter new quality or back: ")
                if Quality.lower() == "back":
                    print("Returning to the panel")
                    return
                if Quality.isdigit():
                    train_info["quality"] = int(Quality)
                    break
                else:
                    print("Please enter a valid number")

        elif choice == "5":
            while True:
                ticket_price = input("Enter new ticket price or back: ")
                if ticket_price.lower() == "back":
                    print("Returning to the panel")
                    return
                if ticket_price.isdigit():
                    train_info["ticket_price"] = float(ticket_price)
                    break
                else:
                    print("Please enter a valid number")

        elif choice == "6":
            while True:
                train_capacity = input("Enter new train capacity or back: ")
                if train_capacity.lower() == "back":
                    print("Returning to the panel")
                    return
                if train_capacity.isdigit():
                    train_info["capacity"] = int(train_capacity)
                    break
                else:
                    print("Please enter a valid number")

        elif choice == "7":
            print("Returning to the panel")
            return

        else:
            print("Invalid choice. Try again.")
            continue

        self.trains[name] = train_info
        print(f"Train '{name}' updated successfully!")
        return
