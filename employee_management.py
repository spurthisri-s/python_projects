class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_department(self):
        print("Department:", self.department)


name = input("Enter Employee Name: ")
salary = input("Enter Salary: ")
department = input("Enter Department: ")

manager = Manager(name, salary, department)

manager.display()
manager.show_department()