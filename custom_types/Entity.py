from typing import Union
from app.TaskStorage import TaskStorage
from app.TaskObserver import TaskObserver
from app.TaskEditor import TaskEditor

Entity = tuple[TaskStorage, TaskObserver, TaskEditor]