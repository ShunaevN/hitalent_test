import pytest
from app.TaskRemover import TaskRemover
from custom_types.Category import Category


@pytest.fixture()
def init_storage():
    data = [
        {
            "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
            "title": "Выполнить тестовое задание Python",
            "description": "Прочитать и выполнить задание",
            "category": "Обучение",
            "due_date": "2024-11-28",
            "priority": "Высокий",
            "status": "Не выполнена"
        },
        {
            "id": "g98ad128-fe36-40ed-8bf5-7095ae077f6c",
            "title": "Pytest сила",
            "description": "Написать тесты на Pytest",
            "category": "Работа",
            "due_date": "2024-12-28",
            "priority": "Средний",
            "status": "Выполнена"
        }
    ]
    task_id = data[0]['id']
    return data, task_id


def test_delete_by_id_view_deleted_task(init_storage):
    storage, task_id = init_storage
    manager = TaskRemover(storage)

    assert (manager.delete_by_id(task_id) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Прочитать и выполнить задание",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Высокий",
        "status": "Не выполнена"
    })


def test_delete_by_id_view_storage(init_storage):
    storage, task_id = init_storage
    manager = TaskRemover(storage)
    manager.delete_by_id(task_id)
    assert (storage == [
        {
            "id": "g98ad128-fe36-40ed-8bf5-7095ae077f6c",
            "title": "Pytest сила",
            "description": "Написать тесты на Pytest",
            "category": "Работа",
            "due_date": "2024-12-28",
            "priority": "Средний",
            "status": "Выполнена"
        }
    ])


def test_delete_by_category(init_storage):
    storage, _ = init_storage
    manager = TaskRemover(storage)

    assert (manager.delete_by_category(Category.TRAINING) == [
        {
            "id": "g98ad128-fe36-40ed-8bf5-7095ae077f6c",
            "title": "Pytest сила",
            "description": "Написать тесты на Pytest",
            "category": "Работа",
            "due_date": "2024-12-28",
            "priority": "Средний",
            "status": "Выполнена"
        }
    ])
