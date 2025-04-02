import os
from model_task import Task
import json
import datetime


class Storage:
    def __init__(self, pwd='./storage/'):
        self.pwd = pwd
        os.makedirs(self.pwd, exist_ok=True)
        self.tasks = {}
        
    def load(self) -> dict[int, Task]:
        _tasksf = os.listdir(self.pwd)
        _tasks = {}
        for i in _tasksf:
            _task = json.load(open(os.path.join(self.pwd, i)))
            task = Task(
                _id = _task['_id'],
                description=_task['description'],
                status = _task['status'],
                createdAt=datetime.datetime.fromisoformat(_task['createdAt']),
                updatedAt=datetime.datetime.fromisoformat(_task['updatedAt'])
            )
            _tasks[task._id] = task
        self.tasks = _tasks
        return _tasks
    
    def save(self):
        for task in self.tasks.values():
            json.dump(task.__dict__, open(os.path.join(self.pwd, f"{task._id}.json"), 'w'))
        
    