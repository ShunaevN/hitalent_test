import time
from custom_types.Priority import Priority
from custom_types.Category import Category
from custom_types.Status import Status
from pprint import pprint
from utils.prepare_task import prepare_task_to_dict
from utils.create_task import create_task
from app.TaskEditor import TaskEditor
from utils.check_date import check_date
from utils.check_empty_string import check_empty_string


def editor_menu(task_editor: TaskEditor, json_data: list[dict]) -> None:
    """
        Describes the logic of editing task in the main menu.

        Args:
            task_editor (TaskEditor): instance of TaskEditor class.
            json_data (list[dict]): storage - list with tasks.

        Returns:
            None object.
    """
    while True:
        print("Вы зашли в режим изменения задачи. Выберите тип изменения")
        print("1. Редактирование существующей задачи")
        print("2. Отметка задачи как выполненной")
        print("3. Вернуть назад")
        task_change_answer = input("Введите пункт меню: ")
        if task_change_answer == "1":
            while True:
                print("Выберите параметр задачи, который хотите изменить:")
                print("1. Все параметры")
                print("2. Название")
                print("3. Описание")
                print("4. Категорию")
                print("5. Срок выполнения")
                print("6. Приоритет")
                print("7. Статус")
                task_change_parameter_answer = input("Введите номер пункта меню: ")
                task_id = input("Введите id задачи: ")
                new_task = None
                if task_change_parameter_answer == "1":
                    task = create_task()
                    task_to_dict = prepare_task_to_dict(task)
                    new_task = task_editor.edit_all(json_data, task_id, task_to_dict)
                elif task_change_parameter_answer == "2":
                    while True:
                        title = input("Введите новое название задачи: ")
                        if check_empty_string(title):
                            break
                    new_task = task_editor.edit_title(json_data, task_id, title)
                elif task_change_parameter_answer == "3":
                    while True:
                        description = input("Введите новое описание задачи: ")
                        if check_empty_string(description):
                            break
                    new_task = task_editor.edit_description(json_data, task_id, description)
                elif task_change_parameter_answer == "4":
                    while True:
                        print("Введите новую категорию задачи")
                        print("1. Работа")
                        print("2. Личное")
                        print("3. Обучение")
                        category_answer = input("Введите номер категории: ")
                        if category_answer in {'1', '2', '3'}:
                            if category_answer == "1":
                                category = Category.JOB
                            elif category_answer == "2":
                                category = Category.PERSONAL
                            else:
                                category = Category.TRAINING
                            break
                        else:
                            print("Неверный номер категории")
                    new_task = task_editor.edit_category(json_data, task_id, category)
                elif task_change_parameter_answer == "5":
                    while True:
                        due_date = input("Введите срок выполнения задачи в формате год-месяц-день, пример 2024-11-30: ")
                        if check_date(due_date):
                            break
                    new_task = task_editor.edit_due_date(json_data, task_id, due_date)
                elif task_change_parameter_answer == "6":
                    while True:
                        print("Введите новый приоритет задачи")
                        print("1. Низкий")
                        print("2. Средний")
                        print("3. Высокий")
                        priority_answer = input("Введите номер приоритета: ")
                        if priority_answer in {'1', '2', '3'}:
                            if priority_answer == "1":
                                priority = Priority.LOW
                            elif priority_answer == "2":
                                priority = Priority.MIDDLE
                            else:
                                priority = Priority.HIGH
                            break
                        else:
                            print("Неверный номер приоритета")
                    new_task = task_editor.edit_priority(json_data, task_id, priority)
                elif task_change_parameter_answer == "7":
                    while True:
                        print("Введите новый статус задачи")
                        print("1. Не выполнена")
                        print("2. Выполнена")
                        status_answer = input("Введите номер статуса: ")
                        if status_answer in {'1', '2'}:
                            if status_answer == "1":
                                status = Status.IN_PROGRESS
                            else:
                                status = Status.DONE
                            break
                        else:
                            print("Неверный номер статуса")
                    new_task = task_editor.edit_status(json_data, task_id, status)
                if task_change_parameter_answer in {"1", "2", "3", "4", "5", "6", "7"}:
                    if new_task:
                        print(f"Задача с id {task_id} успешно изменена")
                        print("Показываем задачу. Через 5 сек. вернемся в основное меню")
                        print("--------------------------------\n\n")
                        pprint(new_task)
                        print("\n\n--------------------------------")
                        time.sleep(5)
                        break
                    else:
                        print(f"Задача с id {task_id} не найдена")
                else:
                    print("Вы ввели неверное значение. Повторите снова.")

        elif task_change_answer == "2":
            task_id = input("Введите id задачи: ")
            task = task_editor.set_as_done(json_data, task_id)
            if task:
                print(f"Задача с id {task_id} успешно изменена")
            else:
                print(f"Задача с id {task_id} не найдена")
        elif task_change_answer == "3":
            break
        else:
            print("Вы ввели неверное значение. Повторите снова.")