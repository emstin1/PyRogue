class DiceRoller:
    import random
    """rolls the dice"""
    def __init__(self, rolls, sides):
        self.rolls = rolls
        self.sides = sides

    def roll(self):
        """Generator that coughs up rollsDsides dice pool"""
        for x in range(self.rolls):
            yield self.random.randrange(self.sides) + 1
