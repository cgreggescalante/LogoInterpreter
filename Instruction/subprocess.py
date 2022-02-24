from turtle import Turtle

from Instruction.instruction import Instruction


class Subprocess(Instruction):
    instructions: list[Instruction]

    def add_instruction(self, instruction: Instruction) -> None:
        self.instructions.append(instruction)

    def execute(self, t: Turtle):
        for instruction in self.instructions:
            instruction.execute(t)
