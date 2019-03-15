import pytest


class TestBaseRoutes:
    """

    """

    def test_home_route_get_status(self, client):
        """
        Tests status code for '/' route using GET method.
        """
        res = client.get('/')
        assert res.status_code == 200

    def test_home_route_title(self, client):
        """

        """
        res = client.get('/')
        assert b'<title>Home</title>' in res.data

    def test_unknown_route_status(self, client):
        """

        """
        res = client.get('/doesnotexist')
        assert res.status_code == 404
        assert b'<h1>404 - Page Not Found</h1>' in res.data
