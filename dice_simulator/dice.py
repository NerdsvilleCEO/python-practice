#!/usr/bin/python

import random

"""
  Programming problem #1 
  CREDIT: https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

  Game loop (while)
  1. Randomly choose number between 1 and 6
  2. Print chosen number
  3. Ask if you'd like to roll again
  4. Need to set min and max number dice can produce
"""
class Dice():
    def __init__(self, minimum, maximum):
        self._minimum = minimum
        self._maximum = maximum

    @property
    def min(self) -> int: return self._minimum

    @property
    def max(self) -> int: return self._maximum

    def roll(self) -> int:
        return random.randint(self.min, self.max + 1)

# dice = Dice(1, 6)
# print(dice.roll())
# while True:
#     roll_again = input("Would you like to roll again? (Y/n)")
#     if roll_again == 'Y':
#         print(dice.roll())
#     else:
#         break
