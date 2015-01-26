from constants import LEVELS

class Queue:
    def __init__(self):
        self.levels = {}
        for level in range(LEVELS):
            self.levels[level] = []
    
    def append(self, person):
        self.levels[person.current_floor].append(person)

    @property
    def is_empty(self):
        waiting = 0
        for level in range(LEVELS):
            waiting += len(self.levels[level])
        
        return not waiting
