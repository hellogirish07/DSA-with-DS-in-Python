class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def great(self):
        print("Hello, My name is ", self.name)
    
    def birthday(self):
        self.age += 1
        print("Happy Birthday ! Now i am ", self.age)

person1 = Person("Girish", 22)
print("Name :", person1.name)
print("Age :", person1.age)

person1.great()
person1.birthday()