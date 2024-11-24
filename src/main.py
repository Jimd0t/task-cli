import os
from task import VALID_STATUSES
from task_library import TaskLibrary
import sys
import json


JSON_DATABASE_FILENAME = "tasks.json"

VALID_ACTIONS = ['list', 'add', 'delete', 'update', 'mark-done', 'mark-todo', 'mark-in-progress']


def main(task_library: TaskLibrary) -> bool:
    if len(sys.argv) < 2:
        return
    command = sys.argv[1]
    if command not in VALID_ACTIONS:
        print(f'The action "{command}" is not a valid action.')
        return
    
    if command == "add":
        if len(sys.argv) < 3:
            print('Missing parameters to complete this action')
            return
        task_name = sys.argv[2]
        id = task_library.add_task(task_name)
        print(f'Task "{task_name}" was created succesfully! (Id={id})')
        
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] in VALID_STATUSES else None
        task_library.print_task_list(status)
        
    elif command == "update":
        if len(sys.argv) < 4:
            raise 'Missing parameters to complete this action'
        id = int(sys.argv[2])
        new_name = sys.argv[3]
        updated = task_library.set_task_name(id=id, new_name=new_name)
        if updated:
            print(f'Task {id} updated succesfully!')
        else:
            print('An error occured')
            
    elif "mark-" in command:
        if len(sys.argv) < 3:
            print("missing arguments")
            return False
        status = command[5::]
        id = int(sys.argv[2])
        if status not in VALID_STATUSES:
            print(f'Status "{status}" is not a valid status')
            return
        updated = task_library.set_task_status(id=id, status=status)
        if updated:
            print(f'Task {id} updated succesfully!')
        else:
            print('An error occured')


def load_tasks():
    FILENAME = JSON_DATABASE_FILENAME
    if not os.path.exists(FILENAME):
        TaskLibrary.init_library(FILENAME)
    with open(FILENAME) as json_file:
        data = json.load(json_file)
        
        task_library = TaskLibrary.load_library(data, FILENAME)
    return task_library


if __name__ == "__main__":
    print('Starting Task Manager')
    task_library = load_tasks()
    main(task_library)

