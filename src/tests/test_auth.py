"""

"""

import pytest


# @pytest.mark.skip()
def test_get_register_status(client):
    res = client.get('/register')
    assert res.status_code == 201


# @pytest.mark.skip()
def test_get_register_has_correct_text(client):
    res = client.get('/register')
    assert b'<title>REG</title>' in res.data


# @pytest.mark.skip()
def test_has_correct_nav_when_not_logged_in(client):
    res = client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/register"' in res.data
    assert b'<a href="/login"' in res.data
    assert b'<a href="/logout"' in res.data


# def test_register_post
