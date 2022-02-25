from typing import Any, Union

from Instruction.instruction import Instruction


class Print(Instruction):
    output: Union[Any, None]
    variable: Union[str, None]

    def __init__(self, term: str, output: str):
        super().__init__()

        if output.startswith(":"):
            self.output = None
            self.variable = output
        else:
            self.output = output
            self.variable = None

    def execute(self, context) -> None:
        if self.variable:
            if self.variable in context.variables:
                print(context.variables[self.variable])
            else:
                raise ValueError(f"{self.variable} is not defined.")
        else:
            print(self.output)
