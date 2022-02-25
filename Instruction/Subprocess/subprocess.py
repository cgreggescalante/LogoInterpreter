from Instruction.instruction import Instruction


class Subprocess(Instruction):
    instructions: list[Instruction]
    definition: bool = True

    def execute(self, context) -> None:
        for instruction in self.instructions:
            instruction.execute(context)
