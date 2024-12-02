import pytest
from app.TaskReader import TaskReader
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
    return data


def test_read_all(init_storage):
    storage = init_storage
    manager = TaskReader(storage)

    assert (manager.read_all() == storage)


def test_read_by_category(init_storage):
    storage = init_storage
    manager = TaskReader(storage)

    assert (manager.read_by_category(Category.TRAINING) == [
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


def test_read_by_category_empty(init_storage):
    storage = init_storage
    manager = TaskReader(storage)
    assert (manager.read_by_category(Category.PERSONAL) == [])
