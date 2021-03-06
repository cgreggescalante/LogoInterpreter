from typing import Any

from Instruction.instruction import Instruction
from Instruction.Subprocess.subprocess import Subprocess


class Function(Subprocess):
    # TODO: function params
    instructions: list[Instruction]
    required_variables: list[str]
    variable_values = list[Any]
    name: str

    def __init__(self, name: str):
        super().__init__()
        self.instructions = []
        self.required_variables = []
        self.variable_values = []
        self.name = name

    def add_param(self, name: str, default: Any = None):
        self.required_variables.append(name)
        self.variable_values.append(default)

    def param_count(self) -> int:
        return len(self.required_variables)

    def set_params(self, values: list[any], context) -> None:
        if len(values) == len(self.variable_values):
            evaluated = []
            for v in values:
                if v.startswith(":"):
                    evaluated.append(context.variables[v])
                else:
                    evaluated.append(v)
            self.variable_values = evaluated
        else:
            raise ValueError(f"Missing required input. Call to '{self.name}' requires {len(self.required_variables)} inputs, {', '.join(self.required_variables)}")

    def execute(self, context) -> None:
        for name, value in zip(self.required_variables, self.variable_values):
            if isinstance(value, str) and value.startswith(":"):
                continue
            context.variables[name] = value
        super().execute(context)
