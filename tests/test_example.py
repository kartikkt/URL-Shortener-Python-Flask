from urllib import response
from shorty.api import tiny_url, bitly, get_shortened_url


class TestComputationalTheory:
    
    def test_home_page(self, get):
        response = get('/')
        assert response.status_code == 200

    def test_tiny_url_method_success(self):
        url =  'https://google.com'
        shorten = 'https://tinyurl.com/mbq3m'

        assert shorten == tiny_url(url).link

    def test_bitly_method_success(self):
        url =  'https://google.com'
        shorten = 'https://bit.ly/37wIUqr'

        assert shorten == bitly(url).link
        
    def test_tiny_url_method_fail(self):
        url =  'https://.com'
        shorten = 'https://tinyurl.com/myq426p'

        assert shorten == tiny_url(url).link

    def test_bitly_method_fail(self):
        url =  'https://.com'
        shorten =  'URL Shortening Failed'

        assert shorten == bitly(url).link

    def test_post_route_success(self,client):
        url = '/shortlinks'

        mock_request_data = { 'original_url': 'https://google.com', 
                            'url_method': 'bit.ly'
                            }

        response = client.post(url, data=mock_request_data )

        assert  response.status_code == 200

    def test_get_short_url_success( self):

        mock_request_data = { 'original_url': 'https://google.com', 
                            'url_method': 'bit.ly'
                            }

        assert  'https://bit.ly/37wIUqr' == get_shortened_url(mock_request_data).link


