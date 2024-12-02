def prepare_task_to_dict(task: list) -> dict:
    """
       Creating task dict object from list of task parameters

       Args:
           task (list): list of task parameters.

       Returns:
           dict: task dict object.
   """
    task_dict = {
        'title': task[0],
        'description': task[1],
        'category': task[2],
        'due_date': task[3],
        'priority': task[4],
        'status': task[5]
    }
    return task_dict
