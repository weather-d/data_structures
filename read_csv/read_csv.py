import csv


CSVFILEPATH = "data_structures/read_csv/csv_example.csv"


def csvToList(fileName):
    with open(fileName) as data:
        csv_data = list(csv.reader(data))

    return csv_data


def writeToCsv(filename, inputList):
    with open(filename, 'a', newline='\n') as data:
        csv.writer(data).writerow(inputList)


for item in csvToList(CSVFILEPATH):
    if len(item) > 0:
        print("Interface Name:", item[0])
        print("Nework Name:", item[1])
        print("IP Address:", item[2])
        print("\n")


answer = input("Add new Interface (y/n)?")

if(answer == "y"):
    intName = input("Interface name:")
    netName = input("Network name:")
    ipAdd = input("IP Address:")
    input = [intName, netName, ipAdd]
    writeToCsv(CSVFILEPATH, input)

