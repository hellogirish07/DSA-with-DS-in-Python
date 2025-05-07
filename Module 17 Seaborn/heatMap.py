import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

data = np.random.randint(1, 11, size=(5, 3))
print(data)
sb.heatmap(data)
plt.show()

