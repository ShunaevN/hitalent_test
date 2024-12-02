import uuid
from typing import Dict, Any
from custom_types.Priority import Priority
from custom_types.Category import Category
from custom_types.Status import Status


class TaskMaker:
    """ A class that performs the function of creating task.
    It is possible to add task to storage """
    def __init__(self, title: str, description: str, category: Category,
                 due_date: str, priority: Priority,
                 status: Status):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.category = category.value
        self.due_date = due_date
        self.priority = priority.value
        self.status = status.value
        self.new_task = self.prepare_dict()

    def prepare_dict(self) -> dict[str, str | Any]:
        """
            Convert list parameters of task to dict object.

            Args:
                no args.

            Returns:
                dict[str, str | Any]: return task by dict object.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

    def add_task(self, storage: list[dict]) -> None:
        """
            Add task to the storage.

            Args:
                storage (list[dict]): storage of tasks.

            Returns:
                 return None object.
        """
        storage.append(self.new_task)
