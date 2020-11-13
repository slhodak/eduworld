import pandas as pd
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, Label, LabelSet

output_file('../html/salary_and_spending.html')

df = pd.read_csv('../data/pupil_spending_teacher_salary/spending_and_salary.csv')

ratio = []
for row in df.axes[0]:
    ratio.append(df.loc[row]['Avg. Teacher Salary (2017)'] / df.loc[row]['Spending Per Pupil (2016)'])

df['ratio'] = ratio

cds = ColumnDataSource(dict(
    salary = df['Avg. Teacher Salary (2017)'],
    spending = df['Spending Per Pupil (2016)'],
    state = df.State,
    ratio = df.ratio,
    color = ['#d42681', '#ed8b4e', '#c2b167', '#61c77d', '#4d5ca1', '#382022', '#ec6ab3', '#d65681', '#ed8b4e', '#c2a167', '#61c72d', '#4d5ca1', '#382042', '#eb63b3', '#d6a681', '#ad8b2e', '#6cc77d', '#4d5ca1', '#382042', '#ebaab3', '#d65621', '#ec8b4e', '#c2b167', '#61c77d', '#4daca1', '#382022', '#fc6ab3', '#c2b167', '#6ac27d', '#4daca1', '#d65621', '#eb6ab3', '#d65681', '#ed8b4e', '#c2a167', '#61c77d', '#4dcca1', '#392642', '#eb6ab3', '#d6a681', '#ed8b2e', '#c2b167', '#d65681', '#ed8c4e', '#c2a167', '#61c72d', '#4c5ca1', '#392042', '#eb6ab3', '#d6a681', '#ed8b4e']
))

TOOLTIPS = [
    ("State", "@state"),
    ("Average Teacher Salary", "$@salary"),
    ("Spending Per Pupil", "$@spending"),
    ("Ratio", "@ratio")
]

p = figure(title='Teacher Salary & Spending Per Pupil by State',
            plot_width=800, plot_height=800,
            x_axis_label='Average Teacher Salary (2017)',
            y_axis_label='Spending Per Pupil (2016)', 
            tooltips=TOOLTIPS)

p.title.text_font_size='16pt'

labels = LabelSet(x='salary', y='spending', text='state', level='glyph', x_offset=-3, y_offset=5, source=cds, render_mode='canvas', text_font_size='8pt')
p.add_layout(labels)

p.square(x='salary', y='spending', fill_color='color', line_alpha=0, source=cds, size=12)

save(p)

