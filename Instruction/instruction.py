from abc import ABC, abstractmethod

from context import Context


class Instruction(ABC):

    @abstractmethod
    def execute(self, context: Context) -> None:
        raise NotImplementedError("This method should be overridden by the implementing class.")
