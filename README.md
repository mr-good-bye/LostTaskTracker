# LostTaskTracker
Simple Task Tracker

Implementation of https://roadmap.sh/projects/task-tracker

Task tracker is a project used to track and manage your tasks. A simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.

## Usage

```sh

# Adding a new task
main add "Buy groceries"

# Updating and deleting tasks
main update 1 "Buy groceries and cook dinner"
main delete 1

# Marking a task as in progress or done
main mark-in-progress 1
main mark-done 1
main mark-to-do 1

# Listing all tasks
main list

# Listing tasks by status
main list done
main list todo
main list in-progress
```


## Task Properties

```yaml
id: A unique identifier for the task (incremental int)
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
```

