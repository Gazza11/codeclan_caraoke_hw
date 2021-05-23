import unittest
from src.rooms import Rooms
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest1 = Guest('Peter', 100, 35)
        self.guest2 = Guest('Jaap', 45, 40)
        self.guest3 = Guest('Denis', 0, 16)

        self.song1 = Song('Song A', 150)
        self.song2 = Song('Song B', 210)
        self.song3 = Song('Song C', 1000)

        self.room1 = Rooms('Aurum', 20)
        self.room2 = Rooms('Institute', 1)

#1
    def test_room_has_name__one(self):
        self.assertEqual('Aurum', self.room1.room_name)

#2
    def test_room_has_name__two(self):
        self.assertEqual('Institute', self.room2.room_name)

#3
    def test_room_has_guests__empty(self):
        self.assertEqual([], self.room1.list_of_current_guests)

#4
    def test_room_has_list_of_songs__empty(self):
        self.assertEqual([], self.room1.list_of_songs)

#5
    def test_add_song_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.list_of_songs))
    
#6
    def test_add_song__check_both_rooms(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.list_of_songs))
        self.assertEqual(0,len (self.room2.list_of_songs))

#7
    def test_add_song__multiple(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.list_of_songs))
        self.assertEqual(0,len (self.room2.list_of_songs))

#8
    def test_add_person_to_room__room1(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual(1, len(self.room1.list_of_current_guests))

#9
    def test_add_person__more_than_1(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.assertEqual(2, len(self.room1.list_of_current_guests))

#10
    def test_add_person__multiple_rooms(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.room2.add_person(self.room1.list_of_current_guests, self.guest3)
        self.assertEqual(2, len(self.room1.list_of_current_guests))
        self.assertEqual(1, len(self.room2.list_of_current_guests))

#11
    def test_check_person_in_room__person_there(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Peter', self.room1.check_person(self.room1.list_of_current_guests, self.guest1))

#12
    def test_check_person_in_room__person_not_there(self):
        self.assertEqual('Person not in this room.', self.room1.check_person(self.room1.list_of_current_guests, self.guest1))

#13 
    def test_check_person_in_room__person_in_room1_but_check_other_room(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Person not in this room.', self.room2.check_person(self.room2.list_of_current_guests, self.guest1))

#14
    def test_add_person_to_room__already_in(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Already in room', self.room1.add_person(self.room1.list_of_current_guests, self.guest1))

#15
    def test_remove_person__room1(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.room1.remove_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual(1, len(self.room1.list_of_current_guests))

#16
    def test_remove_person__not_in_room(self):
        self.room1.remove_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual('Person not in this room.', self.room1.remove_person(self.room1.list_of_current_guests, self.guest1))

#17
    def test_add_then_remove_then_check(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1) #Add Peter, room 1
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2) #Add Jaap, room 1
        self.assertEqual(2, len(self.room1.list_of_current_guests)) #Check room 1
        self.assertEqual(0, len(self.room2.list_of_current_guests)) #Check room 2
        self.room1.remove_person(self.room1.list_of_current_guests, self.guest1) #Remove Peter, room 1
        self.assertEqual(1, len(self.room1.list_of_current_guests)) #Check room 1
        self.assertEqual(0, len(self.room2.list_of_current_guests)) #Check room 2
        self.assertEqual('Jaap', self.room1.check_person(self.room1.list_of_current_guests, self.guest2)) 
        self.assertEqual('Person not in this room.', self.room2.check_person(self.room2.list_of_current_guests, self.guest2))

# EXTENSIONS - Capacity

#18
    def test_capacity__room1(self):
        self.assertEqual(20, self.room1.capacity)

#19
    def test_capacity__room2(self):
        self.assertEqual(1, self.room2.capacity)

#20
    def test_capacity__add_person(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual(19, self.room1.capacity)

#21
    def test_capacity__remove_person(self):
        self.room1.add_person(self.room1.list_of_current_guests, self.guest1)
        self.room1.add_person(self.room1.list_of_current_guests, self.guest2)
        self.room1.remove_person(self.room1.list_of_current_guests, self.guest1)
        self.assertEqual(19, self.room1.capacity)

#22
    def test_space_left__room1(self):
        self.assertEqual(20, self.room1.space_left_in_room())

#23
    def test_space_left__room2(self):
        self.assertEqual(1, self.room2.space_left_in_room())

#24
    def test_no_space__room2(self):
        self.room2.add_person(self.room2.list_of_current_guests, self.guest1)
        self.assertEqual('Room is full!', self.room2.add_person(self.room2.list_of_current_guests, self.guest2))

# Advanced Extensions

#25
    def test_current_song__empty(self):
        self.assertEqual('Playlist empty', self.room1.current_song(self.room1))

#26
    def test_current_song__1_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual('Song A', self.room1.current_song(self.room1))

#27
    def test_current_song__1_song(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room1.add_song(self.song3)
        self.assertEqual('Song C', self.room1.current_song(self.room1))

# 28
    def test_current_song__2_songs_2_rooms(self): #Helped see .pop() doesn't make sense to use.
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.room2.add_song(self.song3)
        self.assertEqual('Song B', self.room1.current_song(self.room1))
        self.assertEqual('Song C', self.room2.current_song(self.room2))
        self.assertEqual(2, len(self.room1.list_of_songs))
        self.assertEqual(1, len(self.room2.list_of_songs))

