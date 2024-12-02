def check_empty_string(task_param: str) -> bool:
    """
       Checking task field for emptiness

       Args:
           task_param (str): string with task field.

       Returns:
           bool: string is empty or not.
   """
    is_string = bool(task_param)
    if is_string:
        return is_string
    else:
        print("Пустая строка недопустима к вводу как параметр задачи")