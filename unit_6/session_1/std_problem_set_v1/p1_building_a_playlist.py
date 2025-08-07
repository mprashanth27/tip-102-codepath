from unit_6.linked_list import print_linked_list

class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next
		
top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

print_linked_list(top_hits_2010s)