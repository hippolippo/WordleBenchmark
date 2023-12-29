from .wordle import Wordle
from abc import ABC, abstractmethod

class WordleSolver(ABC):
    # Interface for wordle solver to benchmark
    def __init__(self):
        pass

    @abstractmethod
    def get_guess(self, score: Wordle.Score) -> str:
        pass

    @abstractmethod
    def get_first_guess(self) -> str:
        pass

# An example of how to implement WordleSolver
class Human(WordleSolver):
    def __init__(self):
        print("Welcome to Wordle!")
    
    def get_guess(self, score: Wordle.Score) -> str:
        print(score)
        return self.get_first_guess()
    
    def get_first_guess(self) -> str:
        guess = input("Guess a Word: ")
        if len(guess) != 5:
            print("Must use 5 letters!")
            return self.get_first_guess()
        return guess
