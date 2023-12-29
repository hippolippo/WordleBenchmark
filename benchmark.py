from .solver_interface import WordleSolver, Human
from typing import Type
from .wordle import *

MAX_GUESS = 100
def benchmark(solver: Type[WordleSolver], dictionary="old_potential_answers"):
    results = dict()
    for word in open(dictionary):
        word = word.strip()
        if word in results: continue
        instance = solver()
        game = Wordle(word)
        score = game.guess(instance.get_first_guess())
        while not game.win:
            if game.guesses >= MAX_GUESS:
                break
            score = game.guess(instance.get_guess(score))
        results[word] = game.guesses
    return results

def print_summary(results: dict):
    amount = 0
    total = 0
    counts = [0]*7
    fails = 0
    for score in results.values():
        amount += 1
        total += score
        counts[min(score-1, 7-1)] += 1
        if score >= MAX_GUESS:
            fails += 1
    print(f"{amount} trials")
    for i, count in enumerate(counts):
        percentage = count/amount*100
        print(f"{i+1 if i != 6 else '7+'} Guess{'es' if i+1 > 1 else ''}: {count} ({percentage:.3f}%)")
    if fails != 0:
        percentage = fails/amount*100
        print(f"{fails} trials reached the guess limit of {MAX_GUESS} ({percentage:.3f}%)")
    print(f"Average: {total/amount}")

if __name__ == "__main__":
    print_summary(benchmark(Human, "small_list"))