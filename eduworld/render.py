# Must be run from containing folder

elements = ['attainment', 'header', 'spending2018']
html_snippets = {}

html_path = 'src/html'

template_file = open(f'{html_path}/template.html','r')
template = template_file.read()
template_file.close()

for element in elements:
  file = open(f'{html_path}/{element}.html')
  html_snippets[element] = file.read()
  file.close()

index = template.format(attainment=html_snippets['attainment'],
                        header=html_snippets['header'],
                        spending2018=html_snippets['spending2018'])

index_file = open('public/index.html','w')
index_file.write(index)

index_file.close()
