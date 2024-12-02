from datetime import datetime


def check_date(date: str) -> bool:
    """
        Checking the date for compliance with the format %Y-%m-%d

        Args:
            date (str): string with date.

        Returns:
            bool: compliance string with date format or not.
    """
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        print("Неверный формат даты.")
        print("Введите дату в формате год-месяц-день, например 2024-11-30")
        return False
