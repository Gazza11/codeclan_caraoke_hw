import unittest
from src.guest import Guest
from src.rooms import Rooms
from src.front_till import FrontTill

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Peter', 100)
        self.guest2 = Guest('Jaap', 45)
        self.guest3 = Guest('Denis', 0)

        self.front_till = FrontTill(100)

#1
    def test_guest_has_name__1(self):
        self.assertEqual('Peter', self.guest1.name)

#2
    def test_guest_has_name__2(self):
        self.assertEqual('Jaap', self.guest2.name)

#   
    def test_wallet__person_1(self):
        self.assertEqual(100, self.guest1.wallet)

# 
    def test_wallet__person_3(self):
        self.assertEqual(0, self.guest3.wallet)

#
    def test_paid_entry__no(self):
        self.assertEqual(False, self.guest1.entry_paid)

#
    def test_paid_entry__yes(self):
        self.guest1.pay_entry(self.guest1, self.front_till)
        self.assertEqual(True, self.guest1.entry_paid)