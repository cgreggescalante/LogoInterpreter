import re
import time
import turtle

from Instruction.end import End
from Instruction.function import Function
from Instruction.instruction import Instruction
from Instruction.movement import Movement
from Instruction.repeat import Repeat


MOVEMENT_PATTERN = r"(forward|backward|left|right)\s\d+"
REPEAT_PATTERN = r"repeat\s\d+"
FUNCTION_PATTERN = r"to\s[a-z]+"
END_PATTERN = r"end"


def parse_instruction(instruction: str) -> Instruction:
    spl = instruction.split()
    if re.fullmatch(MOVEMENT_PATTERN, instruction):
        return Movement(spl[0], int(spl[1]))
    elif re.fullmatch(REPEAT_PATTERN, instruction):
        return Repeat(int(spl[1]))
    elif re.fullmatch(FUNCTION_PATTERN, instruction):
        return Function(spl[1])
    elif re.fullmatch(END_PATTERN, instruction):
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

        sub_stack = []

        while lines:
            if lines[0]:
                next_instruction = parse_instruction(lines.pop(0))
                print(next_instruction)

                if not self.uses_turtle and isinstance(next_instruction, Movement):
                    self.uses_turtle = True
                elif isinstance(next_instruction, Repeat) or isinstance(next_instruction, Function):
                    sub_stack.append(next_instruction)
                    continue

                if sub_stack:
                    if isinstance(next_instruction, End):
                        if len(sub_stack) > 1:
                            sub_stack[-2].add_instruction(sub_stack.pop())
                        else:
                            self.instructions.append(sub_stack.pop())
                    else:
                        sub_stack[-1].add_instruction(next_instruction)
                else:
                    self.instructions.append(next_instruction)

        if sub_stack:
            raise ValueError(f"{len(sub_stack)} loop(s) was not closed.")

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
