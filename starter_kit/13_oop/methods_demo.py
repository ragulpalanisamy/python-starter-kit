class Employee:
    company = "TechCorp" # Class variable

    def __init__(self, name, salary):
        self.name = name     # Instance variable
        self.salary = salary # Instance variable

    # 1. Instance Method
    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    # 2. Class Method
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    # 3. Static Method
    @staticmethod
    def is_work_day(day):
        return day.lower() not in ["saturday", "sunday"]

def main():
    emp = Employee("Alice", 50000)
    
    # Instance method
    print(emp.get_details())
    
    # Class method
    Employee.change_company("InnovateX")
    print(f"New Company: {emp.company}")
    
    # Static method
    print(f"Is Monday a work day? {Employee.is_work_day('Monday')}")

if __name__ == "__main__":
    main()
