from email.policy import default
from os import link
from typing import Optional

class Link_Schema():
    url: str 
    url_provider: Optional[str] = None

    def __init__(self, dict):
        self.url = dict["original_url"]
        self.url_provider = dict["url_method"]

class Shortlink():
    url: str 
    link: str 

    def __init__(self, long_url):
        self.url = long_url
        self.link = "URL Shortening Failed"
        
    