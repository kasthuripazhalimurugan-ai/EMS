class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        print(f"\nTasks for {self.name}:")
        if not self.tasks:
            print("No tasks assigned")
        for task in self.tasks:
            print(f"- {task.title} ({task.status})")


# Task class
class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"


# ----- Main Logic -----

# Create employees
emp1 = Employee(1, "John")
emp2 = Employee(2, "Alice")

task1 = Task(101, "Fix Login Bug", "Resolve authentication issue")
task2 = Task(102, "Update Dashboard", "Improve UI design")

# Assign tasks
emp1.assign_task(task1)
emp2.assign_task(task2)

# Mark one task as completed
task1.mark_completed()

# Display tasks
emp1.show_tasks()
emp2.show_tasks()