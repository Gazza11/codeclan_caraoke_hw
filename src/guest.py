# Guests have a name and a wallet. May add a age on. Possibly to check before they buy an alcoholic
# drink of maybe just for entry.
# Could also set a boolean for whether they have paid for entry or not?
from src.front_till import FrontTill


class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.entry_paid = False

    def pay_entry(self, customer):
        if customer.wallet < 5:
            return 'Not enough money'
        else:
            customer.wallet -= 5
            customer.entry_paid = True
