

## Visualizations of education-related data.
---
### Updating the page elements
1. Add an html file in `src` named for the element
2. Include the element in `src/html/template.html` somewhere in `<body>`
3. Add the name of the element to the list of elements atop render.py
3. In `render.py`, add the element name and its lookup in `html_snippets` to the arguments of `template.format()`