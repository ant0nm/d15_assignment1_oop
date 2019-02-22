class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hi, my name is {}!".format(self.name)


class Student(Person):

    def learn(self):
        return "I get it!"

class Instructor(Person):

    def teach(self):
        return "An object is an instance of a class."

nadia = Instructor("Nadia")
print(nadia.greeting())
print(nadia.teach())

chris = Student("Chris")
print(chris.greeting())
print(chris.learn())

# this will throw an AttributeError stating that 'Student' object has no attribute 'teach'
# calling the teach() method on an instance of the Student class won't work
# that is because the Student class does not define a method called teach()
# the teach() method is only defined for instances of the Instructor class
# the only method unique to the Student class is the learn() method
# teach() is unique to the Instructor class and can only be called on instances of that class
# print(chris.teach())
