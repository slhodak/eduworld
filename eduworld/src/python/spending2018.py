from bokeh.sampledata import us_states
from bokeh.plotting import figure, save, output_file
import pandas as pd
import math

output_file('../html/spending.html')

us_states = us_states.data.copy()

del us_states["HI"]
del us_states["AK"]
del us_states["DC"]

state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

colors = ["#66faff", "#66bfff", "#6669ff", "#8f66ff", "#ab66ff", "#e566ff", "#ff66e8", "#ff66b3", "#ff668f", "#ff6666" ]

spendingdf = pd.read_csv('/home/sam/Documents/Projects/Software/eduworld/eduworld/src/data/spending2018/2018_states_edu_gdp.csv')

# To calculate edu spending-to-gdp ratio
def gdp_proportion(state):
    gdp = spendingdf.loc[spendingdf.State == state, 'GDP'].values[0] * 1000
    spending = spendingdf.loc[spendingdf.State == state, 'Education Spending'].values[0]
    return spending / gdp

ratios = []
for state in us_states:
    try:
        idx = gdp_proportion(state)
        ratios.append(idx)
    except KeyError:
        next

# Scale ratios to get widest range of colors
oldMax = max(ratios)
oldMin = min(ratios)
oldRange = oldMax - oldMin
def scaled_index(oldValue):
    return math.floor((oldValue - oldMin) / oldRange * 9)

state_colors = []
for ratio in ratios:
    state_colors.append(colors[scaled_index(ratio)])

height = 450
width = 650
p = figure(title="Primary-Secondary Education Spending as a Proportion of GDP (USA, 2018)", plot_width=width, plot_height=height)
p.patches(state_xs, state_ys, fill_color=state_colors, fill_alpha=0.7, line_color="black")

save(p)
