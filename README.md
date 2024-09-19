# FastAPI User Management API

## Описание
Этот проект представляет собой простое API для управления пользователями, построенное на FastAPI и SQLAlchemy. API предоставляет функции для создания, чтения, обновления и удаления пользователей (CRUD).

## Требования
Для запуска проекта необходимо установить следующие зависимости:
- Python 3.12+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- pytest (для тестирования)

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone <repo_url>
   cd <project_directory>
   ``` 

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Для Windows: .venv\\\\Scripts\\\\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск приложения
Для запуска приложения локально используйте Uvicorn:
```bash
uvicorn main:app --reload
```
API будет доступно по адресу `http://127.0.0.1:8000`.

## Тестирование
Для запуска тестов с использованием `pytest` выполните:
```bash
pytest
```

## Использование API
### Создать пользователя
```http
POST /users/
```
Тело запроса (JSON):
```json
{
  "name": "Test User"
}
```

### Получить всех пользователей
```http
GET /users/
```

### Получить пользователя по ID
```http
GET /users/{id}
```

### Обновить пользователя
```http
PUT /users/{id}
```

### Удалить пользователя
```http
DELETE /users/{id}
```
