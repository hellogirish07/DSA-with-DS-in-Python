# list = [1, 2, 3, 4, 5]
# print(list)
# print(list[0], list[-1])

# list.append(6)
# list.append(7)
# list.remove(7)
# list.insert(2,5)

# pop = list.pop()
# print("Popped Element = ",pop)
# print(list)

# liat_2 = [1,2,3,4,5,6,7,8,9,10]
# sub_list = liat_2[2:8]
# print("List =",liat_2)
# print("Sub List =",sub_list)

# print("Squere = ")
# squeree = [x ** 2 for x in range(10)]
# print(squeree)

# print("Even = ")
# even = [x for x in range(50) if x % 2 == 0]
# print(even)

# print("Odd = ")
# odd = [x for x in range(50) if x % 2 != 0]
# print(odd)

# print("Products =")
# products = [[i * j for j in range(3) for i in range(3)]]
# print(products)

words = ["Apple", "Banana", "Mango", "Orenge"]
length = [len(words) for word in words]
print(length)