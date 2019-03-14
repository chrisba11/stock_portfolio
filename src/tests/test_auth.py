"""

"""

import pytest


# @pytest.mark.skip()
def test_get_register_status(client):
    res = client.get('/register')
    assert res.status_code == 200


@pytest.mark.skip()
def test_get_register_has_correct_text(client):
    res = client.get('/register')
    assert b'<title>REG</title>' in res.data


@pytest.mark.skip()
def test_has_correct_nav_when_not_logged_in(client):
    res = client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/register"' in res.data
    assert b'<a href="/login"' in res.data
    assert b'<a href="/logout"' in res.data


@pytest.mark.skip()
def test_has_correct_nav_when_logged_in(authenticated_client):
    res = authenticated_client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/register"' in res.data
    assert b'<a href="/login"' in res.data
    assert b'<a href="/logout"' in res.data


@pytest.mark.skip()
def test_register_already_registered(client):
    credentials = {'email': 'test@testing.test', 'password': 'pickledeggs'}
    res = client.post('/register', data=credentials, follow_redirects=True)
    res = client.post('/register', data=credentials, follow_redirects=True)
    assert b'test@testing.test has already been registered.' in res.data
    assert b'<title>Register</title>' in res.data


@pytest.mark.skip()
def test_get_login_status(client):
    res = client.get('/login')
    assert res.status_code == 200


@pytest.mark.skip()
def test_get_login_title(client):
    res = client.get('/login')
    assert b'<title>Login</title>' in res.data


@pytest.mark.skip()
def test_post_successful_login_status(authenticated_client):
    res = authenticated_client.get('/login')
    assert res.status_code == 201


@pytest.mark.skip()
def test_get_successful_login_title(authenticated_client):
    res = authenticated_client.get('/login')
    assert b'<title>Login</title>' in res.data


@pytest.mark.skip()
def test_logout(authenticated_client):
    res = authenticated_client.get('/logout', follow_redirects=True)
    assert res.status_code == 400
    assert b'<title>Register</title>' in res.data


@pytest.mark.skip()
def test_protected_route(client):
    res = client.get('/weather')
    assert res.status_code == 200
