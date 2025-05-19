import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.crud.task import task
from app.schemas.task import TaskCreate


def test_create_task(client: TestClient, db_session: Session) -> None:
    data = {"title": "Test Task", "description": "Test Description", "is_completed": False}
    response = client.post("/api/v1/tasks/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert content["is_completed"] == data["is_completed"]
    assert "id" in content
    assert "created_at" in content


def test_read_task(client: TestClient, db_session: Session) -> None:
    # Create a task first
    task_in = TaskCreate(title="Test Task", description="Test Description", is_completed=False)
    task_obj = task.create(db_session, obj_in=task_in)

    response = client.get(f"/api/v1/tasks/{task_obj.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == task_obj.title
    assert content["description"] == task_obj.description
    assert content["is_completed"] == task_obj.is_completed
    assert content["id"] == task_obj.id


def test_read_tasks(client: TestClient, db_session: Session) -> None:
    # Create multiple tasks
    task_in1 = TaskCreate(title="Test Task 1", description="Test Description 1", is_completed=False)
    task_in2 = TaskCreate(title="Test Task 2", description="Test Description 2", is_completed=True)
    task.create(db_session, obj_in=task_in1)
    task.create(db_session, obj_in=task_in2)

    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2
    assert content[0]["title"] == "Test Task 1"
    assert content[1]["title"] == "Test Task 2"


def test_update_task(client: TestClient, db_session: Session) -> None:
    # Create a task first
    task_in = TaskCreate(title="Test Task", description="Test Description", is_completed=False)
    task_obj = task.create(db_session, obj_in=task_in)

    update_data = {"title": "Updated Task", "is_completed": True}
    response = client.put(f"/api/v1/tasks/{task_obj.id}", json=update_data)
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == update_data["title"]
    assert content["is_completed"] == update_data["is_completed"]
    assert content["id"] == task_obj.id


def test_delete_task(client: TestClient, db_session: Session) -> None:
    # Create a task first
    task_in = TaskCreate(title="Test Task", description="Test Description", is_completed=False)
    task_obj = task.create(db_session, obj_in=task_in)

    response = client.delete(f"/api/v1/tasks/{task_obj.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == task_obj.id

    # Verify task is deleted
    response = client.get(f"/api/v1/tasks/{task_obj.id}")
    assert response.status_code == 404


def test_read_nonexistent_task(client: TestClient) -> None:
    response = client.get("/api/v1/tasks/999")
    assert response.status_code == 404


def test_update_nonexistent_task(client: TestClient) -> None:
    update_data = {"title": "Updated Task", "is_completed": True}
    response = client.put("/api/v1/tasks/999", json=update_data)
    assert response.status_code == 404


def test_delete_nonexistent_task(client: TestClient) -> None:
    response = client.delete("/api/v1/tasks/999")
    assert response.status_code == 404 