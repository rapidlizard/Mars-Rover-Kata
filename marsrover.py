class Rover():
    position_x = None
    position_y = None

    def __init__(self):
        self.position_x = 0
        self.position_y = 0

    def move_up(self, number_of_steps):
        self.position_y += number_of_steps

    def move_down(self, number_of_steps):
        self.position_y += -number_of_steps

    def move_right(self, number_of_steps):
        self.position_x += number_of_steps

    def move_left(self, number_of_steps):
        self.position_x += -number_of_steps
