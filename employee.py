class Employee:
    def __init__(self, emp_id, name, salary=0):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def update(self, name):
        self.name = name

    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name}"

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)