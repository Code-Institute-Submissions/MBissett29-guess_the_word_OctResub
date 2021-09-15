"""
This imports the words from the list
of words that was created im the words.py file.
It also allows the run.py file to use the
random file in python
"""
import random
from words import guess_word_list

def pull_the_word():
    """
    Gets the word from the list randomly
    """
    word = random.choice(guess_word_list)
    return word

