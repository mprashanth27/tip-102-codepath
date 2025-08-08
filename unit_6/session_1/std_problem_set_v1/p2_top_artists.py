'''
U-nderstand:

i/p = head 
o/p = {artist: freq}

#Constraints:


#Edge cases
1 node
empty node

M-atch:
hash map

P-lan:
iterate thru nodes & inc artist count if present or artist count = 1


I-mplement:

R-eview:

E-valuate:
'''

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    # T = O(n), M = O(k); k be the number of unique artists in the playlist.
    artist_count = {} # ~ M = O(k)
    cur = playlist
    while cur: # ~ T = O(n)
        artist_count[cur.artist] = artist_count.get(cur.artist, 0) + 1
        cur = cur.next

    return artist_count

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))

print(get_artist_frequency(None)) # empty playlist PASS
