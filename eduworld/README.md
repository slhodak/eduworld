## Visualizations of education-related data.

### Setup
1. `python3 render.py`
2. Navigate to `public/index.html`

### Update page elements
1. Add an html file in `src` named for the element
2. Include the element in `src/html/template.html` somewhere in `<body>`
3. Add the name of the element to the list of elements atop render.py
3. In `render.py`, add the element name and its lookup in `html_snippets` to the arguments of `template.format()`

## To-do
### Plots
1. Key and clarity of Attainment chart
2. Chart cut off?
3. 2nd chart
### Server
1. Environment variables for file paths used by various scripts
2. Create server
### Front-End
1. Header design
2. Citations