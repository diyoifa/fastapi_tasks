from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_user_root():
    response = client.get('/user')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

def test_register_user():
    response = client.post('/user/register', json={
        "username": "test",
        "email": "test@gmail.com",
        "password": "123"})
    assert response.status_code == 201

def test_register_user_already_registered():
    response = client.post('/user/register', json={
        "username": "test",
        "email": "test@gmail.com",
        "password": "123"}
    )
    assert response.status_code == 400

    