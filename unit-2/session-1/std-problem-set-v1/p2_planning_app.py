'''
U:
i/p= artist:str, schedule: dict
o/p= dict

#edge cases
no i/p , artist not found > {'message': 'Artist not found'}

P:
check if it exists in keys
return 

'''

def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule.keys():
        return festival_schedule[artist]
    else:
        return {'message': 'Artist not found'}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  