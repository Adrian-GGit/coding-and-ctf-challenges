from string import printable
from itertools import product

encoded_flag = open("enc").read()

# decode char1 and char2 separate from each other
def way_one():
    flag = ""
    for i in range(0, len(encoded_flag)):
        character1 = chr((ord(encoded_flag[i]) >> 8))
        character2 = chr(encoded_flag[i].encode('utf-16be')[-1])
        flag += character1
        flag += character2
    return flag

# decode as 16 Byte encoding
def way_two():
    flag = ""
    for i in range(0, len(encoded_flag)):
        bytes = encoded_flag[i].encode('utf-16be')
        decoded_bytes = bytes.decode("utf-8")
        flag += decoded_bytes
    return flag

# brute forcing the chars
def way_three():
    combinations = ["".join(x) for x in product(list(printable), repeat=2)]

    original_string = ""
    current_sign = ""
    for i in list(encoded_flag):
        for index, j in enumerate(combinations):
            j0 = list(j)[0]
            j1 = list(j)[1]
            current_sign = chr((ord(j0) << 8) + ord(j1))
            if current_sign == i:
                original_string += j0 + j1
                break
            else:
                if index == len(combinations) - 1:
                    print(f"[!] No combination found for {i}")
    return original_string

# using bit shift and mask (instead of bit shift you could also use another mask)
def way_four():
    flag = ""
    mask_for_char2 = 0b0000000011111111
    for i in range(0, len(encoded_flag)):
        character1 = chr((ord(encoded_flag[i]) >> 8))
        characters_binary = bin(ord(encoded_flag[i]))
        character2 = chr(int(characters_binary, 2) & mask_for_char2)
        flag += character1
        flag += character2
    return flag


# using hex and ascii
def way_five():
    hex_encoded = ""
    for sign in encoded_flag:
        hex_encoded += hex(ord(sign)).split("0x")[1]
        flag = bytearray.fromhex(hex_encoded).decode()
    return flag

print(way_one())
print(way_two())
print(way_three())
print(way_four())
print(way_five())