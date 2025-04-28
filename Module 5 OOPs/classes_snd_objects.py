# class my_class:
#     print("Hello from Class")

# class_data = my_class()
# print(class_data)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print("Car Started")

    def drive(self):
        if self.is_running:
            print("Car is Moving")
        else:
            print("Car is not started yet")
    
my_car = Car("Lemborghini", "Sian", "2019")
print("My Car :",my_car.brand, my_car.model, my_car.year)
my_car.start()
my_car.drive()