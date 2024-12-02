from custom_types.Priority import Priority
from custom_types.Category import Category
from custom_types.Status import Status
from utils.check_date import check_date
from utils.check_empty_string import check_empty_string


def create_task() -> list:
    """
           Creating task fields in a list

           Args:
               no args

           Returns:
               list: list with task fields.
       """

    while True:
        title = input("Введите название задачи: ")
        if check_empty_string(title):
            break
    while True:
        description = input("Введите описание задачи: ")
        if check_empty_string(description):
            break
    print("Выберите категорию задачи.")
    print("1. Работа")
    print("2. Личное")
    print("3. Обучение")
    while True:
        category_answer = input("Введите номер категории: ")
        if category_answer in ['1', '2', '3']:
            if category_answer == '1':
                category = Category.JOB
            elif category_answer == '2':
                category = Category.PERSONAL
            else:
                category = Category.TRAINING
            break
        else:
            print("Выбран неверный номер категории.")
    while True:
        due_date = input("Введите срок выполнения задачи в формате год-месяц-день, пример 2024-11-30: ")
        if check_date(due_date):
            break
    print("Выберите приоритет задачи.")
    print("1. Низкий")
    print("2. Средний")
    print("3. Высокий")
    while True:
        priority_answer = input("Введите приоритет: ")
        if priority_answer in ['1', '2', '3']:
            if priority_answer == '1':
                priority = Priority.LOW
            elif priority_answer == '2':
                priority = Priority.MIDDLE
            else:
                priority = Priority.HIGH
            break
        else:
            print("Выбран неверный номер приоритета.")
    print("Выберите статус задачи.")
    print("1. Не выполнена")
    print("2. Выполнена")
    while True:
        status_answer = input("Введите номер статуса: ")
        if status_answer in ['1', '2']:
            if status_answer == '1':
                status = Status.IN_PROGRESS
            else:
                status = Status.DONE
            break
        else:
            print("Выбран неверный номер статуса.")
    task = [title, description, category, due_date, priority, status]
    return task
