import time
import turtle

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

        self.instructions = parse_subprocess(lines, self.context)

    def execute(self):
        if self.program_title:
            print(f"Executing {self.program_title}.")

        t = turtle.Turtle()
        s = turtle.Screen()

        self.context.set_turtle(t)
        self.context.set_screen(s)

        print(self.functions['square'].instructions)
        print(self.instructions)

        for instruction in self.instructions:
            instruction.execute(self.context)

        time.sleep(10)


if __name__ == '__main__':
    logo = Logo()

    logo.compile("example1.logo")

    logo.execute()
