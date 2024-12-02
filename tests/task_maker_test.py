import pytest
from app.TaskMaker import TaskMaker
from custom_types.Status import Status
from custom_types.Priority import Priority
from custom_types.Category import Category


@pytest.fixture()
def init_task():
    task = ["Не Изучить основы FastAPI", "Не Пройти документацию", Category.TRAINING,
            "2024-11-28", Priority.LOW, Status.IN_PROGRESS]

    task_maker = TaskMaker(*task)
    return task_maker


def test_add_task(init_task):
    storage = []
    task_maker = init_task
    task_maker.add_task(storage)

    # В списке storage добавится объект задачи в виде словаря. Получаем объект по индексу 0.
    # Берем все значения словаря, кроме первого, так как сформированный id мы не знаем
    assert (list(storage[0].values())[1:] == ["Не Изучить основы FastAPI", "Не Пройти документацию",
                                              Category.TRAINING.value,
                                              "2024-11-28", Priority.LOW.value, Status.IN_PROGRESS.value])


def test_prepare_dict(init_task):

    task_maker = init_task
    task_to_dict = task_maker.new_task

    assert (list(task_to_dict.values())[1:] == ["Не Изучить основы FastAPI", "Не Пройти документацию",
                                                Category.TRAINING.value,
                                                "2024-11-28", Priority.LOW.value, Status.IN_PROGRESS.value])
