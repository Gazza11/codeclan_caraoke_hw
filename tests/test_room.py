import unittest
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guests('Peter')
        self.guest2 = Guests('Jaap')
        self.guest3 = Guests('Denis')

        self.song1 = Songs('Song A')
        self.song2 = Songs('Song B')
        self.song3 = Songs('Song C')

        

        # self.list_of_current_guests1 = [self.guest1, self.guest2]
        # self.list_of_current_guests2 = [self.guest3]
        self.room1 = Rooms('Aurum')
        self.room2 = Rooms('Institute')

    def test_room_has_name__one(self):
        self.assertEqual('Aurum', self.room1.room_name)

    def test_room_has_name__two(self):
        self.assertEqual('Institute', self.room2.room_name)

    def test_room_has_guests__one(self):
        self.assertEqual([], self.room1.list_of_current_guests)

    def test_room_has_list_of_songs__one(self):
        self.assertEqual([], self.room1.list_of_songs)

    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.list_of_songs))