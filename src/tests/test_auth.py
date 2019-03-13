import pytest


def test_get_register_status(client):
    res = client.get('/register')
    assert res.status_code == 201


def test_get_register_has_correct_text(client):
    res = client.get('/register')
