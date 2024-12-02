import time
from custom_types.Category import Category
from pprint import pprint
from app.TaskRemover import TaskRemover
from utils.check_empty_string import check_empty_string


def remover_menu(task_remover: TaskRemover) -> list[dict] | None:
    """
        Describes the logic of removing tasks in the main menu.

        Args:
            task_remover (TaskRemover): instance of TaskRemover class.

        Returns:
            list[dict] | None: return None if tasks not found or list of deleted tasks .
    """
    while True:
        print("Вы зашли в меню удаления задач. Выберите режим удаления: ")
        print("1.Удаление по идентификатору.")
        print("2. Удаление по категории. ")
        print("3. Выход в главное меню")
        task_remover_answer = input("Введите пункт меню: ")
        if task_remover_answer == '1':
            while True:
                task_id = input("Введите идентификатор задачи: ")
                if check_empty_string(task_id):
                    break
            deleted_task = task_remover.delete_by_id(task_id)
            if deleted_task:
                print("Показываем удаленную задачу и возвращаемся в меню через 5 сек. :")
                print("--------------------------------\n\n")
                pprint(deleted_task)
                print("\n\n--------------------------------")
                time.sleep(5)
                break
            else:
                print(f"Задача с id {task_id} не найдена.")
        elif task_remover_answer == '2':
            while True:
                print("Выберите нужную категорию")
                print("1. Работа")
                print("2. Личное")
                print("3. Обучение")
                print("4. Назад")
                task_remover_category_answer = input("Введите номер категории: ")
                if task_remover_category_answer in ['1', '2', '3']:
                    category = None
                    if task_remover_category_answer == '1':
                        category = Category.JOB
                    elif task_remover_category_answer == '2':
                        category = Category.PERSONAL
                    elif task_remover_category_answer == '3':
                        category = Category.TRAINING
                    saved_task = task_remover.delete_by_category(category)
                    print("Задача успешно удалена.")
                    print("Показываем оставшиеся задачи и возвращаемся в меню через 5 сек. :")
                    print("--------------------------------\n\n")
                    pprint(saved_task)
                    print("\n\n--------------------------------")
                    time.sleep(5)
                    return saved_task
                elif task_remover_category_answer == '4':
                    break
                else:
                    print("Вы ввели неверное значение. Повторите снова.")
        elif task_remover_answer == '3':
            break
        else:
            print("Вы ввели неверное значение. Повторите снова.")
