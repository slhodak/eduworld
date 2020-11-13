# Must be run from containing folder

elements = ['attainment', 'header', 'enrollment_2017', 'salary_and_spending']
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
                        enrollment_2017=html_snippets['enrollment_2017'],
                        salary_and_spending=html_snippets['salary_and_spending'])

index_file = open('public/index.html','w')
index_file.write(index)

index_file.close()
