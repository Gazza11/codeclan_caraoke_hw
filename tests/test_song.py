import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song('Song A')
        self.song2 = Song('Song B')
        self.song3 = Song('Song C')

    def test_song_has_name(self):
        self.assertEqual('Song A', self.song1.song_name)

    # def test_song_has_duration(self):
    #     self.assertEqual(150, self.song1.duration)
