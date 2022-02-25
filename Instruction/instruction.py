from abc import ABC, abstractmethod


class Instruction(ABC):
    def __init__(self, instruction: str = None):
        pass

    @abstractmethod
    def execute(self, context) -> None:
        raise NotImplementedError("This method should be overridden by the implementing class.")
