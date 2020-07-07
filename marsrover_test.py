import pytest

from marsrover import Rover


def test_rover_starts_at_x_0():
    rover = Rover()
    assert rover.position_x == 0


def test_rover_starts_at_y_0():
    rover = Rover()
    assert rover.position_y == 0


def test_rover_moves_up_when_given_int():
    rover = Rover()
    rover.move_up(5)
    assert rover.position_y == 5


def test_rover_moves_down_when_given_int():
    rover = Rover()
    rover.move_down(5)
    assert rover.position_y == -5


def test_rover_moves_right_when_given_int():
    rover = Rover()
    rover.move_right(5)
    assert rover.position_x == 5


def test_rover_moves_left_when_given_int():
    rover = Rover()
    rover.move_left(5)
    assert rover.position_x == -5


def test_rover_moves_in_multiple_directions():
    rover = Rover()
    rover.move_up(5)
    rover.move_down(1)
    rover.move_right(5)
    assert rover.position_y == 4 and rover.position_x == 5
