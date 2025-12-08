
from jinja2 import Environment, FileSystemLoader

# loading the environment
env = Environment(loader = FileSystemLoader('.'))

# loading the template
template = env.get_template('template.html')

# rendering the template and storing the resultant text in variable output
content = template.render(
    cpu_load = '50%',
    ram_size = '6G',
    ram_load = '30%',
    storage_size = '70G',
    storage_load = '70%'
)

# printing the output on screen
print(content)

with open('index.html', 'w') as file:
    file.write(content)