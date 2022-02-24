import time
import turtle

from Instruction.function import Function
from Instruction.instruction import Instruction
from parse_instruction import parse_subprocess


class Logo:
    instructions: list[Instruction]
    functions: dict[str, Function]
    uses_turtle: bool
    program_title: str

    def __init__(self):
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

        self.instructions = parse_subprocess(lines, self.functions)

    def execute(self):
        if self.program_title:
            print(f"Executing {self.program_title}.")

        t = turtle.Turtle()

        print(self.functions['square'].instructions)
        print(self.instructions)

        for instruction in self.instructions:
            instruction.execute(t)

        time.sleep(10)


if __name__ == '__main__':
    logo = Logo()

    logo.compile("example1.logo")

    logo.execute()
