from src.song import Song

# Rooms have a name and a capacity that is set per room. They also have two empty lists for songs ans guests.

# Current song will be the last added to the playlist.

class Rooms:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.list_of_current_guests = []
        self.list_of_songs = []
        self.capacity = capacity

    def add_person(self, room_list, new_person):
        if self.space_left_in_room() < 1:
            return 'Room is full!'
        elif self.check_person(room_list, new_person) == new_person.name:
            return 'Already in room'
        else:
            self.list_of_current_guests.append(new_person)
            self.capacity -= 1

    def remove_person(self, room_list, person):
        if self.check_person(room_list, person) == person.name:
            self.list_of_current_guests.remove(person)
            self.capacity += 1
        return 'Person not in this room.'

    def add_song(self, new_song):
        self.list_of_songs.append(new_song)

    def check_person(self, room_list, person_name):
        for person in room_list:
            if person == person_name:
                return person.name
        return 'Person not in this room.'

    def space_left_in_room(self):
        space_left = self.capacity - len(self.list_of_current_guests)
        return space_left

    def current_song(self, room):
        if len(room.list_of_songs) == 0:
            return 'Playlist empty'
        else:
            room.list_of_songs.reverse() ### Different ways of doing this.
            song_on_now = room.list_of_songs[0]
            # index = len(room.list_of_songs) - 1
            # song_on_now = room.list_of_songs[index]
            # song_on_now = room.list_of_songs.pop()
        return song_on_now.song_name
