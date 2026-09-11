import json
import os

class TodoManager:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.tasks = []
        self.load()

    def load(self):
        # try load, else empty
        pass

    def save(self):
        # save to json
        pass

    def add(self, task_text):
        # append and save
        pass

    def remove(self, task_index):
        # remove by index and save
        pass

    def list(self):
        # print tasks
        pass

# Main Loop
def main():
    manager = TodoManager()
    while True:
        # display menu
        # parse input
        # handle actions
