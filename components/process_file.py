import csv
import re

def load_csv(file_name,delimiter=","):
    array = []
    with open(file_name, encoding="latin2") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            row = [row[0],*row[2:5],*row[6:8]]
            proccess_row_load(row)
            array.append(row)
    array[0] = proccess_first_row(array[0])
    return array

def proccess_first_row(row):
    return_row = []
    for item in row:
        return_row.append(re.match(r'^#(.*?)(\s|$)',item).group(1))
    return return_row

def proccess_row_load(row):
    row[0] = row[0].replace("-"," ")
    if len(row[1]) > 25:
        row[1] = row[1][0:25]
    
    title = re.match(r'(.*?)\/',row[2])
    if title:
        row[2] = title.group(1)
    if len(row[2]) > 25:
        row[2] = row[2][0:25]
    if len(row[3]) > 20:
        row[3] = row[3][0:20]

def sort_by_value(table, **options):
    if(options.get("reverse") == True):
        table.sort(key = lambda x: abs(float(x[4].replace(",",".").replace(" ",""))),reverse=True)
    else:
        table.sort(key = lambda x: abs(float(x[4].replace(",",".").replace(" ",""))))
    return table
