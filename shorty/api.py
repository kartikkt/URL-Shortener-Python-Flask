import contextlib
from http import HTTPStatus
import json
from operator import imod
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen
from flask import Blueprint, jsonify, render_template
from flask.globals import request
from urllib3 import Retry
from shorty.model import Link_Schema, Shortlink
import requests

api = Blueprint('api', __name__)
response_status = None

@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    response = dict(request.form)
    print(response)
    shortlink = get_shortened_url(response)
    response_for_shortUrl = json.loads(json.dumps(shortlink.__dict__))
    
                   
    #return  jsonify(json.dumps(shortlink.__dict__))
    return render_template('link.html', title="page", jsonfile=response_for_shortUrl,
                             response_status = response_status)
    
@api.errorhandler(404)
def page_not_found(e):
    return "Code : " + str(e.code) + " => " + HTTPStatus(e.code).phrase

@api.route("/")
def index():
    return render_template("index.html")

def get_shortened_url(response):

    long_url = response['original_url']
    if 'url_method' not in response.keys() or response['url_method'] == "bit.ly" :
        return bitly(long_url)
    elif response['url_method'] == "tiny_url":
        return tiny_url(long_url)
        
def tiny_url(long_url):
    global response_status
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': long_url })) 
    shortlink = Shortlink(long_url)
    try:   
        with contextlib.closing(urlopen(request_url)) as response:                      
            shortlink.link = response.read().decode('utf-8 ')
        response_status = "Code : " + str(response.code) + " => " + HTTPStatus(response.code).phrase
        return shortlink
    except HTTPError as e: 
        response_status = "Code : " + str(e.code) + " => " + HTTPStatus(e.code).phrase
        return shortlink

def bitly(long_url):
    global response_status
    access_token = ['14215a807e3dfcb7c7ab612706cf4302e7ab8fda']
    query_params = {
        'access_token': access_token,
        'longUrl': long_url
    }
    shortlink = Shortlink(long_url)
    endpoint = 'https://api-ssl.bitly.com/v3/shorten'
    response = requests.get(endpoint, params=query_params, verify=False)
    data = response.json()
    print(data)
    if data['status_code'] in range(199,300):
        shortlink.link = str(data['data']['url'])
    response_status = "Code : " + str(data['status_code']) + " => " + HTTPStatus(data['status_code']).phrase
    return shortlink

