from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_tasks():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ODliNjQxNWQzODdiZjRjYzcxZDk3MiIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20ifQ.Q45S6iIoqV1nKoiVXuOb2Fp42P8FCUs6eIrZ85JvxXA"  
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/task", headers=headers)
    assert response.status_code == 200

def test_get_all_tasks_unauthorized():
    response = client.get("/task")
    assert response.status_code == 401

def test_create_task():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ODliNjQxNWQzODdiZjRjYzcxZDk3MiIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20ifQ.Q45S6iIoqV1nKoiVXuOb2Fp42P8FCUs6eIrZ85JvxXA"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/task", headers=headers, json={
        "title": "test",
        "description": "test",
        "completed": False
    })
    assert response.status_code == 201

def test_create_task_unauthorized():
    response = client.post("/task", json={
        "title": "test",
        "description": "test",
        "completed": False
    })
    assert response.status_code == 401

def test_update_task():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ODliNjQxNWQzODdiZjRjYzcxZDk3MiIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20ifQ.Q45S6iIoqV1nKoiVXuOb2Fp42P8FCUs6eIrZ85JvxXA"  
    header = {"Authorization": f"Bearer {token}"}
    response = client.put('/task/6589fb9ebb3e90b0c6a1f615', headers=header, json={
        "title": "test_task_title",
        "description": "test_task_description",
        "completed": True
    })
    assert response.status_code == 200

def test_update_task_unauthorized():
    response = client.put('/task/6589fb9ebb3e90b0c6a1f615', json={
        "title": "test_task_title",
        "description": "test_task_description",
        "completed": True
    })
    assert response.status_code == 401

def test_delete_task():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ODliNjQxNWQzODdiZjRjYzcxZDk3MiIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20ifQ.Q45S6iIoqV1nKoiVXuOb2Fp42P8FCUs6eIrZ85JvxXA"  
    header = {"Authorization": f"Bearer {token}"}
    response = client.delete('/task/6589f4935bc2f8c44e85fee8', headers=header)
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}

def test_delete_task_unauthorized():
    response = client.delete('/task/6589fb9ebb3e90b0c6a1f615')
    assert response.status_code == 401
 