import unittest
from src.guest import Guest
from src.rooms import Rooms

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest('Peter')
        self.guest2 = Guest('Jaap')
        self.guest3 = Guest('Denis')

#1
    def test_guest_has_name__1(self):
        self.assertEqual('Peter', self.guest1.name)

#2
    def test_guest_has_name__2(self):
        self.assertEqual('Jaap', self.guest2.name)