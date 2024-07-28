import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

new_df = pd.read_csv('Au_nanoparticle_dataset.csv')

new_dif = new_df.loc[:, (df.columns != 'N_total') &  (df.columns != 'N_bulk') & (df.columns != 'N_surface') & (df.columns != ' R_avg columns')]

new_dif.head(20)

N_total_var = np.var(new_df.loc[:,'N_total'])
print(N_total_var)

N_total_mean = np.mean(new_df.loc[:,'N_total'])
print(N_total_mean )

quantile_25 = new_df.loc[:,'N_total'].quantile(0.25)
quantile_50 = new_df.loc[:,'N_total'].quantile(0.50)
quantile_75 = new_df.loc[:,'N_total'].quantile(0.75)
print('quantile_25' , quantile_25)
print('quantile_50' ,quantile_50)
print('quantile_75' ,quantile_75)

N_bulk_var = np.var(new_df.loc[:,'N_bulk'])
print(N_bulk_var)

N_bulk_mean = np.mean(new_df.loc[:,'N_bulk'])
print(N_bulk_mean )

quantile_25 = new_df.loc[:,'N_bulk'].quantile(0.25)
quantile_50 = new_df.loc[:,'N_bulk'].quantile(0.50)
quantile_75 = new_df.loc[:,'N_bulk'].quantile(0.75)
print('quantile_25' , quantile_25)
print('quantile_50' ,quantile_50)
print('quantile_75' ,quantile_75)

N_surface_var = np.var(new_df.loc[:,'N_surface'])
print(N_surface_var)

N_surface_mean = np.mean(new_df.loc[:,'N_surface'])
print(N_surface_mean )

quantile_25 = new_df.loc[:,'N_surface'].quantile(0.25)
quantile_50 = new_df.loc[:,'N_surface'].quantile(0.50)
quantile_75 = new_df.loc[:,'N_surface'].quantile(0.75)
print('quantile_25' , quantile_25)
print('quantile_50' ,quantile_50)
print('quantile_75' ,quantile_75)


R_avg_var = np.var(new_df.loc[:,'R_avg'])
print(R_avg_var)

R_avg_mean = np.mean(new_df.loc[:,'R_avg'])
print(R_avg_mean )

quantile_25 = new_df.loc[:,'R_avg'].quantile(0.25)
quantile_50 = new_df.loc[:,'R_avg'].quantile(0.50)
quantile_75 = new_df.loc[:,'R_avg'].quantile(0.75)
print('quantile_25' , quantile_25)
print('quantile_50' ,quantile_50)
print('quantile_75' ,quantile_75)


plt.hist(new_df.loc[:,'N_total'], bins=30, color='skyblue', edgecolor='black')

plt.hist(new_df.loc[:,'N_bulk'], bins=30, color='skyblue', edgecolor='black')

plt.hist(new_df.loc[:,'N_surface'], bins=30, color='skyblue', edgecolor='black')

plt.hist(new_df.loc[:,'R_avg'], bins=30, color='skyblue', edgecolor='black')


selected_vars = new_df[['N_total','N_bulk','N_surface','R_avg']]
sns.pairplot(selected_vars)
plt.show()

g = sns.PairGrid(new_df)
g.map_upper(sns.histplot)
g.map_diag(sns.histplot)
g.map_lower(sns.kdeplot) 