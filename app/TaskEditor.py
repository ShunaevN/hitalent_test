from custom_types.Status import Status
from custom_types.Category import Category
from custom_types.Priority import Priority


class TaskEditor:
    """ A class that performs the functions of editing tasks.
    It is possible to edit all parameters or one of them """
    @staticmethod
    def edit_all(storage: list[dict], task_id: str, data: dict) -> dict | None:
        """
            Edit all parameters of Task.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                data (dict): dict with task.

            Returns:
                dict | None: return the modified task.
            """
        for task in storage:
            if task['id'] == task_id:
                task['title'] = data['title']
                task['description'] = data['description']
                task['category'] = data['category'].value
                task['due_date'] = data['due_date']
                task['priority'] = data['priority'].value
                task['status'] = data['status'].value
                return task

    @staticmethod
    def edit_title(storage: list[dict], task_id: str, title: str) -> dict | None:
        """
            Edit Task by title.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                title (str): new title of task.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['title'] = title
                return task

    @staticmethod
    def edit_description(storage: list[dict], task_id: str, description: str) -> dict | None:
        """
            Edit Task by description.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                description (str): new description of task.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['description'] = description
                return task

    @staticmethod
    def edit_category(storage: list[dict], task_id: str, category: Category) -> dict | None:
        """
            Edit Task by category.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                category (str): new category of task.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['category'] = category.value
                return task

    @staticmethod
    def edit_due_date(storage: list[dict], task_id: str, due_date: str) -> dict | None:
        """
            Edit Task by due date.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                due_date (str): new due_date of task.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['due_date'] = due_date
                return task

    @staticmethod
    def edit_priority(storage: list[dict], task_id: str, priority: Priority) -> dict | None:
        """
            Edit Task by priority.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                priority (Priority): new priority of task.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['priority'] = priority.value
                return task

    @staticmethod
    def edit_status(storage: list[dict], task_id: str, status: Status) -> dict | None:
        """
            Edit Task by status.

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.
                status (Status): new status of task.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['status'] = status.value
                return task

    @staticmethod
    def set_as_done(storage: list[dict], task_id: str) -> dict | None:
        """
            Set the status of task on DONE value .

            Args:
                storage (list[dict]): storage of tasks.
                task_id (str): id of task for editing.

            Returns:
                dict | None: return the modified task.
        """
        for task in storage:
            if task['id'] == task_id:
                task['status'] = Status.DONE.value
                return task
