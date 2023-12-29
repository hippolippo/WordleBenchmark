from .solver_interface import WordleSolver, Human
from typing import Type
from .wordle import *
from os import path
from time import time_ns

MAX_GUESS = 20
def benchmark(solver: Type[WordleSolver], dictionary="valid_words"):
    start = time_ns()
    results = dict()
    c = 0
    for word in open(path.join(path.dirname(path.abspath(__file__)), dictionary)):
        c += 1
        if c % 100 == 0: print(c)
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
    time = time_ns() - start
    return time, results

def print_summary(results: (int, dict)):
    time, results = results
    amount = 0
    total = 0
    total_no_fail = 0
    counts = [0]*7
    fails = 0
    for score in results.values():
        amount += 1
        total += score
        if score < MAX_GUESS:
            total_no_fail += score
            counts[min(score-1, 7-1)] += 1
        if score >= MAX_GUESS:
            fails += 1
    print()
    print("Benchmark Report:")
    print(f"{amount} trials")
    for i, count in enumerate(counts):
        percentage = count/amount*100
        print(f"{i+1 if i != 6 else '7+'} Guess{'es' if i+1 > 1 else ''}: {count} ({percentage:.3f}%)")
    if fails != 0:
        percentage = fails/amount*100
        print()
        print(f"{fails} trials reached the guess limit of {MAX_GUESS} ({percentage:.3f}%)")
        print("These were not included in the 7+ category")
    print()
    print(f"Average: {total/amount}")
    print(f"Average (fails removed): {total_no_fail/(amount-fails)}")
    print()
    print(f"Took {time}ns to complete")
    print(f"Average {time//amount}ns/trial")

if __name__ == "__main__":
    print_summary(benchmark(Human, "small_list"))