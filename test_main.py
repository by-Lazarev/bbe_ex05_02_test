import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def setup_database():
    # Создаём таблицы в тестовой базе данных
    Base.metadata.create_all(bind=engine)
    yield
    # Удаляем таблицы после тестов
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client():
    from fastapi.testclient import TestClient
    return TestClient(app)


def test_create_user(client):  # Добавляем client как аргумент
    response = client.post("/users/", json={"name": "Test User 1"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User 1"


def test_read_users(client):  # Добавляем client как аргумент
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_user(client):  # Добавляем client как аргумент
    # Сначала создаём пользователя
    response = client.post("/users/", json={"name": "Test User"})
    user_id = response.json()["id"]

    # Читаем созданного пользователя
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"


def test_update_user(client):  # Добавляем client как аргумент
    # Сначала создаём пользователя
    response = client.post("/users/", json={"name": "Old Name"})
    user_id = response.json()["id"]

    # Обновляем имя пользователя
    response = client.put(f"/users/{user_id}", json={"name": "New Name"})
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"


def test_delete_user(client):  # Добавляем client как аргумент
    # Сначала создаём пользователя
    response = client.post("/users/", json={"name": "To Be Deleted"})
    user_id = response.json()["id"]

    # Удаляем пользователя
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
