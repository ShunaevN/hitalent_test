from app.TaskReader import TaskReader
from app.TaskMaker import TaskMaker
from app.TaskEditor import TaskEditor
from app.TaskObserver import TaskObserver
from app.TaskRemover import TaskRemover


class TaskManager(TaskRemover, TaskObserver, TaskEditor, TaskMaker, TaskReader):
    """A super class that can perform all functions with tasks.
    Child classes act as mixins"""