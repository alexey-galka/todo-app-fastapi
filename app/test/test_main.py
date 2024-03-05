from fastapi.testclient import TestClient
from ..main import app
from fastapi import status

client = TestClient(app=app)


def test_return_health_check():
    response = client.get('/heath_check')
    assert response.status_code == status.HTTP_200_OK, 'Status should be 200'
    assert response.json() == {'status': 'healthy'}
