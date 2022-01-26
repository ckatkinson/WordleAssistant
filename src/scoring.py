
from src.word_importer import import_word_list

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def letter_frequency(word_list):
    """
    Returns a dict associating to each letter in alphabet the number of occurrences
    of that letter in word_list.
    """
    letter_dict = { letter : 0 for letter in alphabet}
    for word in word_list:
        for let in word:
            letter_dict[let]+=1
    return letter_dict

def letter_relative_frequency(word_list):
    """
    Divides frequency by the number of letters in the entire list
    """
    letter_dict = letter_frequency(word_list)
    for letter in alphabet:
        if len(word_list) == 0:
            raise RuntimeError("Guess/color combination incompatible with word list")
        else:
            letter_dict[letter] = letter_dict[letter]/(5 * len(word_list))
    return letter_dict

def word_scores(word_list):
    """
    Associates a score to each word in the word list. Score is calculated by
    summing the letter frequencies divided by the number of occurrences of the
    letter in the word. List is in decreasing order of score.

    This was just a naive scoring approach. I'd like to work on this more.
    """
    letter_freq = letter_relative_frequency(word_list)
    scores = []
    for word in word_list:
        score = sum([letter_freq[letter]/(word.count(letter)) for letter in word])
        scores.append((word, score))
    return sorted(scores, key=lambda p : p[1], reverse=True)
