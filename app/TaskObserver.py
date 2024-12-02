from custom_types.Category import Category
from custom_types.Status import Status
from typing import Never


class TaskObserver:
    """ A class that performs the functions of viewing tasks.
    It is possible to view all tasks and tasks by category """

    @staticmethod
    def find_by_keywords(storage: list[dict], keywords: str) -> list[dict] | list[Never]:
        """
            Find task by keywords in title or description.

            Args:
                storage (list[dict]): storage of tasks.
                keywords (str): keywords for search tasks.

            Returns:
                list[dict] | list[Never]: return list of tasks.
        """
        tasks = [task for task in storage
                 if keywords.lower() in task['title'].lower()
                 or keywords.lower() in task['description'].lower()]
        return tasks

    @staticmethod
    def find_by_category(storage: list[dict], category: Category) -> list[dict] | list[Never]:
        """
            Find task by category.

            Args:
                storage (list[dict]): storage of tasks.
                category (Category): category for search tasks.

            Returns:
                list[dict] | list[Never]: return list of tasks.
        """
        tasks = [task for task in storage if task['category'] == category.value]
        return tasks

    @staticmethod
    def find_by_status(storage: list[dict], status: Status) -> list[dict] | list[Never]:
        """
            Find task by status.

            Args:
                storage (list[dict]): storage of tasks.
                status (Status): status for search tasks

            Returns:
                list[dict] | list[Never]: return list of tasks.
        """
        tasks = [task for task in storage if task['status'] == status.value]
        return tasks
