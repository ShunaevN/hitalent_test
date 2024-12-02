import pytest
from app.TaskObserver import TaskObserver
from custom_types.Category import Category
from custom_types.Status import Status


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
    return data


def test_find_by_keywords(init_storage):
    storage = init_storage
    manager = TaskObserver()

    assert (manager.find_by_keywords(storage, "PYTHON") == [
        {
            "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
            "title": "Выполнить тестовое задание Python",
            "description": "Прочитать и выполнить задание",
            "category": "Обучение",
            "due_date": "2024-11-28",
            "priority": "Высокий",
            "status": "Не выполнена"
        }
    ])


def test_find_by_category(init_storage):
    storage = init_storage
    manager = TaskObserver()

    assert (manager.find_by_category(storage, Category.JOB) == [
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


def test_find_by_category_empty(init_storage):
    storage = init_storage
    manager = TaskObserver()

    assert (manager.find_by_category(storage, Category.PERSONAL) == [])


def test_find_by_status(init_storage):
    storage = init_storage
    manager = TaskObserver()

    assert (manager.find_by_status(storage, Status.DONE) == [
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
