from src.song import Song

class Rooms:
    def __init__(self, room_name):
        self.room_name = room_name
        self.list_of_current_guests = []
        self.list_of_songs = []

    def add_person(self, new_person):
        self.list_of_current_guests.append(new_person)

    def remove_person(self, room_list, person):
        if self.check_person(room_list, person) == person.name:
            self.list_of_current_guests.remove(person)
        return 'Person not in this room.'

    def add_song(self, new_song):
        self.list_of_songs.append(new_song)

    def check_person(self, room_list, person_name):
        for person in room_list:
            if person == person_name:
                return person.name
        return 'Person not in this room.'