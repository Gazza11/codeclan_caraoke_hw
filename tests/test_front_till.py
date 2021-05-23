import unittest

from src.front_till import FrontTill
from src.guest import Guest

class TestFrontTill(unittest.TestCase):
    def setUp(self):
        self.front_till = FrontTill(100)

        self.guest1 = Guest('Peter', 100, 35)
        self.guest2 = Guest('Jaap', 45, 40)
        self.guest3 = Guest('Denis', 0, 16)


## Extensions - Entry Fee
#1
    def test_front_till_amount(self):
        self.assertEqual(100, self.front_till.total)

#2
    def test_entry_check__no(self):
        self.assertEqual('Need to pay entry', self.front_till.check_entry_paid(self.guest1))

#3
    def test_entry_check__yes(self):
        self.guest1.pay_entry(self.guest1, self.front_till)
        self.assertEqual(True, self.front_till.check_entry_paid(self.guest1))

#4
    def test_entry_check__before_pay_and_after(self):
        self.assertEqual('Need to pay entry', self.front_till.check_entry_paid(self.guest1))
        self.guest1.pay_entry(self.guest1, self.front_till)
        self.assertEqual(True, self.front_till.check_entry_paid(self.guest1))

#5
    def test_entry_payment__true(self):
        actual = self.front_till.receive_entry_payment()
        self.assertEqual(105, actual)

#6
    def test_money_changed_hands__can_pay(self):
        self.guest1.pay_entry(self.guest1, self.front_till)
        
        self.assertEqual(105, self.front_till.total)
        self.assertEqual(95, self.guest1.wallet)

#7
    def test_money_changed_hands__can_pay_two(self):
        self.guest2.pay_entry(self.guest2, self.front_till)

#8
        self.assertEqual(105, self.front_till.total)
        self.assertEqual(40, self.guest2.wallet)

#9
    def test_entry__cannot_afford(self):
        self.guest3.pay_entry(self.guest3, self.front_till)
        self.assertEqual(100, self.front_till.total)
        self.assertEqual(0, self.guest3.wallet)