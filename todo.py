tasks = [] # List of dicts or objects
next_id = 1

def add(text):
    global next_id
    tasks.append({'id': next_id, 'text': text, 'completed': False})
    next_id += 1

def remove(id):
    # logic to remove

def list_tasks():
    # logic to print
