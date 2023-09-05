from abc import ABC, abstractmethod
from typing import Callable

def FunctionBase(ABC):
    @abstractmethod
    def plot(self, ctx):
        pass

    @abstractmethod
    def describe(self) -> str:
        pass

def SIFunction(FunctionBase):
    def __init__(self, func: Callable[[float], float]):
        self.func = func
        
    def plot(self, ctx):
        pass