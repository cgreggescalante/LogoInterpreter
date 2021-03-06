import sys
import time

from Instruction.Subprocess.function import Function
from Instruction.instruction import Instruction
from context import Context
from parse_instruction import parse_subprocess


class Logo:
    # TODO: create context variable for functions and variables
    context: Context
    instructions: list[Instruction]
    functions: dict[str, Function]
    uses_turtle: bool
    program_title: str

    def __init__(self):
        self.context = Context()
        self.instructions = []
        self.functions = {}
        self.uses_turtle = False
        self.program_title = ""

    def compile(self, source: str):
        if isinstance(source, str):
            return self.compile_from_file(source)

        return None

    def compile_from_file(self, filename: str):
        self.program_title = filename.split(".")[0]

        with open(filename, 'r') as source:
            lines = list(map(lambda s: s.strip(), source.readlines()))

        self.compile_lines(lines)

    def compile_lines(self, lines: list[str]) -> None:
        # Filter out empty lines
        lines = [a for a in lines if a]

        self.instructions, self.functions = parse_subprocess(lines, self.context)

    def execute(self):
        if self.program_title:
            print(f"Executing {self.program_title}.")

        for instruction in self.instructions:
            instruction.execute(self.context)

        time.sleep(10)


if __name__ == '__main__':
    logo = Logo()

    if len(sys.argv) > 1:
        logo.compile(sys.argv[1])
    else:
        logo.compile("examples/output.logo")

    logo.execute()
