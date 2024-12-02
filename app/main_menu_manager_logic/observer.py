import time
from custom_types.Category import Category
from custom_types.Status import Status
from pprint import pprint
from app.TaskObserver import TaskObserver
from utils.check_empty_string import check_empty_string


def observer_menu(task_observer: TaskObserver, json_data) -> None:
    """
        Describes the logic of observing task in the main menu.

        Args:
            task_observer (TaskObserver): instance of TaskObserver class.
            json_data (list[dict]): storage - list with tasks.

        Returns:
            None object.
    """
    while True:
        print("Вы зашли в меню поиска задач. Выберите режим поиска: ")
        print("1. Поиск по ключевым словам.")
        print("2. Поиск по категории. ")
        print("3. Поиск по статусу выполнения.")
        print("4. Выход в главное меню")
        task_observer_answer = input("Введите пункт меню: ")
        if task_observer_answer == '1':
            while True:
                keywords = input("Введите ключевое слово: ")
                if check_empty_string(keywords):
                    break
            tasks = task_observer.find_by_keywords(json_data, keywords)
            if tasks:
                print("Показываем найденные задачи. Через 5 сек. вернемся в основное меню")
                print("--------------------------------\n\n")
                pprint(tasks)
                print("\n\n--------------------------------")
                time.sleep(5)
                break
            else:
                print(f"Задач по данным ключевым словам не найдено")
        elif task_observer_answer == '2':
            while True:
                print("Выберите нужную категорию")
                print("1. Работа")
                print("2. Личное")
                print("3. Обучение")
                print("4. Назад")
                task_observer_category_answer = input("Введите номер категории: ")
                if task_observer_category_answer in ['1', '2', '3']:
                    category = None
                    if task_observer_category_answer == '1':
                        category = Category.JOB
                    elif task_observer_category_answer == '2':
                        category = Category.PERSONAL
                    elif task_observer_category_answer == '3':
                        category = Category.TRAINING
                    tasks = task_observer.find_by_category(json_data, category)
                    if tasks:
                        print("Показываем найденные задачи. Через 5 сек. вернемся в основное меню")
                        print("--------------------------------\n\n")
                        pprint(tasks)
                        print("\n\n--------------------------------")
                        time.sleep(5)
                        break
                    else:
                        print(f"Задач в категории {category.value} не найдены")
                elif task_observer_category_answer == '4':
                    break
                else:
                    print("Вы ввели неверное значение. Повторите снова.")
        elif task_observer_answer == '3':
            while True:
                print("Выберите нужный статус выполнения")
                print("1. Не выполнена")
                print("2. Выполнена")
                print("3. Назад")
                task_observer_status_answer = input("Введите номер статуса: ")
                if task_observer_status_answer in ['1', '2']:
                    status = None
                    if task_observer_status_answer == '1':
                        status = Status.IN_PROGRESS
                    elif task_observer_status_answer == '2':
                        status = Status.DONE
                    tasks = task_observer.find_by_status(json_data, status)
                    if tasks:
                        print("Показываем найденные задачи. Через 5 сек. вернемся в основное меню")
                        print("--------------------------------\n\n")
                        pprint(tasks)
                        print("\n\n--------------------------------")
                        time.sleep(5)
                        break
                    else:
                        print(f"Задач со статусом {status.value} не найдены")
                elif task_observer_status_answer == '3':
                    break
                else:
                    print("Вы ввели неверное значение. Повторите снова.")
        elif task_observer_answer == '4':
            break
        else:
            print("Вы ввели неверное значение. Повторите снова.")
