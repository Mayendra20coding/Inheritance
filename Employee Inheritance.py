class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):

        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post
    def display(self):
        super().display()
        print("Salary:", self.salary)
        print("Post:", self.post)
a = Employee('Rahul', 886012, 200000, "Intern")
a.display()