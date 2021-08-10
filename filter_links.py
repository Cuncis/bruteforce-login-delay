import requests
import re
from urllib.parse import urljoin


target_url = "https://communities.usaa.com/"


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))


href_links = extract_links_from(target_url)

for link in href_links:
    link = urljoin(target_url, link)

    if target_url in link:
        print(link)
