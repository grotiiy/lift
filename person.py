from random import randrange, choice
from constants import LEVELS


class Person:
    def __init__(self):
        self.current_floor = randrange(0, LEVELS)
        other_floors = [x for x in range(0, LEVELS) if x != self.current_floor]
        self.desired_floor = choice(other_floors)

    def __repr__(self):
        return "%s %s" % (self.current_floor, self.desired_floor)

