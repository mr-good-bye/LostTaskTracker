import argparse
from storage import Storage
from model_task import Task, Status as TaskStatus

'''
add *description*
update *id* *description*
delete *id*
mark-in-progress *id*
mark-done *id*
list
list *status*
'''

parser = argparse.ArgumentParser("Lost Task Tracker")
command = parser.add_subparsers(dest='command', required=True)

add = command.add_parser('add', help='Сreate Task')
add.add_argument('description', nargs='+', help='Task Description')

update = command.add_parser('update', help='Update Task')
update.add_argument('id', type=int)
update.add_argument('description', nargs='+', help='Task Description')

delete = command.add_parser('delete', help='Delete Task')
delete.add_argument('id', type=int)

mark_in_progress = command.add_parser('mark-in-progress', help='Mark Task as In Progress')
mark_in_progress.add_argument('id', type=int)

mark_done = command.add_parser('mark-done', help='Mark Task as In Progress')
mark_done.add_argument('id', type=int)

mark_todo = command.add_parser('mark-to-do', help='Mark Task as To Do')
mark_todo.add_argument('id', type=int)

list = command.add_parser('list')
list.add_argument('status', nargs='?', help='Filter by status:\n\t0 - To Do\n\t1 - In Progress\n\t 2 - Done')


args = parser.parse_args()

if args.command in ['add', 'update']:
    args.description = ' '.join(args.description)

storage = Storage()
storage.load()


if args.command == 'add':
    newt = Task(
            _id = storage.last_id+1,
            description = args.description
        )
    storage.tasks[newt._id] = newt
    
    print(f'Task added:\n{newt}')
    
elif args.command == 'update':
    task = storage.tasks.get(args.id, None)
    if not task:
        print(f"Task with ID:<{args.id}> Not found!")
        raise SystemExit(0)
    task.update(description=args.description)
    storage.tasks[args.id] = task
    
    print(f'Task updated:\n{task}')
    
elif args.command == 'delete':
    task = storage.tasks.get(args.id, None)
    if not task:
        print(f"Task with ID:<{args.id}> Not found!")
        raise SystemExit(0)
    del storage.tasks[args.id]
    
    print(f'Task Deleted:\n{task}')
    
elif args.command in ('mark-in-progress', 'mark-to-do', 'mark-done'):
    status = {
        'mark-in-progress': TaskStatus.InProgress,
        'mark-to-do': TaskStatus.ToDo,
        'mark-done': TaskStatus.Done
    }
    task = storage.tasks.get(args.id, None)
    if not task:
        print(f"Task with ID:<{args.id}> Not found!")
        raise SystemExit(0)
    
    task.update(status=status[args.command])
    storage.tasks[task._id] = task
    
    print(f'Task Updated:\n{task}')

elif args.command == 'list':
    tasks = storage.tasks.values()
    if args.status:
        status = {
            '0': TaskStatus.ToDo,
            '1': TaskStatus.InProgress,
            '2': TaskStatus.Done
        }
        tasks = [task for task in storage.tasks.values() if task.status == status[args.status]]
    for task in tasks:
        print(task)

storage.save()
