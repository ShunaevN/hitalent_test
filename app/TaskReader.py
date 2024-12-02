from custom_types.Category import Category
from typing import Never


class TaskReader:
    """ A class that performs the functions of reading tasks.
    It is possible to read all tasks or read tasks by category """
    def __init__(self, storage: list[dict]):
        self.storage = storage

    def read_all(self) -> list[dict] | list[Never]:
        """
            Reading all tasks in storage.

            Args:
                No args.

            Returns:
                list[dict] | list[Never]: return list of Tasks or empty list.
        """
        return self.storage

    def read_by_category(self, category: Category) -> list[dict] | list[Never]:
        """
            Reading tasks by category.

            Args:
                category (Category): category to search for tasks.

            Returns:
                list[dict] | list[Never]: return list of Tasks or empty list.
        """
        return [task for task in self.storage if task['category'] == category.value]
