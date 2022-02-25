from typing import Any

from Instruction.instruction import Instruction


class Variable(Instruction):
    name: str
    value: Any

    def __init__(self, name: str, value: Any):
        super().__init__()

        self.name = name
        self.value = value

    def execute(self, context) -> None:
        raise ValueError("Variable should not be executed.")
