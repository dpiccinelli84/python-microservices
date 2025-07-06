import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_user(client):
    """Test case for fetching a user."""
    # Test for an existing user
    rv = client.get('/users/1')
    assert rv.status_code == 200
    assert rv.json == {'name': 'Alice'}

    # Test for a non-existing user
    rv = client.get('/users/99')
    assert rv.status_code == 404
