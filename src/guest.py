# Guests have a name and a wallet. May add a age on. Possibly to check before they buy an alcoholic
# drink of maybe just for entry.
# Could also set a boolean for whether they have paid for entry or not?
from src.front_till import FrontTill


class Guest:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.entry_paid = False
        self.age = age

    def pay_entry(self, customer, front_till):
        if customer.entry_paid == True:
            return 'Already paid'
        elif customer.wallet < 5:
            return 'Not enough money'
        else:
            customer.wallet -= 5
            front_till.receive_entry_payment()
            customer.entry_paid = True
