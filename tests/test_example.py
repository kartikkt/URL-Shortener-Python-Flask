from urllib import response

import pytest
from shorty.api import tiny_url, bitly, get_shortened_url


class TestComputationalTheory:
    
    def test_home_page(self, get):
        '''
        GIVEN a Flask application for testing
        WHEN the page is requested via GET ('/')
        THEN check if response is valid
        '''        
        response = get('/')
        assert response.status_code == 200


    @pytest.mark.parametrize('url, shorten',
                            [ ('https://google.com','https://tinyurl.com/mbq3m'),
                            ( 'https://withplum.com', 'https://tinyurl.com/y54me8k8'),
                            ('https://facebook.com', 'https://tinyurl.com/ycgnndb')]
                            )
    def test_tiny_url_method_success(self, url, shorten):
        '''
        GIVEN a url to compress
        WHEN it uses tiny_url api for compression
        THEN check that shortened url is the correct one
        '''
        assert shorten == tiny_url(url).link



    @pytest.mark.parametrize('url, shorten',
                            [ ('https://google.com','https://bit.ly/37wIUqr'),
                            ( 'https://withplum.com', 'https://bit.ly/3wlyjH9'),
                            ('https://facebook.com', 'https://bit.ly/37vtbaY')]
                            )
    def test_bitly_method_success(self, url, shorten):
        '''
        GIVEN a url to compress
        WHEN it uses bit.ly api for compression
        THEN check that shortened url is the correct one
        '''

        assert shorten == bitly(url).link


    @pytest.mark.parametrize('url, shorten',
                            [ ('https://.com','https://tinyurl.com/myq426p'),
                            ( 'hello', 'URL Shortening Failed')]
                            )   
    def test_tiny_url_method_fail(self, url, shorten):
        '''
        GIVEN a random input for url to compress
        WHEN it uses tiny_url api for compression
        THEN check that shortened url fails
        '''
        assert shorten == tiny_url(url).link
    
    @pytest.mark.parametrize('url, shorten',
                            [ ('https://.com','URL Shortening Failed'),
                            ( 'hello', 'URL Shortening Failed')]
                            )
    def test_bitly_method_fail(self, url, shorten):
        '''
        GIVEN a random input for url to compress
        WHEN it uses bit.ly api for compression
        THEN check that shortened url fails
        '''
        assert shorten == bitly(url).link

    def test_post_route_success(self,client):
        '''
        GIVEN a response from the landing page
        WHEN it calls the  POST request with '/shortlinks'
        THEN check if the route is working properly
        '''
        url = '/shortlinks'

        mock_request_data = { 'original_url': 'https://google.com', 
                            'url_method': 'bit.ly'
                            }

        response = client.post(url, data=mock_request_data )

        assert  response.status_code == 200


    @pytest.mark.parametrize('url, method, link',
                        [   ('https://google.com', 'bit.ly','https://bit.ly/37wIUqr'),
                            ( 'https://withplum.com', '' , 'https://bit.ly/3wlyjH9'),
                            ('https://facebook.com', 'tiny_url' ,'https://tinyurl.com/ycgnndb') ] )
    def test_get_short_url_success( self, url, method, link ):
        '''
        GIVEN a url and compression method as a request
        WHEN it passes through the function
        THEN check that shortened url is the correct one depending on the url_method
        '''
        mock_request_data = { 'original_url': url,'url_method': method }
        if method=='':
            mock_request_data = { 'original_url': url }       
    
        assert  link == get_shortened_url(mock_request_data).link


