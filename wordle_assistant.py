#!/usr/bin/python3

from typing import List
from src.word_importer import import_word_list
from src.scoring import word_scores
from src.wordle_filter import filter_from_word_info

class WordleAssistant():
    """
    This class asks for input when initialized and then packages the suggestion mechanism.
    """
    def __init__(self, word_list: List[str]=import_word_list()) -> None:
        self.guess = input("Input the 5-letter word that you guessed: \n").strip(" '\"")
        self.color = input("Input the colors given back by wordle (for example bygyy): \n").strip(" '\"")
        self.word_list = filter_from_word_info(self.guess, self.color, word_list)
        self.scored_words = word_scores(self.word_list)
    
    def suggestions(self, number: int=10) -> List[str]:
        return [w for w, _ in self.scored_words[:number]]
   
#This is the 'interactive' part of the program. Is this (ie the while loop) a good idea? Probably not, but I'm still learning.
#Initial suggestions:
def main():
    wl = import_word_list()
    scored = word_scores(wl)
    print("\nHere are some suggested guesses: ")
    print([w for w, _ in scored[:10]])

    w = WordleAssistant()
    print(w.suggestions())
    # loop until we're done
    while True:
        cont = input("Would you like to keep going ([y]/n)? ")
        if cont=='n':
            break
        
        w = WordleAssistant(filter_from_word_info(w.guess, w.color, w.word_list))
        
        print("\nHere are some suggested guesses: ")
        print(w.suggestions())

if __name__ == "__main__":
    main()  
    
    
