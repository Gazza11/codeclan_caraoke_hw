from src.songs import Songs

class Rooms:
    def __init__(self, room_name):
        self.room_name = room_name
        self.list_of_current_guests = []
        self.list_of_songs = []

    def add_song(self, new_song):
        self.list_of_songs.append(new_song)