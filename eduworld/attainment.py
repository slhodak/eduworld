#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pandas

sns.set_theme(style="ticks")

df = pandas.read_csv("data/table-1-1-mf.csv")
grouped = df.set_index("Age Group")
sns.relplot(data=grouped, height=5, aspect=2)

plt.show()
# %%
