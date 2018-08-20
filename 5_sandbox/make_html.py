
import lorem

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

contents = {}

template = env.get_template('main.html')
with open('output.html', 'w') as fh:
    fh.write(template.render(contents))
    # You could also have written the following:
    # fh.write(template.render(**contents))
