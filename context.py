import turtle
from turtle import Turtle, Screen
from typing import Any, Union

from Instruction.Subprocess.subprocess import Subprocess


class Context:
    variables: dict[str, Any]
    functions: dict[str, Subprocess]
    turtle: Union[Turtle, None]
    screen: Screen

    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()

    def add_function(self, function: Subprocess) -> None:
        self.functions[function.name] = function

    def get_function(self, function_name: str) -> Subprocess:
        return self.functions[function_name]

    def set_turtle(self, turtle: Turtle) -> None:
        self.turtle = turtle

    def set_screen(self, screen: Screen) -> None:
        self.screen = screen
