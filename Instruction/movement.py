from enum import Enum
from tkinter import Canvas
from turtle import Turtle
from typing import Union

from Instruction.instruction import Instruction


class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4


class Movement(Instruction):
    def __init__(self, direction: str, distance: Union[int, float]):
        match direction:
            case "forward" | "f":
                self.direction = Direction.FORWARD
            case "backward" | "b":
                self.direction = Direction.BACKWARD
            case "left" | "l":
                self.direction = Direction.LEFT
            case "right" | "r":
                self.direction = Direction.RIGHT
        self.distance = distance

    def execute(self, t: Turtle, c: Canvas) -> None:
        match self.direction:
            case Direction.FORWARD:
                t.forward(self.distance)
            case Direction.BACKWARD:
                t.backward(self.distance)
            case Direction.LEFT:
                t.left(self.distance)
            case Direction.RIGHT:
                t.right(self.distance)
