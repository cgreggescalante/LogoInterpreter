from Instruction.instruction import Instruction
from context import Context


class Subprocess(Instruction):
    instructions: list[Instruction]
    definition: bool = True

    def execute(self, context: Context) -> None:
        for instruction in self.instructions:
            instruction.execute(context)
