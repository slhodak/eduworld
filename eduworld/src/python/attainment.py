# Must be run from containing folder

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3

df = pd.read_csv('../data/table-1-1-mf.csv')
grouped = df.set_index('Age Group')
sns.set_theme(style='ticks')
plot = sns.relplot(data=grouped, height=4, aspect=2)
figure = plot.fig

html_str = mpld3.fig_to_html(figure)
Html_file = open("../html/attainment.html","w")
Html_file.write(html_str)
Html_file.close()
