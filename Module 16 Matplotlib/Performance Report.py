import matplotlib.pyplot as plt

# Initialize data
x = [1, 2, 3, 4, 5]
y = [85, 87, 83, 86, 85]

# plt.plot(x, y, color="green") # Line Chart
# plt.bar(x, y, color="green") # Bar Chart
plt.scatter(x, y, color="green") # Scatter Chart
plt.title('Performance Report')
plt.xlabel('Semaster')
plt.ylabel('MArks')
plt.show()