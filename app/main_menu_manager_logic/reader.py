import time
from custom_types.Category import Category
from pprint import pprint
from app.TaskReader import TaskReader


def reader_menu(task_reader: TaskReader) -> None:
    """
        Describes the logic of reading task in the main menu.

        Args:
            task_reader (TaskReader): instance of TaskReader class.

        Returns:
            None object.
    """
    while True:
        print("Вы зашли в меню просмотра списка задач. Какие задачи Вам показать?")
        print("1. Просмотр всех текущих задач.")
        print("2. Просмотр задач по категориям (работа, личное, обучение)")
        print("3. Выход в главное меню")
        task_reader_answer = input("Введите пункт меню: ")
        if task_reader_answer == '1':
            print("Показываем все задачи и возвращаемся в меню просмотра задач через 5 сек. :")
            print("--------------------------------\n\n")
            pprint(task_reader.read_all())
            print("\n\n--------------------------------")
            time.sleep(5)
        elif task_reader_answer == '2':
            while True:
                print("Выберите нужную категорию")
                print("1. Работа")
                print("2. Личное")
                print("3. Обучение")
                print("4. Назад")
                task_reader_category_answer = input("Введите номер категории: ")
                if task_reader_category_answer in ['1', '2', '3']:
                    print("Показываем задачи и возвращаемся в меню просмотра задач через 5 сек. :")
                    print("--------------------------------\n\n")
                    if task_reader_category_answer == '1':
                        pprint(task_reader.read_by_category(Category.JOB))
                    elif task_reader_category_answer == '2':
                        pprint(task_reader.read_by_category(Category.PERSONAL))
                    elif task_reader_category_answer == '3':
                        pprint(task_reader.read_by_category(Category.TRAINING))
                    print("\n\n--------------------------------")
                    time.sleep(5)
                elif task_reader_category_answer == '4':
                    break
                else:
                    print("Вы ввели неверное значение. Повторите снова.")
        elif task_reader_answer == '3':
            break
        else:
            print("Вы ввели неверное значение. Повторите снова.")