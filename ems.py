class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.reports = []

    def add_report(self, date, task, work_done, learning, issues, status):
        report = {
            "Date": date,
            "Task": task,
            "Work Done": work_done,
            "Learning": learning,
            "Issues": issues,
            "Status": status
        }
        self.reports.append(report)
        print("Report added successfully!\n")

    def view_reports(self):
        if not self.reports:
            print("No reports found.\n")
        else:
            for report in self.reports:
                print("----- Daily Task Report -----")
                for key, value in report.items():
                    print(f"{key}: {value}")
                print("-----------------------------\n")


# Main Program
employees = {}

while True:
    print("1. Add Employee")
    print("2. Add Daily Report")
    print("3. View Reports")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        employees[emp_id] = Employee(emp_id, name)
        print("Employee added successfully!\n")

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            date = input("Enter Date: ")
            task = input("Enter Task: ")
            work_done = input("Enter Work Done: ")
            learning = input("Enter Learning: ")
            issues = input("Enter Issues: ")
            status = input("Enter Status (Pending/Completed): ")

            employees[emp_id].add_report(date, task, work_done, learning, issues, status)
        else:
            print("Employee not found!\n")

    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            employees[emp_id].view_reports()
        else:
            print("Employee not found!\n")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.\n")