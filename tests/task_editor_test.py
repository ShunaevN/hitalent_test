import pytest
from app.TaskEditor import TaskEditor
from custom_types.Status import Status
from custom_types.Priority import Priority
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
        }
    ]
    task_id = data[0]['id']
    return data, task_id


def test_edit_all(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    task = {
        "title": "Не Изучить основы FastAPI",
        "description": "Не Пройти документацию",
        "category": Category.TRAINING,
        "due_date": "2024-11-28",
        "priority": Priority.LOW,
        "status": Status.IN_PROGRESS
    }

    assert (task_editor.edit_all(storage, task_id, task) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Не Изучить основы FastAPI",
        "description": "Не Пройти документацию",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Низкий",
        "status": "Не выполнена"
    })


def test_edit_title(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    title = "Только Flask!"

    assert (task_editor.edit_title(storage, task_id, title) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Только Flask!",
        "description": "Прочитать и выполнить задание",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Высокий",
        "status": "Не выполнена"
    })


def test_edit_description(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    description = "Писать тесты на Pytest"

    assert (task_editor.edit_description(storage, task_id, description) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Писать тесты на Pytest",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Высокий",
        "status": "Не выполнена"
    })


def test_edit_category(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    category = Category.JOB

    assert (task_editor.edit_category(storage, task_id, category) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Прочитать и выполнить задание",
        "category": "Работа",
        "due_date": "2024-11-28",
        "priority": "Высокий",
        "status": "Не выполнена"
    })


def test_edit_priority(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    priority = Priority.MIDDLE

    assert (task_editor.edit_priority(storage, task_id, priority) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Прочитать и выполнить задание",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Средний",
        "status": "Не выполнена"
    })


def test_edit_due_date(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    due_date = "2024-12-28"

    assert (task_editor.edit_due_date(storage, task_id, due_date) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Прочитать и выполнить задание",
        "category": "Обучение",
        "due_date": "2024-12-28",
        "priority": "Высокий",
        "status": "Не выполнена"
    })


def test_edit_status(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()
    status = Status.DONE

    assert (task_editor.edit_status(storage, task_id, status) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Прочитать и выполнить задание",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Высокий",
        "status": "Выполнена"
    })


def test_set_as_done(init_storage):
    storage, task_id = init_storage
    task_editor = TaskEditor()

    assert (task_editor.set_as_done(storage, task_id) == {
        "id": "e58ad128-fe36-40ed-8bf5-7095ae077f5d",
        "title": "Выполнить тестовое задание Python",
        "description": "Прочитать и выполнить задание",
        "category": "Обучение",
        "due_date": "2024-11-28",
        "priority": "Высокий",
        "status": "Выполнена"
    })
