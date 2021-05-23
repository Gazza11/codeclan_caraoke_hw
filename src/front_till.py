class FrontTill:
    def __init__(self, total):
        self.total = total


    def receive_entry_payment(self): # Not sure if this is correct, works but seems wrong.
        self.total += 5
        return self.total

## This was the original function set up but seemed to always return None.

        # if self.check_entry_paid(customer) == True:  # This was the original function set up but seemed to always return None.
        #     return 'Already paid'
        # elif customer.wallet > 4:
        #     self.total = self.total + 5
        #     return self.total
        # else:
        #     return 'No entry'

    def check_entry_paid(self, customer):
        if customer.entry_paid == True:
            return True
        else:
            return 'Need to pay entry'