from employee import Employee
def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Salary: {self.salary}"

employees = {}

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))

    employees[emp_id] = Employee(emp_id, name, salary)
    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("No employees found")
        return

    print("\nEmployee List:")
    for emp in employees.values():
        print(emp)

def update_employee():
    emp_id = input("Enter Employee ID to update: ").strip()

    if emp_id not in employees:
        print("Employee not found")
        return

    new_name = input("Enter new Employee Name: ").strip()

    if not new_name:
        print("Name cannot be empty")
        return

    employees[emp_id].update(new_name)
    print("Employee updated successfully")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()

    if emp_id not in employees:
        print("Employee not found")
        return

    del employees[emp_id]
    print("Employee deleted successfully")

while True:
    print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Thank you! Exiting EMS...")
        break
    else:
        print("Invalid choice, try again")

emp1 = Employee(101, "Arun", 25000)
emp2 = Employee(102, "Kavi", 30000)

emp1.display()
print("----------")
emp2.display()