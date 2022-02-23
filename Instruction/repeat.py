from turtle import Turtle

from Instruction.instruction import Instruction


class Repeat(Instruction):
    instructions: list[Instruction]
    repeats: int

    def __init__(self, repeats: int):
        self.instructions = []
        self.repeats = repeats

    def add_instruction(self, instruction: Instruction):
        self.instructions.append(instruction)

    def execute(self, t: Turtle):
        for _ in range(self.repeats):
            for instruction in self.instructions:
                instruction.execute(t)
