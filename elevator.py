from constants import LEVELS, ELEVATOR_SIZE

from time import sleep
from random import randrange

class Elevator:

    def __init__(self, initial=0):
        self.current_floor = initial
        self.queue = []
        self.payload = []
        self.transported = 0

    @property
    def is_empty(self):
        return not self.payload

    @property
    def can_enter(self):
        return len(self.payload) < ELEVATOR_SIZE
        
    def add_to_payload(self, person):
        self.add_to_queue(person.desired_floor)
        self.payload.append(person)

    def add_to_queue(self, desired_floor):
        if not desired_floor in self.queue:
            self.queue.append(desired_floor)

    def will_stop(self, floor):
        return floor in self.queue
    
    @property
    def direction(self):
        if not len(self.queue):
            return "-"
        if self.queue[0] > self.current_floor:
            return "U"
        if self.queue[0] < self.current_floor:
            return "D"
        
    @property
    def floor_lights(self):
        display = ""
        for level in range(LEVELS):
            if level in self.queue:
                display += str(level)
            else:
                display += " "

        return display

    @property
    def display_payload(self):
       return  " ".join(["P" for x in self.payload])

    def floor_reached(self):
        for person in self.payload:
            if self.current_floor == person.desired_floor:
                self.payload.remove(person)
                self.transported +=1

    def go_to(self, floor_number):
        sleep(0.1)
        self.current_floor = floor_number
        self.floor_reached()

    def turn(self, queue):
        sleep(0.1)
        if self.queue:
            self.go_to(self.queue.pop(0))
        if self.is_empty:
            if not queue.is_empty:
                self.go_to(randrange(LEVELS))



    def __repr__(self):
        display =  "[{:^3}|{:^3}|{:^3}]\n"
        display += "[{:^11s}]\n"
        display += "[{:^11s}]"
        display = display.format(self.direction,
                             self.current_floor,
                             self.direction,
                             self.floor_lights,
                             self.display_payload,
                             )

        return display
