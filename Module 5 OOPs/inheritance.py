class Animal:
    def speak():
        print("The animal makes a sound")
    
class Dog(Animal):
    def bark():
        print("The dog barks")
        
    def weg_tail():
        print("The dog wags its tail")

dog = Dog()
Dog.speak()
Dog.bark()