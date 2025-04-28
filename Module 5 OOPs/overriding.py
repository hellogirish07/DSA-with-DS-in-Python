# class Shape:
#     def area(self):
#         return 0

# class Squere(Shape):
#     def area(self):
#         side = 5
#         return side * side

# squere = Squere()
# print("The Area of Squere : ",squere.area())

class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person : {self.name}"
    
class Employ(Person):
    def __str__(self):
        return f"Employ : {self.name}"

employ = Employ("GK")
print(employ)