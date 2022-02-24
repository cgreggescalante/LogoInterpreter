from abc import ABC, abstractmethod
from tkinter import Canvas
from turtle import Turtle


class Instruction(ABC):

    @abstractmethod
    def execute(self, t: Turtle, s: Canvas):
        raise NotImplementedError("This method should be overridden by the implementing class.")
