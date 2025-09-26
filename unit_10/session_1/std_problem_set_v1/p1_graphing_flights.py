"""adjacency_dictionary = {
    0: [1],
    1: [0, 2],
    2: [1, 3], 
    3: [2]        
}

Problem 1: Graphing Flights
U:
     - input: manually input flight names
     - output: airport = key, neighboring airports = value
M: dictionary
"""
flights = {}
flights["JFK"] = ["LAX", "DFW"]
flights["LAX"] = ["JFK"]
flights["DFW"] = ["JFK", "ATL"]
flights["ATL"] = ["DFW"]
print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])