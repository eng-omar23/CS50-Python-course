class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def is_completed(self):
        return self.completed

    def set_completed(self, completed):
        self.completed = completed


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.set_completed(True)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_task_list(self):
        return self.tasks


# Create an instance of the ToDoList class
todo_list = ToDoList()

# Add tasks to the to-do list
task1 = Task("Buy groceries")
task2 = Task("Finish homework")
task3 = Task("Call a friend")
task4 = Task("Read Quraan")
task5 = Task("Read about emotional intelligence")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)
todo_list.add_task(task4)
todo_list.add_task(task5)

# Mark a task as completed
todo_list.mark_task_as_completed(1)

# Remove a task
todo_list.remove_task(3)
todo_list.remove_task(4)

# Get the task list
task_list = todo_list.get_task_list()

# Print the task descriptions and completion status
for task in task_list:
    print(f"Task: {task.get_description()}, Completed: {task.is_completed()}")
