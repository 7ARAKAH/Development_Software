# Python Object-Oriented Programming

class Employee:
    
    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Hany', 'AbuShall', 'abushall@hany.space', 55000)
emp2 = Employee('Katherine', 'Haenschen', 'keh303@gmail.com', 67000)

print(emp2.fullname())