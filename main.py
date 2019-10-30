from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

j2_env = Environment(loader=FileSystemLoader('templates'),                                                                                                                            
                     trim_blocks=True)

template = j2_env.get_template('readme.md.j2')

rendered_file = template.render(
name='guiadco',
website='https://ccl-consulting.fr',
logo='docs/logo.pnj',
email='guiadco@geekhomeinside.com',
issue='issues',
project='jinja2-readme',
namespace='ccl-consulting',
github='https://github.com',
release='release',
badges='test'
)

print(rendered_file)

# to save the results
with open("README.md", "w") as fh:
    fh.write(rendered_file)