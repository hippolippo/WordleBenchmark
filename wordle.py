GRAY = 0
YELLOW = 1
GREEN = 2
KEYS = {GRAY: "\x1b[40;37m", YELLOW: "\x1b[43;37m", GREEN: "\x1b[42;37m"}
NORMAL = "\x1b[0m"

class Wordle:

    class Score:

        def __init__(self, word: str, real_word: str):
            if len(word) != len(real_word):
                raise ValueError(f"Provided word \"{word}\" is {len(word)} characters, but should be {len(real_word)} characters")
            self.word = word
            self.score = [GREEN if letter == real_letter else GRAY for letter, real_letter in zip(word, real_word)]
            # Add yellows where appropriate
            # The number of highlighted tiles of a letter should match the amount of that letter in the real word and are added left-to-right
            letters = [letter for letter, color in zip(real_word, self.score) if color == GRAY]
            for i in range(len(word)):
                if self.score[i] == GREEN: continue
                if word[i] in letters:
                    letters.remove(word[i])
                    self.score[i] = YELLOW
            self.win = word == real_word

        def __repr__(self):
            out = ""
            for letter, color in zip(self.word, self.score):
                out += KEYS[color] + letter
            out += NORMAL + "\n"
            return out



    def __init__(self, word: str):
        self.word = word
        self.guesses = 0
        self.win = False

    def guess(self, word: str) -> Score:
        self.guesses += 1
        score = Wordle.Score(word, self.word)
        self.win = score.win
        return score