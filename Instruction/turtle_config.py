from enum import Enum

from Instruction.instruction import Instruction
from context import Context


# TODO: implement turtle wrap, window, fence, and fill
class TurtleConfigOption(Enum):
    SHOW_TURTLE = 1
    HIDE_TURTLE = 2
    CLEAN = 3
    CLEAR_SCREEN = 4
    WRAP = 5
    WINDOW = 6
    FENCE = 7
    FILL = 8
    PEN_DOWN = 9
    PEN_UP = 10
    PEN_PAINT = 11

    @staticmethod
    def from_str(label: str):
        match label:
            case "showturtle", "st":
                return TurtleConfigOption.SHOW_TURTLE
            case "hideturtle", "ht":
                return TurtleConfigOption.HIDE_TURTLE
            case "clean":
                return TurtleConfigOption.CLEAN
            case "clearscreen", "cs":
                return TurtleConfigOption.CLEAR_SCREEN
            case "wrap":
                return TurtleConfigOption.WRAP
            case "window":
                return TurtleConfigOption.WINDOW
            case "fence":
                return TurtleConfigOption.FENCE
            case "fill":
                return TurtleConfigOption.FILL


class TurtleConfig(Instruction):
    option: TurtleConfigOption

    def __init__(self, option: str):
        super().__init__(option)
        self.option = TurtleConfigOption.from_str(option)

    def execute(self, context: Context) -> None:
        match self.option:
            case TurtleConfigOption.SHOW_TURTLE:
                context.turtle.showturtle()
            case TurtleConfigOption.HIDE_TURTLE:
                context.turtle.hideturtle()
            case TurtleConfigOption.CLEAN:
                context.turtle.clear()
            case TurtleConfigOption.CLEAR_SCREEN:
                context.turtle.clear()
                context.turtle.home()
