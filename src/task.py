
from datetime import datetime
VALID_STATUSES = ['done', 'todo', 'in-progress']

class Task:
    name: str
    id: int
    status: str
    created_datetime: str
    last_updated_datetime: str
    
    def __init__(self, name: str,created_datetime: str=str(datetime.now()), last_updated_datetime: str=str(datetime.now()), status: str = 'todo', id: int = 0, ):
        if status not in VALID_STATUSES:
            raise f'Unexpected status "{status}"'
        self.status = status
        self.name = name
        self.id = id
        self.created_datetime = created_datetime
        self.last_updated_datetime = last_updated_datetime
        
    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f'{self.id} - {self.name} | {self.status}'
        
    
    @classmethod
    def from_dict(cls, dict_obj):
        return Task(**dict_obj)