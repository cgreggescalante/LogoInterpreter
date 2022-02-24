from tkinter import Canvas
from turtle import Turtle

from Instruction.instruction import Instruction


class Subprocess(Instruction):
    instructions: list[Instruction]
    definition: bool = True

    def execute(self, t: Turtle, c: Canvas) -> None:
        for instruction in self.instructions:
            instruction.execute(t, c)
