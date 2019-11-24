# import csv
import re
import sys
from components import out
from components import process_file

arr = process_file.load_csv("data/74340910_190823_191123",";")

if len(sys.argv) > 1 and sys.argv[1] == "sort":
    arr[1:] = process_file.sort_by_value(arr[1:])

out.print_table(arr)
