from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


# Helper function to create a task
def create_sample_task():

    response = client.post(
        "/tasks",
        json={
            "title": "Learn Python",
            "description": "Python basics",
            "priority": "High",
            "status": "Pending"
        }
    )

    assert response.status_code == 201

    return response.json()


# TEST HOME
def test_home():

    response = client.get("/")

    assert response.status_code == 200


# TEST CREATE TASK
def test_create_task():

    response = client.post(
        "/tasks",
        json={
            "title": "Learn Python",
            "description": "Python basics",
            "priority": "High",
            "status": "Pending"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Learn Python"
    assert data["priority"] == "High"


# TEST GET ALL TASKS
def test_get_all_tasks():

    create_sample_task()

    response = client.get("/tasks")

    assert response.status_code == 200

    assert len(response.json()) > 0


# TEST GET TASK BY ID
def test_get_task_by_id():

    task = create_sample_task()

    task_id = task["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200

    assert response.json()["id"] == task_id


# TEST UPDATE TASK
def test_update_task():

    task = create_sample_task()

    task_id = task["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "status": "Completed"
        }
    )

    assert response.status_code == 200

    assert response.json()["status"] == "Completed"


# TEST DELETE TASK
def test_delete_task():

    task = create_sample_task()

    task_id = task["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    # Check whether deleted task is unavailable
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 404


# TEST INVALID TASK
def test_invalid_task():

    response = client.post(
        "/tasks",
        json={
            "title": "",
            "description": "Test",
            "priority": "Urgent",
            "status": "Pending"
        }
    )

    assert response.status_code == 422