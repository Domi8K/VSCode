"""
# more specific and shorter is

from random import choice

coin = choice(['head', 'tail'])
print(coin)
"""

import random # which imports everything in the random module, this is more general

# this flips a coin
coin = random.choice(['heads','tails'])
print(coin)

# this picks a random number
number = random.randint(1, 10) # a random number between 1 and 10 inclusive
print(number)

#this performs a shuffle
cards = ['king', 'jack', 'queen', 'ace']
random.shuffle(cards)
# using print(cards) also works fine, but gives the ugly python syntax of lists with commas and single quotes...
for card in cards:
    print(card)