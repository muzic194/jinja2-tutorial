
import lorem

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

contents = {}

contents['header'] = "My Webpage"
contents['title'] = "Random Page"
contents['introduction'] = "This is a random page containing some results for users"

contents['paragraphs'] = []
for i in range(10):
    new_p = {}
    new_p['title'] = 'Paragraph {}'.format(i)
    new_p['text'] = lorem.paragraph()
    if i < 4:
        new_p['width'] = 6

    contents['paragraphs'].append(new_p)

template = env.get_template('main.html')
with open('output.html', 'w') as fh:
    fh.write(template.render(contents))
    # You could also have written the following:
    # fh.write(template.render(**contents))
