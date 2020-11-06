## Visualizations of education-related data.

### Setup
1. `python3 render.py`
2. Navigate to `public/index.html`

### Add Charts
1. Add chart html file to `src` named for the new element
2. Include the element in `src/html/template.html` somewhere in `<body>`
3. Add the name of the element to the list of elements atop render.py
3. In `render.py`, add the element name and its lookup in `html_snippets` to the arguments of `template.format()`

## To-do
### Plots
1. Hover show values (attainment)
2. Pandas for data manipulation for attainment chart
3. 2nd chart
### Server
1. Environment variables for file paths used by various scripts
2. Create server
### Front-End
1. Footer inviting contributors
2. Do not refactor chart sub-template w/citation. Do this way until you __need__ a solution.