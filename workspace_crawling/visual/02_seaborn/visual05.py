import seaborn as sns
import matplotlib.pyplot as plt


penguins = sns.load_dataset('penguins')

# sns.boxplot(data=penguins, x='bill_length_mm')
# sns.boxplot(data=penguins, y='bill_length_mm')
sns.boxplot(data=penguins, x='species', y='bill_depth_mm', hue='sex')
plt.show()


