from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

j2_env = Environment(loader=FileSystemLoader('templates'),                                                                                                                            
                     trim_blocks=True)

template = j2_env.get_template('readme.md.j2')

rendered_file = template.render(name='mario', website='https://portfolio.geekhomeinside.com/', logo='docs/logo.pnj', email='guiadco@geekhomeinside.com')

print(rendered_file)