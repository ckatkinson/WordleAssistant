"""
This defines the function that does most of the work for the Wordle Assistant. filter_from_word_info
filters the word_list according to a guessed 'word' and the 'colors' reported by the Wordle app to give
the remaining possiblities for the answer. 
"""

from typing import List


def filter_from_word_info(word: str, colors: str, word_list: List[str]) -> List[str]:
    """
    Returns the remaining possible words if Wordle tells us that word has
    colors
    """
    word_info = list(zip(enumerate(word), colors))

    for (position, letter), color in word_info:
        if color == "b":

            """
            Tricky case. If all letters in word that are letter are black, then
            we want b_mask to disallow letter from word completely.

            If some letter letters are not black, we need to allow that number
            of letter in word.

            Acheive this by counting the number of letters of letter that are
            not black and allowing than number of letter at other positions.
            """
            black_letters = [
                ((_, l), c) for ((_, l), c) in word_info if (l == letter) and (c == "b")
            ]
            letter_count = word.count(letter)

            num_not_black = letter_count - len(black_letters)
            b_mask = lambda x: (x.count(letter) == num_not_black) and (
                x[position] != letter
            )

            word_list = list(filter(b_mask, word_list))
            pass

        elif color == "g":

            g_mask = lambda x: x[position] == letter
            word_list = list(filter(g_mask, word_list))

        elif color == "y":

            yellow_positions = [
                p for ((p, l), c) in word_info if (l == letter) and (c == "y")
            ]
            num_yell = len(yellow_positions)

            y_mask = lambda x: (all([x[p] != letter for p in yellow_positions])) and (
                x.count(letter) >= num_yell
            )
            word_list = list(filter(y_mask, word_list))

        else:
            raise RuntimeError(
                f"Color must be one of 'b', 'g', or 'y'. Color was '{color}'."
            )

    return list(word_list)
