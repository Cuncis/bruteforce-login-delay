import requests


target_url = "google.com/"


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError:
        pass


with open("/opt/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + word
        response = request(test_url)
        if response:
            print(f"[+] Discovered URL -> {test_url}")
