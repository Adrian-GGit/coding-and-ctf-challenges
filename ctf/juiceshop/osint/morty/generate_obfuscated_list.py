import itertools as it
from itertools import product

FILE_NAME = "pets.txt"
LEET_DICT = {
    'a': '4', 
    'b': '8', 
    'e': '3', 
    # 'g': '9',
    # 'G': '6',
    'i': '1', 
    'l': '1',
    'o': '0', 
    's': '5', 
    't': '7', 
    'z': '2'
}

words_for_gen = [
    "Snuffles",
    "Snowball",
]

def leet_combs(word):
    possibles = []
    for l in word.lower():
        ll = LEET_DICT.get(l, l)
        possibles.append((l,) if ll == l else (l, ll))
    return [''.join(t) for t in product(*possibles)]

def big_letter_combs(word):
   return list(map(''.join, it.product(*(sorted(set((c.upper(), c.lower()))) for c in word))))

with open(FILE_NAME, "a") as file:
    obfuscated_words = []

    for word in words_for_gen:
        for leet in leet_combs(word):
            obfuscated_words += big_letter_combs(leet)
        for obfuscated_word in obfuscated_words:
            file.write(obfuscated_word + "\n")
    file.close()