from typing import Union

from Instruction.Subprocess.subprocess import Subprocess
from context import Context


class Repeat(Subprocess):
    repeats: Union[str, int]
    variable: bool

    def __init__(self, repeats: str):
        super().__init__()
        self.instructions = []

        try:
            self.repeats = int(repeats)
            self.variable = False
        except ValueError:
            self.repeats = repeats
            self.variable = True

    def execute(self, context: Context):
        if self.variable:
            self.repeats = context.variables[self.repeats]

        for _ in range(int(self.repeats)):
            super().execute(context)
