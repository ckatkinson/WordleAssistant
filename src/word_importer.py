
""" 
sgb-words.txt is from here:
https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
"""

from typing import TextIO, List

def import_word_list(file: TextIO ='./sgb-words.txt') -> List[str]:
    """
    Import the dictionary of 5-letter words. Returns a list
    """
    with open(file) as the_file:
        word_list = the_file.readlines()
        word_list = [line.rstrip() for line in word_list]
    return word_list
