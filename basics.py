#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pandas

sns.set_theme(style="ticks")

df = pandas.read_csv("data/table-1-1-mf.csv")

sns.relplot(data=df)

plt.show()
# %%
