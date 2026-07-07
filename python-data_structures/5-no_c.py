#!/usr/bin/python3
def no_c(my_string):
    letters = list(my_string)
    new_word = []
    for letter in letters:
        if letter.lower() != "c":
            new_word.append(letter)
    return "".join(new_word)
