
from operator import itemgetter

people = [
    {"name": "Ed", "height": 176},
    {"name": 'Andrew', "height": 188},
    {"name": 'Kath', "height": 170}
]


get_height = itemgetter("height") 

print(sorted(people, key=get_height))