from task import Task
from datetime import datetime
import json

class TaskLibrary():
    last_id: int
    tasks: [Task]
    filename: str    
        
    def __str__(self):        
        output = f'Filename: {self.filename}:\nLast Id: {self.last_id}\nTasks: '
        for task in self.tasks:
            output += f'\n{str(task)}'
        return output
    
    def udpate_json(self):
        with open(self.filename, 'w') as task_json:
            json.dump(self.task_library_to_dict(), task_json, indent=4)
    
    def get_task_list_dict(self):
        return [task.to_dict() for task in self.tasks]
    
    def task_library_to_dict(self):        
        return {'last_id': self.last_id, 'tasks': self.get_task_list_dict()}
    
    def print_task_list(self, status: str = None):
        for task in self.tasks:
            if status and task.status != status:
                continue
            print(task)
            
    def set_task_name(self, id:int, new_name: str):
        found = False
        for task in self.tasks:
            if task.id != id:
                continue
            found=True
            task.name = new_name
            task.last_updated_datetime = str(datetime.now())
            print(task)
            break
        if found:
            self.udpate_json()
        return found
    
    def set_task_status(self, id: int, status: str):
        found = False
        for task in self.tasks:
            if task.id != id:
                continue
            found=True
            task.status = status
            task.last_updated_datetime = str(datetime.now())
            print(task)
            break
        if found:
            self.udpate_json()
        return found
    
    
    def delete_task(self, id: int):
        found = False
        for task in self.tasks:
            if task.id != id:
                continue
            found=True
            self.tasks.remove(task)
            break
        if found:
            self.udpate_json()
        return found
        
    
    def add_task(self, name: str, status: str = 'todo') -> int:
        self.last_id +=1
        self.tasks.append(Task(name=name,status=status, id=self.last_id))
        self.udpate_json()
        return self.last_id
    
    @classmethod
    def load_library(cls, task_json: dict, filename: str):
        cls = TaskLibrary()
        cls.filename = filename
        cls.last_id = task_json['last_id']
        
        cls.tasks = [Task.from_dict(task) for task in task_json['tasks']]
        return cls

    @classmethod
    def init_library(cls, filename: str):
        with open(filename, 'w') as task_json:
            json.dump({'last_id': 0, 'tasks': []}, task_json, indent=4)
    
