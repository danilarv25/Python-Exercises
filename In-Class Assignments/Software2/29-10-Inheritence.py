class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees += 1
        self.id = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"Employee ID {self.id} : {self.first_name} {self.last_name}")

class HourlyWage(Employee):
    def __init__(self, first_name, last_name, wage:float):
        super().__init__(first_name, last_name)
        self.wage = wage

    def print_information(self):
        super().print_information()
        print(f"    Paid hourly: {self.wage} €")

class MonthlyWage(Employee):
    def __init__(self, first_name, last_name, wage:float):
        super().__init__(first_name, last_name)
        self.wage = wage

    def print_information(self):
        super().print_information()
        print(f"    Paid monthly: {self.wage} €")

employees = []

emp1 = Employee("Dan", "Jones")
emp2 = Employee("Susan", "Smith")
emp3 = HourlyWage("Chris", "Buchanen", 14.25)
emp4 = MonthlyWage("Jenni", "Karpalo", 2300)

employees.append(emp1)
employees.append(emp2)
employees.append(emp3)
employees.append(emp4)

for e in employees:
    e.print_information()