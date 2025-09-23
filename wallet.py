from BANK import API

class Wallet:
    def __init__(self):
        self.balance = 0
        self.cards = []
        self.bank_api = API()
    print("---Reminder---" \
    "Card: 16 digit\n" \
    "exp_month: 1 - 12\n" \
    "exp_year: 1403 - 1408\n" \
    "password: 6 digit\n" \
    "cvv2: 3 digit" \
    "---------------")

    def add_balance(self, amount, card, exp_month, exp_year, password, cvv2):
        try:
            exp_month = int(exp_month)
            exp_year = int(exp_year)
            payment_id = self.bank_api.pay(card, int(exp_month), int(exp_year), password, cvv2, amount)
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

    def add_card(self, card, exp_month, exp_year):
        if card in [c["card"] for c in self.cards]:
            print("Card already saved.")
            return False
        self.cards.append({
            "card": card,
            "exp_month": exp_month,
            "exp_year": exp_year
        })
        print("Card saved.")
        return True

    def list_cards(self):
        if not self.cards:
            print("No cards saved.")
            return
        for i, c in enumerate(self.cards, start=1):
            print(f"{i}. Card: {c['card']} | Exp: {c['exp_month']}/{c['exp_year']}")

    def select_card(self, index):
        if not (1 <= index <= len(self.cards)):
            print("Invalid card selection.")
            return None
        return self.cards[index-1]

    def add_balance_with_saved(self, index, amount, password, cvv2):
        card_info = self.select_card(index)
        if not card_info:
            return
        try:
            payment_id = self.bank_api.pay(card_info["card"], card_info["exp_month"], card_info["exp_year"], password, cvv2, amount)
            self.balance += amount
            print(f"Balance updated successfully! Payment ID: {payment_id}")
            print(f"Current balance: {self.balance}")
        except ValueError:
            print("Invalid card information. Please try again.")

    def direct_pay_with_saved(self, index, amount, password, cvv2):
        card_info = self.select_card(index)
        if not card_info:
            return False
        try:
            payment_id = self.bank_api.pay(card_info["card"], card_info["exp_month"], card_info["exp_year"], password, cvv2, amount)
            print(f"Direct payment successful! Payment ID: {payment_id}")
            return True
        except ValueError:
            print("Invalid card information. Please try again.")
            return False

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Payment of {amount} was successful. Remaining balance: {self.balance}")
            return True
        else:
            print("Insufficient balance. Please recharge your wallet.")
            return False

    def show_wallet(self):
        print(f"Balance: {self.balance}")
        if not self.cards:
            print("No cards saved.")
        else:
            print("Saved cards:")
            for c in self.cards:
                print(f"Card: {c['card']} | Exp: {c['exp_month']}/{c['exp_year']}")
    
    

        
        
