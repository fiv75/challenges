from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words_list = f.read().split()
    return words_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_scores = 0
    for current_letter in word.upper():
        for letter, score in LETTER_SCORES.items():
            if letter == current_letter:
                word_scores += score
    return word_scores

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value())

if __name__ == "__main__":
    print(max_word_value())
    
    # run unittests to validate
