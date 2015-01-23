from queue import Queue

BUTTON_STATES = {
    "PRESSED": True,
    "NOTPRESSED": False,
}


class Floor:
    def __init__(self, level):
        self.level = level
        self.up_button_state = BUTTON_STATES["NOTPRESSED"]
        self.down_button_state = BUTTON_STATES["NOTPRESSED"]

    def button_pressed(person):
        if person.desired_floor > self.level:
            self.up_button_state = BUTTON_STATES["PRESSED"]
        else:
            self.down_button_state = BUTTON_STATES["PRESSED"]


    



