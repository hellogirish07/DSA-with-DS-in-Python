import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('tips')

sb.set_style('whitegrid')
# Hist
# fg = sb.FacetGrid(df, col = "time", row = "smoker")
# fg.map(plt.hist, "tip", color = "red")

# scatter
# fg = sb.FacetGrid(df, col = "time", row = "smoker")
# fg.map(plt.scatter, "total_bill","tip", color = "red", edgecolor = "blue")

fg = sb.FacetGrid(df, col="time", row="sex")
fg = fg.map(plt.scatter, "total_bill", "tip")
fg = fg.add_legend()
plt.show()