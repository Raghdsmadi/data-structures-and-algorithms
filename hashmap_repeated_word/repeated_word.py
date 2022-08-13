from hash_table.hash import *
import string


def repeated_word(text):
    """
    A function that accepts a string, and returns the first word that occurs more than once.
    Args:
        text (str): Any string.
    """
    ht = HashTable()
    words = str.replace(",","").split(" ")
    for x in words:
        x = x.lower()
        ht.set(x, "1")
        count = len(ht.get(x))
        if count > 1:
            return x
    return "No Repeat"




