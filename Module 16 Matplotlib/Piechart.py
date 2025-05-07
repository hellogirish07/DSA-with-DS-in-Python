import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
e = [0.1, 0, 0, 0]  # Explode only the first slice

plt.pie(x, explode=e)
plt.title('Pie Chart')
plt.show()
