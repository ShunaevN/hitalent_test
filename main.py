from app.TaskStorage import TaskStorage
from app.TaskReader import TaskReader
from app.TaskObserver import TaskObserver
from app.TaskEditor import TaskEditor
from app.TaskRemover import TaskRemover
from custom_types.Entity import Entity
from app.main_menu_manager_logic.maker import maker_menu
from app.main_menu_manager_logic.reader import reader_menu
from app.main_menu_manager_logic.editor import editor_menu
from app.main_menu_manager_logic.remover import remover_menu
from app.main_menu_manager_logic.observer import observer_menu


def init_entities(path: str) -> Entity:
    storage = TaskStorage(path)
    task_editor = TaskEditor()
    task_observer = TaskObserver()
    return storage, task_observer, task_editor


def main() -> None:
    (storage,
     task_observer,
     task_editor) = init_entities('./data/tasks.json')

    json_data = storage.load_json()
    task_reader = TaskReader(json_data)
    task_remover = TaskRemover(json_data)

    while True:
        print(
            """
Добро пожаловать в приложение 'Менеджер задач'.
Для дальнейшей работы с программой введи следующие значения:
1. Вход в главное меню функционала программы
2. Выход 
"""
        )
        greet_menu_answer = input("Введите пункт меню: ")
        if greet_menu_answer == "2":
            print("Сохраняем данные в файл и завершаем работу.")
            storage.dump_json(json_data)
            return
        elif greet_menu_answer == "1":
            while True:
                print("""Вы попали в главное меню. Выберите операцию:
1. Просмотр списка задач.
2. Добавление задачи.
3. Изменение задачи.
4. Удаление задачи.
5. Поиск задачи.
6. Выход из приложения.
                """)
                main_menu_answer = input("Введите пункт меню: ")
                if main_menu_answer == '1':
                    reader_menu(task_reader)
                elif main_menu_answer == '2':
                    maker_menu(json_data)
                elif main_menu_answer == '3':
                    editor_menu(task_editor, json_data)
                elif main_menu_answer == '4':
                    data = remover_menu(task_remover)
                    if data is not None:
                        json_data = data
                elif main_menu_answer == '5':
                    observer_menu(task_observer, json_data)
                elif main_menu_answer == '6':
                    print("Сохраняем данные в файл и завершаем работу.")
                    storage.dump_json(json_data)
                    return
                else:
                    print("Вы ввели неверное значение. Повторите снова.")
        else:
            print("Вы ввели неверное значение. Повторите снова.")


if __name__ == '__main__':
    main()
