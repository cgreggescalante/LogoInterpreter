from turtle import Turtle

from instruction import Instruction


class End(Instruction):
    def execute(self, t: Turtle):
        raise ValueError("End instruction should never be executed")
