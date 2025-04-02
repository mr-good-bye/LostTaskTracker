from datetime import datetime
from time import sleep


class Status:
    ToDo = "To Do"
    InProgress = "In Progress"
    Done = "Done"


class Task:
    def __init__(
        self,
        _id=None,
        description=None,
        status=Status.ToDo, 
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    ):
        self._id = _id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        
    def __str__(self):
        return f'''{"="*25}
    ID:  {str(self._id).rjust(5)} | Status: {self.status}
    DESCRIPTION: {self.description}
    Created    : {self.createdAt.strftime("%Y-%m-%d %H:%M:%S")}
    Updated    : {self.updatedAt.strftime("%Y-%m-%d %H:%M:%S")}\n{"="*25}'''
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key not in ('_id', 'description', 'status'):
                continue
            setattr(self, key, value)
        self.updatedAt = datetime.now()
        
        
        
if __name__ == "__main__":
    t = Task(
        1,
        'Test Description',
        Status.InProgress
    )
    print(t)
    sleep(2)
    t.update(description='Updated description')
    print(t)
