from turtle import Turtle

from Instruction.instruction import Instruction


class Subprocess(Instruction):
    instructions: list[Instruction]
    definition: bool = True

    def execute(self, t: Turtle):
        for instruction in self.instructions:
            instruction.execute(t)
