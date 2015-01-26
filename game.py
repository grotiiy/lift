from person import Person
from queue import Queue
from elevator import Elevator
from constants import LEVELS
from floor import Floor

from random import randrange
from time import sleep
import sys

elevator = Elevator()
queue = Queue()
floors = [Floor(f) for f in range(LEVELS) ]

def clear():
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()

def floor_display(level, level_queue, elevator):
    display = "------------------------------\n"
    display += "{:<30}\n".format(level_queue)
    if elevator.current_floor == level:
        display += "{:<30}\n".format(elevator)
    else:
        display += "{:<30}\n{:<30}\n{:<30}\n".format(" ", " ", " ")
    display += "------------------------------\n"
    return display
    
while True:
    clear()
    person = Person()
    if not randrange(0, 5):
        queue.append(person)
    
    for level, level_queue in queue.levels.iteritems():        
        print floor_display(level, level_queue, elevator)


    while elevator.can_enter and queue.levels[elevator.current_floor]:
        elevator.add_to_payload(queue.levels[elevator.current_floor].pop(0))

    elevator.turn(queue)

    print elevator.payload
    print "total:", elevator.transported
#    sleep(0.1)
