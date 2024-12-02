import json
from typing import Never


class TaskStorage:
    """ A class that performs the functions of load json to storage or
    dump storage to json object """
    def __init__(self, src: str):
        self.src = src
        self.dictionary_storage = None

    def load_json(self) -> list[dict] | list[Never]:
        """
            Load data with tasks from json to list.

            Args:
                no args.

            Returns:
                list[dict] | list[Never]: return list with tasks or empty list if json was empty.
        """
        try:
            with open(self.src, encoding='utf-8') as json_file:
                self.dictionary_storage = json.load(json_file)
        except FileNotFoundError:
            self.dictionary_storage = []
            print("Файл не найден или имеет некорректный формат")
            print(f"Проверьте правильность файла по пути {self.src}")
        except ValueError:
            self.dictionary_storage = []
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
        finally:
            return self.dictionary_storage

    def dump_json(self, data: list[dict]) -> None:
        """
            Dump data from list to json object.

            Args:
                data (list[dict]): storage of tasks.

            Returns:
                None: return None object.
        """
        try:
            with open(self.src, mode='w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)
        except FileNotFoundError:
            print("Файл не найден или имеет некорректный формат")
            print(f"Проверьте правильность файла по пути {self.src}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

    def __repr__(self):
        return self.dictionary_storage
