import unittest
from src.guests import Guests
from src.rooms import Rooms

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guests('Peter')
        self.guest2 = Guests('Jaap')
        self.guest3 = Guests('Denis')

    def test_guest_has_name__1(self):
        self.assertEqual('Peter', self.guest1.name)

    def test_guest_has_name__2(self):
        self.assertEqual('Jaap', self.guest2.name)