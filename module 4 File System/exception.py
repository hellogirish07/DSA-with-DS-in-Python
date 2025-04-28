# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")

# try:
#     value = int("ABC")
# except ValueError:
#     print("Error: Invalid input")  
# except TypeError:
#     print("Error: Type Error")  

# try:
#     result = 20 / 2
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")
# else:
#     print("Result is:", result)
# finally:
#     print("This will always be executed")

# class CustoemError(Exception):
#     pass
# try:
#     raise CustoemError("This is a Custom Error Message")
# except CustoemError as e:
#     print("Caught exception:", e) 

try:
    file = open('module 4/file_2.txt', 'r')
except FileNotFoundError:
    print("Error : File not found")
else:
    print("Done : File found")
    with open('file_2.txt', 'w') as file:
        file.write("Hello, World!")
        print("Done : Data Written")
finally:
    print("Cleanup : Closing the file")
    if 'file' in locals():
        file.close() 