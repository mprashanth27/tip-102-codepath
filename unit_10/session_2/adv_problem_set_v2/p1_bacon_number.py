'''
Understand: 
Input: Adjacency dictionary, string celeb
Output: int (bacon number)

Each key is an actor
Each value is their list of adjacent actors

Match: graph search (BFS)

Cases:
    not celeb -> return -1

Plan:
Start from Kevin Bacon at 0
use a queue (current_nodes)

queue: (kevin bacon, 0)
current_node = queue1.popleft()
if the current node is already visited, move on to next one
queue2.extend(bacon_network[current_node])


actor, distance


use a set to avoid revisiting fully explored nodes
for each actor from queue, we check for their adjacent nodes/neighbours
if we reach the celeb, we return the current distance

Implement

'''
from collections import deque

def bacon_number(bacon_network, celeb):
    # can save checking the entire graph
    if celeb not in bacon_network:
        return -1
    # can save like 2 checks
    if celeb == "Kevin Bacon":
        return 0
    
    visited = set()
    celeb_queue = deque([("Kevin Bacon", 0)])
    while celeb_queue:
        # get current celeb + bacon num
        current, distance = celeb_queue.popleft()
        # skip old celebs
        if current in visited:
            continue
        # if target found return bacon number
        if current == celeb:
            return distance
        # mark celeb visited
        visited.add(current)
        # add (neighbors,distance) tuple to queue
        for person in bacon_network[current]:
            celeb_queue.append((person, distance + 1))
    # if no connection return -1
    return -1



bacon_network = {
    "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon"],
    "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
    "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
    "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
    "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
    "George Clooney": ["Julia Roberts", "Vera Farmiga"],
    "Vera Farmiga": ["George Clooney", "Max Theriot"],
    "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
    "Jennifer Lawrence": ["Max Theriot"]
}

print(bacon_number(bacon_network, "Jennifer Lawrence"))
print(bacon_number(bacon_network, "Tom Cruise"))