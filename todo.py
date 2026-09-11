import sys

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task_text):
        if not task_text.strip():
            return False
        self.tasks.append(task_text)
        return True

    def remove(self, index):
        try:
            index = int(index)
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                return True
            return False
        except ValueError:
            return False

    def list_tasks(self):
        # print format
        pass

def cli():
    manager = TodoList()
    while True:
        # show menu
        # get input
        # dispatch
        pass
