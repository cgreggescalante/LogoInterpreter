from Instruction.Subprocess.subprocess import Subprocess
from context import Context


class Repeat(Subprocess):
    repeats: int

    def __init__(self, repeats: int):
        super().__init__()
        self.instructions = []
        self.repeats = repeats

    def execute(self, context: Context):
        for _ in range(self.repeats):
            super().execute(context)
