# def Hello():
#     print("Hello, World!")
#     return
# Hello()

# def Hello(name):
#     print(f"Hello, {name}!")
#     return
# Hello("GK") 

# def add(a, b):
#     return a + b
# result = add(301, 15) 
# print(f"The sum is: ",result)

# def great(name, msg) :
#     print(f"{name} says: {msg}")
# result = great(name = "GK", msg = "Hello")

def get_info():
    name = "Girish"
    age = 24
    city = "Sirohi"
    email = "girish123@gmail.com"

    return name, age, city, email

name, age, city, email = get_info()
print(f"Name : {name}")
print(f"Age : {age}")
print(f"City : {city}")
print(f"Email : {email}")

