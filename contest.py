import random

names = [
'Eric',
'Brook',
'Kevin',
]

max_range = len(names)

winner_index = random.randrange(0, max_range)

winner = names[winner_index]

print(winner)
