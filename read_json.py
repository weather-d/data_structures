import json
from pprint import pprint

JSONFILEPATH = "data_structures/json_example.json"

def setNewAddress(json_dict):
    ip = input("IP Address: ")
    netmask = input("Netmask: ")
    newNetwork = [{"ip": ip, "netmask": netmask}]
    json_dict["addresses"] += newNetwork

    return json_dict

def writeToJSON(entry):
    with open(JSONFILEPATH, 'w') as data: 
        json.dump(entry, data, indent=4)


def readFromJSON():
    with open(JSONFILEPATH, 'r') as data: 
        json_dict = json.loads(data.read())

    return json_dict


answer = input("Would you like to add a network? (y/n)")

if answer == 'y': 
    writeToJSON(setNewAddress(readFromJSON()))

pprint(readFromJSON())


