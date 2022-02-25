from typing import Any

from Instruction.instruction import Instruction
from Instruction.Subprocess.subprocess import Subprocess


class Function(Subprocess):
    # TODO: function params
    instructions: list[Instruction]
    required_variables: dict[str, Any]
    name: str

    def __init__(self, name: str):
        super().__init__()
        self.instructions = []
        self.required_variables = {}
        self.name = name

    def add_required_input(self, name):
        self.required_variables[name] = None

    def execute(self, context) -> None:
        if None in self.required_variables.values():
            raise ValueError("Missing required input")
