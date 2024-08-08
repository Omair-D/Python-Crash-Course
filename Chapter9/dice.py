from random import randint

class Die:
    """Class simulating real world dice"""
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        roll = randint(1, self.sides)
        print(f"\n{self.sides} sided die:")
        print(f"You rolled a: {roll}")
    
die1 = Die()
# Roll a six sided dice ten times
for i in range(1, 11):
    die1.roll_die()

# Make a 10 sided die and roll ten times
die2 = Die(sides=10)
for i in range(1, 11):
    die2.roll_die()

# Make a 20 sided die and roll ten times
die3 = Die(sides=20)
for i in range(1, 11):
    die3.roll_die()