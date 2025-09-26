from unit_6.linked_list import print_linked_list

class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

song_3 = SongNode("Bad Romance")
song_2 = SongNode("Party Rock Anthem",song_3)
song_1 = SongNode("Uptown Funk", song_2)

#top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

print_linked_list(song_1)