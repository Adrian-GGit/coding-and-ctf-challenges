import requests
import json

from constants import JUICESHOP_URL, NUMBER_OF_PRODUCTS, REL_REVIEWS_PATH, REVIEWS_PATH

with open(REL_REVIEWS_PATH, "w") as file:
    for i in range(NUMBER_OF_PRODUCTS):
        request = requests.get(JUICESHOP_URL + REVIEWS_PATH.format(i))
        response = request.json()
        json_response = json.dumps(response, indent=4)
        file.write(json_response)
    file.close()