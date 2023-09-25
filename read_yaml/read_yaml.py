import yaml
from pprint import pprint

with open("data_structures/read_yaml/yaml_example.yaml") as data: 
    yaml_dict = yaml.safe_load(data.read())
newAddress = [{"ip": "172.16.0.5", "netmask": "255.255.255.0"}]

yaml_dict["addresses"] += newAddress

pprint(yaml.dump(yaml_dict))
pprint(yaml.dump(yaml_dict, default_flow_style=False))
pprint(yaml.dump(yaml_dict, default_flow_style=True))

with open("data_structures/read_yaml/yaml_example.yaml", "w") as data: 
    data.write(yaml.dump(yaml_dict, default_flow_style=False))