from bokeh.sampledata import us_states
from bokeh.plotting import figure, save, output_file
import pandas as pd
import math

output_file('/home/sam/Documents/Projects/Software/eduworld/eduworld/src/html/spending.html')

us_states = us_states.data.copy()

del us_states["HI"]
del us_states["AK"]

state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

colors = ["#754beb", "#8b4beb", "#a04beb", "#cb4beb", "#e64beb", "#eb4bd6", "#eb4bb6", "#eb4b9e", "#eb4b78", "#eb4b4b" ]
state_colors = []

spendingdf = pd.read_csv('/home/sam/Documents/Projects/Software/eduworld/eduworld/src/data/spending2018/2018_spending_by_state_elementary_secondary.csv')

maximum = spendingdf.Total.max()

def of_max(state):
  return math.floor((spendingdf.loc[spendingdf.State == state, 'Total']/maximum) * 10)

for state in us_states:
  try:
    idx = of_max(state) - 1
    state_colors.append(colors[idx])
  except KeyError:
    state_colors.append("white")

p = figure(title="US Primary-Secondary Education Spending 2018", plot_width=900, plot_height=700)
p.patches(state_xs, state_ys, fill_color=state_colors, fill_alpha=0.7,line_color="black")

save(p)
