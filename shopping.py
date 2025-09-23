import datetime
class Shopping:
    def __init__(self, trains_dict, wallet, username):
        self.trains_dict = trains_dict
        self.wallet = wallet
        self.username = username

    def show_trains(self):
        if not self.trains_dict:
            print("No trains available.")
            return
        print("\nAvailable Trains:")
        for name, info in self.trains_dict.items():
            print(f"{name}: Line={info['line']}, Price={info['ticket_price']}$, Remaining={info['capacity']}")
        with open("trains.txt", "w", encoding="utf-8") as f:
            for name, info in self.trains_dict.items():
                f.write(f"{name}: Line={info['line']}, Price={info['ticket_price']}$, Remaining={info['capacity']}\n")

    def buy_ticket(self):
        if not self.trains_dict:
            print("No trains available!")
            return
        train_name = input("Enter train name: ").strip()
        if train_name not in self.trains_dict:
            print("Train not found!")
            return
        train = self.trains_dict[train_name]
        try:
            qty = int(input("Enter ticket quantity: ").strip())
        except ValueError:
            print("Invalid quantity!")
            return
        if qty <= 0:
            print("Quantity must be greater than zero!")
            return
        total_price = qty * train["ticket_price"]
        if self.wallet.balance < total_price:
            print("Insufficient wallet balance!")
            return
        if qty > train["capacity"]:
            print("Not enough tickets available!")
            return
        self.wallet.pay(total_price)
        train["capacity"] -= qty
        print(f"Successfully bought {qty} ticket(s) for {train_name}. Remaining wallet: {self.wallet.balance}$")
        if train["capacity"] == 0:
            print(f"{train_name} is sold out!")
        with open("tickets.txt", "a", encoding="utf-8") as f:
            f.write(f"User: {self.username} bought {qty} tickets for {train_name}, Total={total_price}$\n")

    def export_ticket(username, train_name, qty, total_price):
        exact_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"ticket_{username}_{exact_time}.txt"
        ticket_info = f"""

        Buyer Name: {username}
        Train Name: {train_name}
        Quantity: {qty}
        Total Price: {total_price}
        Purchase Time: {exact_time}
        
        """

        with open(filename, "w") as f:
            f.write(ticket_info)

        print(f"Ticket exported successfully! Details saved to {filename}")

    