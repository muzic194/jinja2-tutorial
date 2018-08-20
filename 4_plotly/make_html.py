

import pandas

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

contents = {}

contents['header'] = "My Webpage"
contents['title'] = "Random Page"
contents['introduction'] = "This is a random page containing some results for users"

csv_data = pandas.read_csv('./data/dataset_r_values.csv', index_col=0)
contents['plots'] = [
                        {
                             'title':'My fancy plot',
                             'div':'plot0',
                             'json':csv_data.T.to_json(orient='split'),
                        },
                    ]

template = env.get_template('main.html')
with open('output.html', 'w') as fh:
    fh.write(template.render(contents))
    # You could also have written the following:
    # fh.write(template.render(**contents))
