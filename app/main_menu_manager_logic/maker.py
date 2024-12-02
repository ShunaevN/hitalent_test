from utils.create_task import create_task
from app.TaskMaker import TaskMaker


def maker_menu(json_data: list[dict]) -> None:
    """
        Describes the logic of making task in the main menu.

        Args:
            json_data (list[dict]): storage - list with tasks.

        Returns:
            None object.
    """
    while True:
        print("Вы зашли в меню добавления задач. Введите параметры задачи:")
        task = create_task()
        print("Параметры задачи получены. Задача добавлена.")
        maker = TaskMaker(*task)
        maker.add_task(json_data)
        break
