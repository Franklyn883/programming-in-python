from random import randint

class Die():
    """A simple model of a die."""
    def __init__(self):
        self.sides = 6
        
    def roll_die(self):
        number = randint(1,self.sides)
        print(number)
        
new_die = Die()
die_10 = Die()
die_10.sides = 10
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
print("\n Roll dices with 10 sides.\n")
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()