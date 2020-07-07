class Rover():
    position_x = None
    position_y = None
    orientation = None

    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.orientation = "N"

    def turn(self, direction):
        if direction == "right":
            if self.orientation == "N":
                self.orientation = "W"
            if self.orientation == "W":
                self.orientation = "S"
            if self.orientation == "S":
                self.orientation = "E"
            if self.orientation == "E":
                self.orientation = "N"
        if direction == "left":
            if self.orientation == "N":
                self.orientation = "E"
            if self.orientation == "E":
                self.orientation = "S"
            if self.orientation == "S":
                self.orientation = "W"
            if self.orientation == "W":
                self.orientation = "N"

    def move_forward(self, number_of_steps):
        self.position_y += number_of_steps

    def move_back(self, number_of_steps):
        self.position_y += -number_of_steps
