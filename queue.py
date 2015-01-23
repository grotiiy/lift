from constants import LEVELS

class Queue:
    def __init__(self):
        self.levels = {}
        for level in range(LEVELS):
            self.levels[level] = []
    
    def append(self, person):
        self.levels[person.desired_floor].append(person)

