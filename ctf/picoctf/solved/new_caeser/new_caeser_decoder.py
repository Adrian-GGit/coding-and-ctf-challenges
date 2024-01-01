import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
encoded_flag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

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


def shift(c, k):
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

for k in string.ascii_lowercase:
    decoded_flag = ""
    for c in encoded_flag:
        decoded_flag += shift(c, k)
    if (set(decoded_flag) <= set(ALPHABET)):
        print(f"Decoded flag: {b16_decode(decoded_flag)}")
    else:
        print("-")
