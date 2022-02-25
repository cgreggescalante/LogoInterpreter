from enum import Enum

from Instruction.instruction import Instruction
from context import Context

RANDOM_TYPES = ["set-random-position"]


class RandomMethod(Enum):
    RANDOM_POSITION = 1
    RANDOM_CHOICE = 2


class Random(Instruction):
    method: RandomMethod

    def __init__(self, method: str):
        match method:
            case "set-random-position":
                self.method = RandomMethod.RANDOM_POSITION
            case "random-pick":
                self.method = RandomMethod.RANDOM_CHOICE

    def execute(self, context: Context) -> None:
        if self.method == RandomMethod.RANDOM_POSITION:
            context.turtle.goto(context.screen.winfo_width(), context.screen.winfo_height())
        else:
            raise NotImplementedError
