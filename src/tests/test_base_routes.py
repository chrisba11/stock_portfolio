import pytest


class TestBaseRoutes:
    """

    """

    def test_home_route_get_status():
        """
        Tests status code for '/' route using GET method.
        """
        rv = app.test_client().get('/')
        assert rv.status_code == 200
