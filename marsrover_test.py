import pytest

from marsrover import Rover


def test_rover_starts_at_x_0():
    rover = Rover()
    assert rover.position_x == 0


def test_rover_starts_at_y_0():
    rover = Rover()
    assert rover.position_y == 0


def test_rover_starts_facing_north():
    rover = Rover()
    assert rover.orientation == "N"


def test_rover_turns_right():
    rover = Rover()
    rover.turn("right")
    assert rover.orientation == "W"


def test_rover_moves_forward_when_given_int():
    rover = Rover()
    rover.move_forward(5)
    assert rover.position_y == 5


def test_rover_moves_back_when_given_int():
    rover = Rover()
    rover.move_back(5)
    assert rover.position_y == -5
