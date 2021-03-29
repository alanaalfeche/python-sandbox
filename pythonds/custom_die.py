import random 

class CustomDie:
    """
    A custom multi-sided die 

    Instance Variables:
        num_sides
        cur_value
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.cur_value = self.roll()

    def roll(self):
        return random.randrange(1, self.num_sides+1)


my_die = CustomDie(6)
num = [my_die.roll() for _ in range(5)]
print(num)