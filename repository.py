from models import Task


class TaskRepository:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def find_all(self):
        return list(self._tasks.values())
