import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
# plt.scatter(x, y, color='red', marker='o')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()