import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('tips')
print(df.head())

sb.set_style('whitegrid')
gender_palette = ["red", "blue"]
sb.swarmplot(x="day", y="tip", hue="sex", palette=gender_palette, data=df)

plt.show()