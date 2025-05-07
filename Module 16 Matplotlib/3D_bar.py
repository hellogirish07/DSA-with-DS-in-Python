import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # optional, but good practice for 3D

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 76, 25]
z = [0, 0, 0, 0, 0]  # base z-position (usually zero)

dx = [0.5] * 5  # width of bars in x-direction
dy = [0.5] * 5  # width of bars in y-direction
dz = [1, 8, 27, 64, 125]  # height of each bar

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.bar3d(x, y, z, dx, dy, dz)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Bar Chart')
plt.show()
