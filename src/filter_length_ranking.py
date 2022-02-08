from typing import List, Dict
from wordle_filter import filter_from_word_info
from simulator import color_string
from word_importer import import_word_list

"""
Idea for another ranking of words:

For each target t and for each guess g, compute the filtered wordle list assuming t is target given guess g. Collect as a Dict[ guesses, [filtered list length] ]

Rank words by average length of filtered list length.
"""

#This is very slow. How can we speed it up??? ~6 minutes for 10 words
# Playing around with filter_from_word_info, noted that about 2/3 of the time is spent filtering.
def build_list_length_dict( word_list: List[str]=import_word_list()) -> Dict[str, List[int]]:
    dict = {word : [] for word in word_list}
    for guess in word_list[:10]:
        print(f"Working on {guess}")
        for target in word_list:
            colors = color_string(guess, target)
            filtered_length = len(filter_from_word_info(guess, colors, word_list))
            dict[guess].append(filtered_length)
    return dict

def build_list_length_dict2( word_list: List[str]=import_word_list()) -> Dict[str, List[int]]:
    c = color_string
    dict = {g : [len(filter_from_word_info( g, c(g, t), word_list)) for t in word_list] for g in word_list[:10]}
    return dict

#Yep, this just takes a long time. Only hope is probably to speed up filter_from_word_info
#This is just a test for one word. :(
def list_lengths_one(w, wl=import_word_list()):
    c = color_string
    return [len(filter_from_word_info(w, c(w,t),wl)) for t in wl]