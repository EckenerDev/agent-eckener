import json
import os

class TodoManager:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.todos = []
        self._load()

    def _load(self):
        # try to load from file, handle errors
        pass

    def _save(self):
        # save to file, handle errors
        pass

    def add(self, task):
        # add to list
        pass

    def remove(self, index):
        # remove by index
        pass

    def show(self):
        # print list
        pass

def main():
    # CLI loop
    pass
