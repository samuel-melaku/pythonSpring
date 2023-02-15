# object orientated programming in Python
x = 1
y = 1
print(x + y)

print(type(x))

def hello():
    print('hello')
print(type(hello))

string = 'hello'
print(string.upper()) # .<operator> is a method

class Dog:
    def __init__(self, name):
        self.name = name

    def add_one(self, x):
        return x + 1    
    def bark(self):
        print("bark") # a method is a function inside of a class
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
dogs_name = ['tim', 'bill']
dogs_age = [32, 14]


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init_(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade() 

        return value / len(self.students)
course = Course('Science', 2)
s1 = Student('sam', 15, 100)
s2 = Student('ahmad', 15, 85)
s3 = Student('artisan', 15, 93)
print(course.get_average_grade())

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("bark")


class Person:
    number_of_people = 0
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

    def number_of_people(cLs):
        return cLs.number_of_people()
        
p1 = Person('tim')
p2 = Person('sam')

Person.number_of_people = 8
print(Person.number_of_people)
print(Person.number_of_people)
print(p1.number_of_people)
