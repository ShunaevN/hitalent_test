import pytest
import json
from app.TaskStorage import TaskStorage
from app.TaskMaker import TaskMaker
from custom_types.Category import Category
from custom_types.Status import Status
from custom_types.Priority import Priority


@pytest.fixture()
def init_task():
    task = ["Не Изучить основы FastAPI", "Не Пройти документацию", Category.TRAINING,
            "2024-11-28", Priority.LOW, Status.IN_PROGRESS]

    task_maker = TaskMaker(*task)
    return task_maker


def test_load_json_empty_json():
    path = './data/test_task.json'
    open(path, "w").close()  # очищаем json
    manager = TaskStorage(path)
    assert (manager.load_json() == [])


def test_load_json_add_task(init_task):
    manager = TaskStorage('./data/test_task.json')
    storage = manager.load_json()
    task_maker = init_task
    task_maker.add_task(storage)
    assert (list(storage[0].values())[1:] == ["Не Изучить основы FastAPI", "Не Пройти документацию",
                                              Category.TRAINING.value,
                                              "2024-11-28", Priority.LOW.value, Status.IN_PROGRESS.value])


def test_dump_json(init_task):
    path = "./data/test_task.json"
    open(path, "w").close()
    manager = TaskStorage(path)
    storage = manager.load_json()
    task_maker = init_task
    task_maker.add_task(storage)
    manager.dump_json(storage)
    with open(path, encoding='utf-8') as json_file:
        try:
            dictionary_storage = json.load(json_file)
        except ValueError:
            dictionary_storage = []

    assert (dictionary_storage != [])  # проверяем, что задача добавлена в json
