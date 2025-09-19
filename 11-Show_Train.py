def show_trains(self):
    if not self.trains:
        print("No trains registered")
        return

    print("Trains list")
    for name, info in self.trains.items():
        print(f"Train Name : {name}")
        for key, value in Train_info.items():
            print(f"{key}: {value}")
            return

