import unittest
from src.rooms import Rooms
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest('Peter')
        self.guest2 = Guest('Jaap')
        self.guest3 = Guest('Denis')

        self.song1 = Song('Song A')
        self.song2 = Song('Song B')
        self.song3 = Song('Song C')

        self.room1 = Rooms('Aurum', 20)
        self.room2 = Rooms('Institute', 1)

#1
    def test_room_has_name__one(self):
        self.assertEqual('Aurum', self.room1.room_name)

#2
    def test_room_has_name__two(self):
        self.assertEqual('Institute', self.room2.room_name)

#3
    def test_room_has_guests__one(self):
        self.assertEqual([], self.room1.list_of_current_guests)

#4
    def test_room_has_list_of_songs__one(self):
        self.assertEqual([], self.room1.list_of_songs)

#5
    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.list_of_songs))
    
#
    def test_add_song__check_both_rooms(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.list_of_songs))
        self.assertEqual(0,len (self.room2.list_of_songs))

#
    def test_add_song__multiple(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.list_of_songs))
        self.assertEqual(0,len (self.room2.list_of_songs))

#
    def test_add_person_to_room__room1(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual(1, len(self.room1.list_of_current_guests))

#
    def test_add_person__more_than_1(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.assertEqual(2, len(self.room1.list_of_current_guests))

#
    def test_add_person__multiple_rooms(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.room2.add_person(self.room1.list_of_current_guests, self.guest3)
        self.assertEqual(2, len(self.room1.list_of_current_guests))
        self.assertEqual(1, len(self.room2.list_of_current_guests))

#
    def test_check_person_in_room__person_there(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Peter', self.room1.check_person(self.room1.list_of_current_guests, self.guest1))

#
    def test_check_person_in_room__person_not_there(self):
        self.assertEqual('Person not in this room.', self.room1.check_person(self.room1.list_of_current_guests, self.guest1))

#
    def test_add_person_to_room__already_in(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Already in room', self.room1.add_person(self.room1.list_of_current_guests, self.guest1))
#
    def test_remove_person__room1(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.room1.remove_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual(1, len(self.room1.list_of_current_guests))

#
    def test_remove_person__not_in_room(self):
        self.room1.remove_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Person not in this room.', self.room1.remove_person(self.room1.list_of_current_guests, self.guest1))

# EXTENSIONS

#
    def test_capacity__room1(self):
        self.assertEqual(20, self.room1.capacity)

    def test_capacity__room2(self):
        self.assertEqual(1, self.room2.capacity)