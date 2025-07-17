# Group 64 code
"""
Problem 1: Blueprint Approval Process
You are in charge of overseeing the blueprint approval process for various architectural designs. Each blueprint has a specific complexity level, represented by an integer. Due to the complex nature of the designs, the approval process follows a strict order:

Blueprints with lower complexity should be reviewed first.
If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
Your task is to simulate the blueprint approval process using a queue. You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

Return the order in which the blueprints are approved.

Understand:
    input: list of integers
    output: sorted list of integers

#Constraints:
Your task is to simulate the blueprint approval process using a queue

Planning: sorting the blueprints in with a queue
    # queue: every blueprint - add it to the queue
        pop and push until the last element in the queue is smaller than curr num but the top eleent > num
        add curr num to the end of the queue
        continue the rest of the pop and push
    
        curr > greatest in queue -> add to the end of the queue

[3 5] -> add 2
top queue: 3 -> pop 3 , append to the end [3 5 2] -> [5 2 3] -> [2 3 5]
add 1 -> [2 3 5 1] -> [3 5 1 2] -> [5 1 2 3] -> [1 2 3 5]
 
to add 4 -> [1 2 3 5] -> [2 3 5 1] -> [3 5 1 2] -> [ 5 1 2 3]
this where we add 4 [ 5 1 2 3 4] -> [ 1 2 3 4 5]  
"""
from collections import deque

def blueprint_approval(blueprints):
    queue = deque()

    curr_max = float("-inf")

    for complex in blueprints:
        if complex >= curr_max:
            queue.append(complex)
            curr_max = complex
        else:
            # rotate until end is the place to append next blueprints
            # this point it hit a loop 
            # rotate until the last element in queue < complex
            # no smaller element?
            # rotate until first element is greater complex
            # rotate while the first element is smaller complex
            # first element => next element after complex
            while queue[0] < complex:
                temp = queue.popleft()
                queue.append(temp)

            queue.append(complex)

            # do the res of rotations to go back to sorted list
            while queue[0] > queue[-1]:
                temp = queue.popleft()
                queue.append(temp)
    
    return queue

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 

"""
[3] -> curr max = 3
comp : 5 -> [3 5] curr max 5 
comp : 2 -> [3 5]  

"""

# solution example
# [1, 2, 3, 4, 5]
# [2, 4, 5, 6, 7]


