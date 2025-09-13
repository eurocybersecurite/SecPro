import pytest
from secpro.app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, SecPro!' in response.data

def test_api_login(client):
    response = client.post('/api/login')
    assert response.status_code == 200
    assert b'access_token' in response.data

def test_api_report(client):
    response = client.get('/api/report')
    assert response.status_code == 200
    assert b'Report generated' in response.data
