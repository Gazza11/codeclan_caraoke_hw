class FrontTill:
    def __init__(self, total):
        self.total = total


    def receive_entry_payment(self, customer):
        if self.check_entry_paid(customer) != True and customer.wallet > 4:
            self.front_till.total += 5
        else:
            return 'Not entry'



    def check_entry_paid(self, customer):
        if customer.entry_paid == True:
            return True
        else:
            return 'Need to pay entry'