from random import randint

class Die:
    """A class representing a die with an arbitrary number of sides. """
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        """Displays the outcome of a die roll 10 times. """
        outcome = []
        for i in range(0,10):
            outcome.append(randint(1, self.sides))
        print(f"Outcome= {outcome}")

twenty_die = Die(20)
twenty_die.roll_die()


