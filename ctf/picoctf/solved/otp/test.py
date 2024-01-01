def encode_char_with_lambda(string, key):
    return list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), string, key))

def encoded_char_with_for_loop(string, key):
    encoded = ""
    for c, k in zip(string, key):
        print(ord(c) ^ k)
    return encoded

string = "alhamdulilah"
key = b"Qsdfjkloetesttest"
print(encoded_char_with_for_loop(string, key))
print(encode_char_with_lambda(string, key))