# with open('Module 6/file.file.txt', 'w') as file:
#     file.write('Hello, world!')
#     print("Data written")

# with open('Module 6/file.file.txt', 'r') as file:
#     data = file.read()
#     print("File Data :\n", data)

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exe_type, exe_val, exe_tb):
        print("Exiting the context")
    
    def do_something(self):
        print("Doing something")
    
with MyContextManager() as manager:
    manager.do_something()