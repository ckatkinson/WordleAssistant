
"""
The plan here is to test the performance of the Wordle Assistant. One naive approach:
1) For each word in a (perhaps non-proper) subset of the word_list, test the number of guesses
    when always choosing the first suggestion.
    a) need to write my own simulation of Wordle so that I can evaluate guesses. (Done. See simulator.py)
    b) What do I want to record:
        - num_wins
        - num_losses
        - num_tries for each target word
"""

from typing import Dict, List
from simulator import color_string, WordleGame, simulate_game
from word_importer import import_word_list
from numpy import mean

class WordleData():
    """
    Class for collecting data on performance.
    """
    def __init__(self, 
                num_wins: int=0, 
                num_losses: int=0, 
                record: Dict[str, int]={}) -> None:
        self.num_wins = num_wins
        self.num_losses = num_losses
        self.record = record
    def mean_guesses(self):
        guesses = list(self.record.values())
        return mean(guesses)
    def win_percentage(self):
        return self.num_wins/(self.num_wins + self.num_losses)

       


def collect_data(list_of_targets: List[str]=import_word_list()) -> WordleData:
    """
    Simulate a game for every target in list_of_targets and collect stats on wins/losses and attempts. 
    On my computer, runs in about 80 seconds on the full list. No reason to cut it down.
    """
    data = WordleData()
    word_list = list_of_targets
    for target in list_of_targets:
        game = WordleGame(target, 0, [], [], word_list)
        simulate_game(game)
        if game.num_attempts > 6:
            data.num_losses += 1
            data.record[target] = game.num_attempts
        else:
            data.num_wins += 1
            data.record[target] = game.num_attempts
    return data

