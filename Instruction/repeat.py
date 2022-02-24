from tkinter import Canvas
from turtle import Turtle

from Instruction.subprocess import Subprocess


class Repeat(Subprocess):
    repeats: int

    def __init__(self, repeats: int):
        self.instructions = []
        self.repeats = repeats

    def execute(self, t: Turtle, c: Canvas):
        for _ in range(self.repeats):
            super().execute(t, c)
