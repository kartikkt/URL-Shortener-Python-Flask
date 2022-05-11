from urllib import response


class TestComputationalTheory:
    def test_p_equals_np(self):
        assert 'NP' == 'NP'

    def test_home_page(self, get):
        response = get('/')
        assert response.status_code == 200
