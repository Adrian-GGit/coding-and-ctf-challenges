import requests
import re

url = "https://7adf4975944a406a3c4d00e2-greetings.challenge.master.cscg.live:31337/"
endpoint = "login.php"
invalid = "Invalid username or password."

login_payload = {
    "username": "test",
    "password": "testtest",
}

res = requests.post(
    url=url + endpoint,
    data=login_payload,
)
invalid = re.findall(
    invalid, res.text
)
if invalid:
    print(f"[!] Invalid creds for {login_payload.get('username')}")
else:
    print(f"[*] Valid login for {login_payload.get('username')}")