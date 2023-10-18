import requests
import json

from constants import JUICESHOP_URL, REL_FILE_PATH, VULN_PATH

file_name = input("Filename to save output in: ")
sqli = input("SQLI: ")
request = requests.get(JUICESHOP_URL + VULN_PATH + sqli)
response = request.json()

with open(REL_FILE_PATH + file_name, "w") as file:
    json_response = json.dumps(response, indent=4)
    file.write(json_response)
    file.close()