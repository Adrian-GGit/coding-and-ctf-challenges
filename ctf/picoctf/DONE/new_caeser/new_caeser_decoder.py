import math
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
encoded_flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
# encoded_flag = "jgihjfjgiiioidij"

def b16_decode(encoded):
    dec = ""
    for i in range(0, len(encoded), 2):
        index_in_alphabet = ALPHABET.index(encoded[i])
        index_in_alphabet_2 = ALPHABET.index(encoded[i + 1])
        b = format(index_in_alphabet, '04b')
        b_2 = format(index_in_alphabet_2, '04b')
        binary = b + b_2
        dec += chr(int(binary, 2))
    return dec

# def get_correct_t1(t1_):
#     while t1_ < 0:
#         t1_ = len(ALPHABET) + t1_
#     return t1_

def shift(c, k):
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

for k in string.ascii_lowercase:
# for k in "c":
    decoded_flag = ""
    for c in encoded_flag:
        # t2 = ord(k) - LOWERCASE_OFFSET
        # index_in_alphabet = ALPHABET.index(c)
        # t1_ = index_in_alphabet - t2
        # t1_ = get_correct_t1(t1_)
        # t1 = t1_ + LOWERCASE_OFFSET
        # decoded_flag += chr(t1)
        decoded_flag += shift(c, k)
    if (set(decoded_flag) <= set(ALPHABET)):
        # print(f"Half decoded flag: {decoded_flag}")
        print(f"Decoded flag: {b16_decode(decoded_flag)}")
    else:
        print("NOT")
