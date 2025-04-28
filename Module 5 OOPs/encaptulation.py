class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Invalid ammount balance")

    def _display_balance(self):
        print(f"Balance: {self._balance}") 

    def show_balance(self):
        self._display_balance()
    
account = Account("GK", 10000)
account.deposit(1000)
account.show_balance()