#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:45:02 2017

@author: fiv75
"""
from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as init_file:
        return [word.strip() for word in init_file.read().split()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum((LETTER_SCORES.get(letter, 0) for letter in word.upper()))


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value)


if __name__ == "__main__":
    print(max_word_value())
    # run unittests to validate
