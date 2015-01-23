from person import Person
from queue import Queue
from elevator import Elevator
from constants import LEVELS
from floor import Floor

from random import randrange
from time import sleep

elevator = Elevator()
queue = Queue()
floors = [Floor(f) for f in range(LEVELS) ]

while True:
    person = Person()
    queue.append(person)

    for level, level_queue in queue.levels.iteritems():
        print level, level_queue

    sleep(3)
