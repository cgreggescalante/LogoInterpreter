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
    direction: Direction
    distance: Union[int, None]
    variable: Union[str, None]

    def __init__(self, direction: str, distance: str):
        super().__init__()
        match direction:
            case "forward" | "fd":
                self.direction = Direction.FORWARD
            case "backward" | "bk":
                self.direction = Direction.BACKWARD
            case "left" | "lt":
                self.direction = Direction.LEFT
            case "right" | "rt":
                self.direction = Direction.RIGHT

        if distance.startswith(":"):
            self.variable = distance
            self.distance = None
        else:
            self.distance = int(distance)
            self.variable = None

    def get_distance(self, context: Context) -> int:
        if self.variable:
            return int(context.variables[self.variable])
        return self.distance

    def execute(self, context: Context) -> None:
        distance = self.get_distance(context)

        match self.direction:
            case Direction.FORWARD:
                context.turtle.forward(distance)
            case Direction.BACKWARD:
                context.turtle.backward(distance)
            case Direction.LEFT:
                context.turtle.left(distance)
            case Direction.RIGHT:
                context.turtle.right(distance)
