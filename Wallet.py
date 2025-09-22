from BANK import API

class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.cards = []
        self.bank_api = API()

    def add_balance(self, amount, card, exp_month, exp_year, password, cvv2):
        try:
            payment_id = self.bank_api.pay(card, exp_month, exp_year, password, cvv2, amount)
            self.balance += amount
            if card not in [c["card"] for c in self.cards]:
                self.cards.append({
                    "card": card,
                    "exp_month": exp_month,
                    "exp_year": exp_year
                })
            print(f"Balance updated successfully! Payment ID: {payment_id}")
            print(f"Current balance: {self.balance}")
        except ValueError:
            print("Invalid card information. Please try again.")

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of {amount} was successful. Remaining balance: {self.balance}")
            return True
        else:
            print("Insufficient balance. Please recharge your wallet.")
            return False

    def show_wallet(self):
        print(f"--- {self.owner}'s Wallet ---")
        print(f"Balance: {self.balance}")
        if not self.cards:
            print("No cards saved.")
        else:
            print("Saved cards:")
            for c in self.cards:
                print(f"Card: {c['card']} | Exp: {c['exp_month']}/{c['exp_year']}")
