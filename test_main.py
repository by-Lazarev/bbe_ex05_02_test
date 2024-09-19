from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Test User"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_user():
    # Сначала создаём пользователя
    response = client.post("/users/", json={"name": "Test User"})
    user_id = response.json()["id"]

    # Читаем созданного пользователя
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_update_user():
    # Сначала создаём пользователя
    response = client.post("/users/", json={"name": "Old Name"})
    user_id = response.json()["id"]

    # Обновляем имя пользователя
    response = client.put(f"/users/{user_id}", json={"name": "New Name"})
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"

def test_delete_user():
    # Сначала создаём пользователя
    response = client.post("/users/", json={"name": "To Be Deleted"})
    user_id = response.json()["id"]

    # Удаляем пользователя
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
