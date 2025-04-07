class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def is_passed(self):
        if self.grade > 40:
            return "PASS"
        else:
            return "FAIL"  # Add this line for completeness

# Creating an object
obj = Student('Rahul', 23, 40)

# Using methods
print(obj.get_grade())       # Outputs: 40
print(obj.is_passed())       # Outputs: FAIL


class Student:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, add):
        self.balance += add  # Update the object's balance
        return self.balance

# Create an instance
a = Student(2333, 500)

# Call deposit method
print(a.deposit(100))  # Output: 600





