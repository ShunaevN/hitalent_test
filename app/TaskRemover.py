from custom_types.Category import Category
from typing import Never


class TaskRemover:
    """ A class that performs the functions of removing tasks.
    It is possible to remove task by id or by category """
    def __init__(self, storage):
        self.storage = storage

    def delete_by_id(self, task_id: str) -> dict | None:
        """
            Remove task by id.

            Args:
                task_id (str): id of task for remove.

            Returns:
                dict | None: return deleted task or None if task by id not found.
        """
        for task in self.storage:
            if task['id'] == task_id:
                self.storage.remove(task)
                return task

    def delete_by_category(self, category: Category) -> list[dict] | list[Never]:
        """
            Remove task by category.

            Args:
                category (Category): category of task for remove.

            Returns:
                list[dict] | list[Never]: return new storage with task or empty if all tasks were deleted.
        """
        tasks = list(filter(lambda task: task['category'] != category.value, self.storage))
        self.storage = tasks.copy()
        return self.storage
