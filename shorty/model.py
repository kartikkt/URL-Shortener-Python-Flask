from email.policy import default
from os import link
from typing import Optional

class Link_Schema():
    '''
    A schema of link and provider that is given as request to the api
    | param    | type   | required | description                        |
    |----------|--------|----------|------------------------------------|
    | url      | string | Y        | The URL to shorten                 |
    | provider | string | N        | The provider to use for shortening |
    '''
    url: str 
    url_provider: Optional[str] = None

    def __init__(self, dict):
        self.url = dict["original_url"]
        self.url_provider = dict["url_method"]

class Shortlink():
    '''
    A shortlink schema for resource to be sent as response
    | param    | type   | required | description                        |
    |----------|--------|----------|------------------------------------|
    | url      | string | Y        | The original URL                   |
    | link     | string | Y        | The shortened link                 |
    '''
    url: str 
    link: str 

    def __init__(self, long_url):
        self.url = long_url
        self.link = "URL Shortening Failed"
        
    