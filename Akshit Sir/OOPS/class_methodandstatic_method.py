class Employee:
    # class variable
    no_of_employess = 0
    # raise_amount =

    def __init__(self, name, salary):
        # variable inside method is called instance variable
        self.name = name
        self.salary = salary

        Employee.no_of_employess += 1

    def raise_salary(self):
        self.salary = self.salary * Employee.raise_amount

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        salary = float(salary)
        return cls(name, salary)
    # cls represent the method of class

    @classmethod
    def from_list(cls, data):
        name, salary = data
        return cls(name, salary)

    @staticmethod
    def is_holiday(day):
        if day.weekday() in [5, 6]:
            return True
        return False

    def display_details(self):
        print(f"Name:{self.name},Salary:{self.salary}")


akshit = Employee("Akshit", 10000)
viral = Employee("Viral", 8000)

akshit.display_details()
viral.display_details()


# if u get value in string faction and u have to assign this value for making obejct constructot and pass that value as parameter
# to constructor
