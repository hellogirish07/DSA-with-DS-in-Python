import  matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Bins = ?

plt.title('Histogram')
plt.legend(["bar"])
plt.show()