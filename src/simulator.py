"""
Wordle simulator: given a target word and a guess, output the color string for that guess given the target
"""

from typing import List
from scoring import word_scores_letter_freq
from word_importer import import_word_list
from wordle_filter import filter_from_word_info


def color_string(guess: str, target: str) -> str:
    """
    Returns Wordle colors for guess given target.
    """
    c_string = ""
    for pos, letter in enumerate(guess):
        if target[pos] == letter:
            c_string += "g"
        elif letter in target:
            c_string += "y"
        else:
            c_string += "b"
    return c_string


class WordleGame:
    """
    Holds state of a Wordle game.
    """

    def __init__(
        self,
        target: str,
        num_attempts: int = 0,
        guesses_made: List[str] = [],
        colors_seen: List[str] = [],
        word_list: List[str] = import_word_list(),
    ) -> None:
        self.target = target
        self.num_attempts = num_attempts
        self.guesses_made = guesses_made
        self.colors_seen = colors_seen
        self.word_list = word_list

    def __repr__(self):
        rep = f"""
        State of Wordle Game:
        Guess made: {self.guesses_made}
        Colors seen: {self.colors_seen}

        Target is: {self.target}
        """
        return rep

    def make_guess(self, guess):
        colors = color_string(guess, self.target)
        self.guesses_made.append(guess)
        self.colors_seen.append(colors)
        self.num_attempts += 1


def simulate_game(game: WordleGame) -> None:
    """
    Uses our scoring based guesser to play through a wordle game.
    """
    # we'll modify working_word_list as we guess. Iterator for speed.
    working_word_list = (w for w, _ in word_scores_letter_freq(game.word_list))
    # while (len(game.colors_seen) == 0) or (game.colors_seen[-1] != 'ggggg'):
    while True:
        try:
            best_word = next(working_word_list)
            # somethings not right in some edge case here. I'll just skip the round when it #happens.
            best_word

            # Play wordle with guess:
            game.make_guess(best_word)

            # Last colors seen:
            last_colors = game.colors_seen[-1]
            if last_colors == "ggggg":
                break

            # filter working list
            filtered_wl = filter_from_word_info(
                best_word, last_colors, working_word_list
            )
            working_word_list = (w for w, _ in word_scores_letter_freq(filtered_wl))
        except StopIteration:
            break
