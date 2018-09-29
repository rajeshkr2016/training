'''
1. Object-oriented programming creates reusable patterns of code to curtail redundancy in development projects.
One way that object-oriented programming achieves recyclable code is through inheritance,
when one subclass can leverage code from another base class.
2. Inheritance is when a class uses code constructed within another class.

'''

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname



class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())