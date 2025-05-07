import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 76, 25]
z = [1, 8, 27, 64, 125]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z)
plt.show()