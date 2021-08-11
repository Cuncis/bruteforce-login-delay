import requests
import re
from urllib.parse import *

target_url = "https://vuln.cilsy.id/"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))


href_links = extract_links_from(target_url)
for link in href_links:
    link = urljoin(target_url, link)

    if '#' in link:
        link = link.split('#')[0]

    if target_url in link and link not in target_links:
        target_links.append(link)
        print(link)
