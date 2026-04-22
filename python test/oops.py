# Create class
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to display details
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

# Create 2 objects
emp1 = Employee("Nifla", 25000)
emp2 = Employee("Rahul", 30000)

# Call method
emp1.display()
print("-----")
emp2.display()

