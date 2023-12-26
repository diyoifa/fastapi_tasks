from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_login():
    response = client.post('/login', json={
        "email": "test@gmail.com",
        "password": "123"}
    )
    assert response.status_code == 200

def test_user_login_invalid_credentials():
    response = client.post('/login', json={
        "email": "wrong@test@gmail.com",
        "password": "123"}
    )
    assert response.status_code == 401