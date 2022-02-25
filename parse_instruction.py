import re
from typing import Union

from Instruction.end import End
from Instruction.Subprocess.function import Function
from Instruction.instruction import Instruction
from Instruction.movement import Movement
from Instruction.Subprocess.repeat import Repeat
from Instruction.Subprocess.subprocess import Subprocess
from Instruction.random import Random
from Instruction.turtle_config import TurtleConfig
from context import Context

MOVEMENT_PATTERN = r"(forward|backward|left|right)\s\d+"
REPEAT_PATTERN = r"repeat\s\d+"
FUNCTION_PATTERN = r"to\s[a-z]+"
CALL_PATTERN = r"[a-z]+"
KEYWORDS = {
    "end": End,
    "set-random-position": Random,
    "showturtle": TurtleConfig,
    "st": TurtleConfig,
    "hideturtle": TurtleConfig,
    "ht": TurtleConfig,
    "clean": TurtleConfig,
    "clearscreen": TurtleConfig,
    "cs": TurtleConfig,
    "wrap": TurtleConfig,
    "window": TurtleConfig,
    "fence": TurtleConfig,
    "fill": TurtleConfig
}


def parse_instruction(instruction: str, context: Context) -> Instruction:
    instruction = instruction.strip()
    spl = instruction.split()
    if re.fullmatch(MOVEMENT_PATTERN, instruction):
        return Movement(spl[0], int(spl[1]))
    elif re.fullmatch(REPEAT_PATTERN, instruction):
        return Repeat(int(spl[1]))
    elif re.fullmatch(FUNCTION_PATTERN, instruction):
        return Function(spl[1])
    elif instruction in KEYWORDS:
        return KEYWORDS[instruction](instruction)
    elif re.fullmatch(CALL_PATTERN, instruction):
        return context.get_function(instruction)

    raise ValueError(f"Instruction '{instruction}' not recognized.")


def parse_subprocess(lines: list[str], context: Context, in_process: bool = False) \
        -> Union[tuple[list[Instruction], dict[str, Function]], list[Instruction]]:
    instructions = []
    functions = {}

    while lines:
        instruction = parse_instruction(lines.pop(0), context)
        if isinstance(instruction, End):
            return instructions
        if isinstance(instruction, Subprocess):
            if instruction.definition:
                instruction.instructions = parse_subprocess(lines, context, True)
                instruction.definition = False
                if isinstance(instruction, Function):
                    functions[instruction.name] = instruction
                    context.add_function(instruction)
                else:
                    instructions.append(instruction)
            else:
                instructions.append(instruction)
        else:
            instructions.append(instruction)

    if in_process:
        raise ValueError("Loop not ended")
    else:
        return instructions, functions
