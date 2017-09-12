import requests

import urllib.parse

class MemesServiceClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_meme(self, meme_id):
        url = urllib.parse.urljoin(self.base_url, f'/meme/{meme_id}')
        response = requests.get(url)
        return response.json()
