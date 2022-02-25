from enum import Enum
from typing import Union

from Instruction.instruction import Instruction
from context import Context


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

    def execute(self, context: Context) -> None:
        match self.direction:
            case Direction.FORWARD:
                context.turtle.forward(self.distance)
            case Direction.BACKWARD:
                context.turtle.backward(self.distance)
            case Direction.LEFT:
                context.turtle.left(self.distance)
            case Direction.RIGHT:
                context.turtle.right(self.distance)
