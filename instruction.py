from abc import ABC, abstractmethod
from turtle import Turtle


class Instruction(ABC):

    @abstractmethod
    def execute(self, t: Turtle):
        raise NotImplementedError("This method should be overridden by the implementing class.")
