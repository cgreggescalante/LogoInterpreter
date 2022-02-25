from abc import ABC, abstractmethod


class Instruction(ABC):

    @abstractmethod
    def execute(self, context) -> None:
        raise NotImplementedError("This method should be overridden by the implementing class.")
