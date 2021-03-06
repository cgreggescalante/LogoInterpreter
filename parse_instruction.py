from typing import Union

from Instruction.Subprocess.function import Function
from Instruction.Subprocess.repeat import Repeat
from Instruction.instruction import Instruction
from Instruction.movement import Movement
from Instruction.random import Random
from Instruction.print import Print
from Instruction.turtle_config import TurtleConfig
from Instruction.variable import Variable
from context import Context

ZERO_ARG = {
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

ONE_ARG = {
    "forward": Movement,
    "fd": Movement,
    "backward": Movement,
    "bk": Movement,
    "left": Movement,
    "lt": Movement,
    "right": Movement,
    "rt": Movement,
    "print": Print
}


def parse_instruction(source: str, context: Context) -> Union[Instruction, tuple[Instruction, str]]:
    source = source.strip()
    source, term = get_term(source)

    if term == "repeat":
        source, term = get_term(source)
        repeat = Repeat(term)

        source, term = get_term(source)

        while source and not source.startswith("]"):
            next_instruction, source = parse_instruction(source, context)
            repeat.add_instruction(next_instruction)

        source = source[2:]
        if source:
            return repeat, source
        return repeat

    elif term == "to":
        source, name = get_term(source)
        function = Function(name)

        while source.startswith(":"):
            source, current_term = get_term(source)
            function.add_param(current_term)

        while source and not source.startswith("end"):
            next_instruction, source = parse_instruction(source, context)
            function.add_instruction(next_instruction)

        if source == "end":
            return function
        elif not source:
            raise ValueError("Expected 'end' after function definition")

    elif term.startswith(":"):
        source, param = get_term(source)
        if source:
            return Variable(term, param), source
        return Variable(term, param)

    elif term in ZERO_ARG:
        if source:
            return ZERO_ARG[term](term), source
        return ZERO_ARG[term](term)

    elif term in ONE_ARG:
        source, param = get_term(source)
        if source:
            return ONE_ARG[term](term, param), source
        return ONE_ARG[term](term, param)

    elif term in context.functions:
        function = context.functions[term]
        if function.param_count():
            params = []
            for _ in range(function.param_count()):
                source, param = get_term(source)
                params.append(param)
            function.set_params(params, context)
        if source:
            return function, source
        return function

    raise ValueError(f"Instruction '{term}' not recognized.")


def get_term(instruction: str) -> tuple[str, str]:
    if " " not in instruction:
        return "", instruction
    spc_index = instruction.find(" ")
    if instruction.startswith('"'):
        while spc_index > -1 and instruction[spc_index - 1] == "\\":
            spc_index = instruction.find(" ", spc_index + 1)
        if spc_index == -1:
            return "", instruction[1:].replace("\\", "")
        else:
            return instruction[spc_index + 1:], instruction[:spc_index].replace("\\", "")
    return instruction[spc_index + 1:], instruction[:spc_index]


def parse_subprocess(lines: list[str], context: Context, in_process: bool = False) \
        -> Union[tuple[list[Instruction], dict[str, Function]], list[Instruction]]:
    instructions = []
    functions = {}

    while lines:
        instruction = parse_instruction(lines.pop(0), context)
        if isinstance(instruction, Function) and instruction.definition:
            if instruction.definition:
                instruction.definition = False
                functions[instruction.name] = instruction
                context.add_function(instruction)
        elif isinstance(instruction, Variable):
            context.variables[instruction.name] = instruction.value
        else:
            instructions.append(instruction)
    if in_process:
        raise ValueError("Loop not ended")
    else:
        return instructions, functions
