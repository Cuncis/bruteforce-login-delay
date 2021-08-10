import requests

target_url = "usaa.com"


def request(url):
    try:
        return requests.get(f"https://{url}")
    except requests.exceptions.ConnectionError:
        pass


with open("/opt/seclists/subdomains-top1million-5000.txt", "r") as wordlists:
    for line in wordlists:
        word = line.strip()
        test_url = f"{word}.{target_url}"
        response = request(test_url)
        if response:
            print(f"[+]  Discovered subdomain --> {test_url}")

