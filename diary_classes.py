class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.math = []
        self.physics = []
        self.chemistry = []

    def __repr__(self):
        return f'Student(name={self.name}, surname={self.surname}, age={self.age})'

    def __str__(self):
        return f'{self.name} {self.surname} {self.age}'