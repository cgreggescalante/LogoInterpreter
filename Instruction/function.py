from Instruction.instruction import Instruction
from Instruction.subprocess import Subprocess


class Function(Subprocess):
    instructions: list[Instruction]
    name: str

    def __init__(self, name: str):
        self.instructions = []
        self.name = name
