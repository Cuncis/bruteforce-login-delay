import requests
import re

target_url = "communities.usaa.com/"


def request(url):
    try:
        return requests.get(f"https://{url}")
    except requests.exceptions.ConnectionError:
        pass


response = request(target_url)

href_links = re.findall('(?:href=")(.*?)"', str(response.content))

print(href_links)
