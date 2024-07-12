#!/usr/bin/python3
"""
A module that prints a text with 2 new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
""" function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_characters = ['.', '?', ':']
    i = 0
    while i < len(text):
        if text[i] in special_characters:
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
