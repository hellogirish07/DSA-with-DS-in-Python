import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('tips')

sb.set_style('whitegrid')
day_palette = ["red", "blue", "green", "yellow"]
# sb.violinplot(x = df['tip'], color='lightblue')
sb.violinplot(x = "day", y = "total_bill", palette=day_palette, data = df)
plt.show()