# Description
In this program you'll find a simple structure for tasks with parameters such as the **Name**, **Status**, **Created Date** and **Updated Date**. The data is stored in a **json** file which is initialized upon starting the script.
This is a simple cli app for research and learning purposes motivated by **[roadmap.sh](https://roadmap.sh/)** . The project is: [task-tracker](https://roadmap.sh/projects/task-tracker)

# Requirements
1. You will need to have installed Python 3 on your computer

# Running instructions
There are actions to list tasks, add tasks, remove tasks and update tasks. I'll go into each one and how to use them

## Adding tasks
For adding tasks we'll use the **add** action followed by the tasks name just as follows: 
``` terminal
python src/main.py add "Task name"
```


With a message stating that the creation was successful and the tasks **id**

## Removing tasks
 For deleting tasks we'll use the **delete** action followed by the tasks id just as follows: 
``` terminal
python src/main.py delete <task_id>
```

## Updating Tasks
### Updating Status
There are 3 statuses for a task. This are *'todo'*, *'in-progress'* and *'done'*

You can change to each of the states with the command mark-\[status].
Being \[status] any of the 3 specified statuses. Also the id of the task to be updated is to be entered

The following is an example of setting the status of a task: 
``` terminal
python src/main.py mark-<status> <task_id>
```

### Updating Task Name
You can change the name of any task by using the following command: 
```terminal
python src/main.py update <id> <new_name>
```
