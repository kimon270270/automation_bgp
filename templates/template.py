from jinja2 import Environment, FileSystemLoader
import os
import yaml

# loading template
env = Environment (loader = FileSystemLoader("templates/"))
template = env.get_template("template.j2")


# loading variables for template
# list of path to yml file
yml_dir = "./device_configs_yaml"
yml_paths = os.listdir(yml_dir)

# getting full path
paths = []
for path in yml_paths:
    paths.append(os.path.join(yml_dir, path))

# rendering template for each yml file
for path in paths:
    # getting device name from the file
    '''
    file_name = os.path.basename(path)
    file = file_name.split(".")
    device_name = file[0]
    '''

    # getting device name from yml file
    # with open (path) as f:
    with open ("device_configs_yaml/Router1.yml") as f:
        data = yaml.safe_load(f)
        device_name = data['device']['name']
        config = template.render(**data)        # need to use ** when passing in raw dictonary


    # cerating config file for each device
    with open (f"device_configs/{device_name}.txt", "w") as f:
        f.write(config)

