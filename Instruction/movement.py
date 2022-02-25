from enum import Enum

from Instruction.instruction import Instruction
from context import Context


class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4


class Movement(Instruction):
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
        self.distance = float(distance)

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
