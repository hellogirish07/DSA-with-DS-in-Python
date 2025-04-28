with open('file.txt', 'w') as file:
    file.write('Hello, world! \n Hello GK \n Hello Python')
    print("File Written")

with open('file.txt', 'r') as file:
    data = file.read()
    print("Using read() : \n" ,data)

with open('file.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    print("Using readline() : \n", line1, line2, line3 )
