import matplotlib.pyplot as plt, mpld3
plot = plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
#mpld3.show() # hosts graph at localhost:8888

html = mpld3.fig_to_html(plot.fig)
file = open('html.html','w')
file.write(html)
file.close()
