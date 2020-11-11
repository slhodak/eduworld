import pandas as pd
from bokeh.plotting import figure, output_file, save, show
import math

output_file('../html/enrollment_2017.html')

df = pd.read_csv('../data/enrollment_by_grade_2017.csv')

colors = [ "#355070", "#6d597a", "#b56576", "#e56b6f", "#eaac8b", "#d8e2dc", "#ffe5d9", "#f4acb7", "#9d8189", "#d4e09b", "#f6f4d2", "#cbdfbd", "#f19c79", "#cad2c5", "#52796f", "#354f52"]

p = figure(x_range=df.columns.tolist(), plot_width=800, x_axis_label='Grade', y_axis_label='Enrollment', title='Primary and Secondary School Enrollment by Grade (USA, 2017)')
p.vbar(x=df.columns.tolist(), top=df.iloc[0].tolist(), width=0.8, fill_color=colors)
p.xaxis.major_label_orientation = math.pi/5
p.title.text_font_size = '14pt'

save(p)
