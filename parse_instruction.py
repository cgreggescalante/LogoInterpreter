import re

from Instruction.end import End
from Instruction.Subprocess.function import Function
from Instruction.instruction import Instruction
from Instruction.movement import Movement
from Instruction.Subprocess.repeat import Repeat
from Instruction.Subprocess.subprocess import Subprocess
from context import Context

MOVEMENT_PATTERN = r"(forward|backward|left|right)\s\d+"
REPEAT_PATTERN = r"repeat\s\d+"
FUNCTION_PATTERN = r"to\s[a-z]+"
END_PATTERN = r"end"
CALL_PATTERN = r"[a-z]+"


def parse_instruction(instruction: str, context: Context) -> Instruction:
    instruction = instruction.strip()
    spl = instruction.split()
    if re.fullmatch(MOVEMENT_PATTERN, instruction):
        return Movement(spl[0], int(spl[1]))
    elif re.fullmatch(REPEAT_PATTERN, instruction):
        return Repeat(int(spl[1]))
    elif re.fullmatch(FUNCTION_PATTERN, instruction):
        return Function(spl[1])
    elif re.fullmatch(END_PATTERN, instruction):
        return End()
    elif re.fullmatch(CALL_PATTERN, instruction):
        return context.get_function(instruction)

    raise ValueError(f"Instruction '{instruction}' not recognized.")


def parse_subprocess(lines: list[str], context: Context, in_process: bool = False) -> list[Instruction]:
    instructions = []

    while lines:
        instruction = parse_instruction(lines.pop(0), context)
        if isinstance(instruction, End):
            return instructions
        if isinstance(instruction, Subprocess):
            if instruction.definition:
                instruction.instructions = parse_subprocess(lines, context, True)
                if isinstance(instruction, Function):
                    context.add_function(instruction)
                else:
                    instructions.append(instruction)
                instruction.definition = False
            else:
                instructions.append(instruction)
        else:
            instructions.append(instruction)

    if in_process:
        raise ValueError("Loop not ended")
    else:
        return instructions
