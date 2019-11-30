# import csv
import re
import sys
from components import out
from components import process_file
from components import parse_mb

args = {}
for line in sys.stdin:
    sys.argv.append(line.strip())

for i in range(1,len(sys.argv)):
    if sys.argv[i].startswith("-"):
        if sys.argv[i][1:] == "file":
            args["file"] = sys.argv[i+1] if sys.argv[i+1] else None
        if sys.argv[i][1:] == "sort":
            args["sort"] = True
            args["reverse"] = True if i < len(sys.argv) - 1 and sys.argv[i+1] in ['r','reverse'] else False 

if not "file" in args:
    print("No file specified: use flag -file filename")
else:
    arr = parse_mb.load_csv(args["file"] if args["file"].endswith(".csv") else args["file"] + ".csv" , ";")
    arr = process_file.load_from_array(arr)
    if "sort" in args:
        arr[1:] = process_file.sort_by_value(arr[1:],reverse=args["reverse"])

    out.print_table(arr)
