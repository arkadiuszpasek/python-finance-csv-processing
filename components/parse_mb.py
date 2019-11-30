import csv

def load_csv(file_name,delimiter=","):
    array = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        reading_started = False
        for row in csv_reader:
            if len(row) == 0:
                if reading_started:
                    break
                else:
                    continue

            proccess_row = False

            if reading_started or row[0].startswith("#Data op"):
                reading_started = True
                proccess_row = True
            elif row[0].startswith("#Saldo"):
                print("Saldo poczatkowe: " + row[1])
            elif row[0].startswith("#Za okres"):
                row = csv_reader.__next__()
                print("Za okres [%s]-[%s]" % (row[0],row[1]))
            
            if proccess_row:
                row = [row[0],*row[2:5],*row[6:8]]
                array.append(row)
    return array