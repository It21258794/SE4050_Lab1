import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

nums = np.random.rand(4,4)
exp_array = np.exp(nums)
print(exp_array)


plt.hist(np.random.rand(100000), density=True, bins=100, histtype="step", color="blue",
label="rand")
plt.axis([-2.5, 1.5, 0, 1.1])
plt.legend(loc = "upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

z = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')


ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()


df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')

pearson_corr = df.corr(numeric_only=True,method='pearson')
pearson_corr

plt.figure(figsize=(9,8))
sns.heatmap(pearson_corr)

spearman_corr = df.corr(numeric_only=True,method='spearman')
spearman_corr

plt.figure(figsize=(9,8))
sns.heatmap(spearman_corr)



