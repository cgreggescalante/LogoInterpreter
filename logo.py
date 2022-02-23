import re
import time
import turtle

from end import End
from instruction import Instruction
from movement import Movement
from repeat import Repeat


MOVEMENT_PATTERN = r"(forward|backward|left|right)\s\d+"
REPEAT_PATTERN = r"repeat\s\d+"
END_PATTERN = r"end"


def parse_instruction(instruction: str) -> Instruction:
    if re.fullmatch(MOVEMENT_PATTERN, instruction):
        spl = instruction.split()
        return Movement(spl[0], int(spl[1]))
    if re.fullmatch(REPEAT_PATTERN, instruction):
        spl = instruction.split()
        return Repeat(int(spl[1]))
    if re.fullmatch(END_PATTERN, instruction):
        return End()

    raise ValueError(f"Instruction '{instruction}' not recognized.")


class Logo:
    def __init__(self):
        self.instructions: list[Instruction] = []
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

        repeat_stack = []

        while lines:
            if lines[0]:
                next_instruction = parse_instruction(lines.pop(0))
                print(next_instruction)

                if not self.uses_turtle and isinstance(next_instruction, Movement):
                    self.uses_turtle = True
                elif isinstance(next_instruction, Repeat):
                    repeat_stack.append(next_instruction)
                    continue

                if repeat_stack:
                    if isinstance(next_instruction, End):
                        if len(repeat_stack) > 1:
                            repeat_stack[-2].add_instruction(repeat_stack.pop())
                        else:
                            self.instructions.append(repeat_stack.pop())
                    else:
                        repeat_stack[-1].add_instruction(next_instruction)
                else:
                    self.instructions.append(next_instruction)

        if repeat_stack:
            raise ValueError(f"{len(repeat_stack)} loop(s) was not closed.")

    def execute(self):
        if self.program_title:
            print(f"Executing {self.program_title}.")
        if self.uses_turtle:
            t = turtle.Turtle()
        else:
            t = None

        for instruction in self.instructions:
            instruction.execute(t)

        time.sleep(10)


if __name__ == '__main__':
    logo = Logo()

    logo.compile("example1.logo")

    logo.execute()
