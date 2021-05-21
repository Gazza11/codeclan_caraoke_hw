import unittest

from src.front_till import FrontTill
from src.guest import Guest

class TestFrontTill(unittest.TestCase):
    def setUp(self):
        self.front_till = FrontTill(100)

        self.guest1 = Guest('Peter', 100)
        self.guest2 = Guest('Jaap', 45)
        self.guest3 = Guest('Denis', 0)

#
    def test_front_till_amount(self):
        self.assertEqual(100, self.front_till.total)

#
    def test_entry_check__no(self):
        self.assertEqual('Need to pay entry', self.front_till.check_entry_paid(self.guest1))

#
    def test_entry_check__yes(self):
        self.guest1.pay_entry(self.guest1)
        self.assertEqual(True, self.front_till.check_entry_paid(self.guest1))

#
    def test_entry_check__before_pay_and_after(self):
        self.assertEqual('Need to pay entry', self.front_till.check_entry_paid(self.guest1))
        self.guest1.pay_entry(self.guest1)
        self.assertEqual(True, self.front_till.check_entry_paid(self.guest1))

    def test_money_changed_hands__can_pay(self):
        self.guest1.pay_entry(self.guest1)
        self.front_till.receive_entry_payment(self.guest1)
        # self.assertEqual(105, self.front_till.total)
        self.assertEqual(95, self.guest1.wallet)
