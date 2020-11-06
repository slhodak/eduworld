elements = ['attainment', 'header']
html_snippets = {}

template_file = open('src/template.html','r')
template = template_file.read()
template_file.close()


for element in elements:
  file = open(f'src/{element}.html')
  html_snippets[element] = file.read()
  file.close()

index = template.format(attainment=html_snippets['attainment'],
                        header=html_snippets['header'])

index_file = open('public/index.html','w')
index_file.write(index)

index_file.close()
