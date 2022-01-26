
from src.word_importer import import_word_list
from src.scoring import word_scores
from src.wordle_filter import filter_from_word_info

class WordleAssistant():
    def __init__(self, word_list=import_word_list()):
        self.guess = input("Input the 5-letter word that you guessed: \n").strip(" '\"")
        self.color = input("Input the colors given back by wordle (for example bygyy): \n").strip(" '\"")
        self.word_list = filter_from_word_info(self.guess, self.color, word_list)
        self.scored_words = word_scores(self.word_list)
    
    def suggestions(self, number=10):
        return [w for w, _ in self.scored_words[:number]]
   
#Initial suggestions:
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
    
    
