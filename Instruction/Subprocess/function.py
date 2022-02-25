from Instruction.instruction import Instruction
from Instruction.Subprocess.subprocess import Subprocess


class Function(Subprocess):
    # TODO: function params
    instructions: list[Instruction]
    name: str

    def __init__(self, name: str):
        self.instructions = []
        self.name = name
