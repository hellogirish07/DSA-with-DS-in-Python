# class Animal:
#     def speak(self):
#         print("The animal make a sound")

# class Dog(Animal):
#     def speak(self):
#         print("The Dog Barks")

# animal = Animal()
# dog = Dog()

# animal.speak()
# dog.speak()

class Shape:
    def Area(self, side1=None, side2=None):
        if side1 is not None and side2 is not None:
            return side1 * side2
        elif side1 is not None:
            return side1 * side1  # Treat as a square
        else:
            return 0

shape = Shape()
print(shape.Area(5, 10))  # Output: 50
print(shape.Area(5))      # Output: 25 (Assuming a square)
print(shape.Area())       # Output: 0

