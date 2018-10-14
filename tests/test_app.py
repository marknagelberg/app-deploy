from .conftest import new_name, test_client, create_database


def test_new_name(new_name):
    assert new_name.name == 'Mark'


def test_test_client(test_client):
    assert test_client is not None


def test_main_page(test_client, create_database):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data
    assert b'Mark' in response.data
