"""
This algorithm searches for a symbol
- follow the program to input free text and place in each word of this text the very first character
    that is NOT repeated in the analyzed word
- then, from the received set of program symbols, you need to select the first unique one
    (that is, the one that is no longer used in the set) and return it.
>>> find_unique_character("Hello World!")
'H'
>>> find_unique_character("C makes it easy for you to shoot yourself in the foot. C++ makes that harder," \
                        "but when you do, it blows away your whole leg. " \
                        "(с) Bjarne Stroustrup")
'e'
"""

from collections import Counter
import doctest


def find_unique_character(text):
    # Divide the text into separate words
    words = text.split()

    unique_chars = []
    for word in words:
        # Count the number of each character in word
        char_counts = Counter(word)
        # Find the first character that is no longer repeated
        for char in word:
            if char_counts[char] == 1:
                unique_chars.append(char)
                break

    # Count the number of each unique character
    unique_counts = Counter(unique_chars)

    # Find the first unique character that does not occur again
    for char in unique_chars:
        if unique_counts[char] == 1:
            return char

    return None


if __name__ == "__main__":
    doctest.testmod()

