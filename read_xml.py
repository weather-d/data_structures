import xmltodict
from pprint import pprint

XMLFILEPATH = "data_structures/xml_example.xml"

def setNewAddress(xml_dict):
    ip = input("IP Address: ")
    netmask = input("Netmask: ")
    newNetwork = [{"ip": ip, "netmask": netmask}]
    xml_dict["root"]["addresses"] += newNetwork

    return xml_dict


def writeToXML(entry):
    with open(XMLFILEPATH, 'w') as data: 
        data.write(xmltodict.unparse(entry, pretty=True))


def readFromXML():
    with open(XMLFILEPATH, 'r') as data: 
        xml_dict = xmltodict.parse(data.read())

    return xml_dict


answer = input("Would you like to add a network? (y/n)")

if answer == 'y': 
    writeToXML(setNewAddress(readFromXML()))
elif answer =='n':
   pass
else:
    print("Not y/n. You don't get to add now.")

pprint(readFromXML())