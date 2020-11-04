#%%

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pandas

sns.set_theme()

ages = pandas.read_csv("data/simplest-data.csv")

sns.relplot(
  data=ages,
  x="name", y="age", hue="age"
)

plt.show()

# %%
