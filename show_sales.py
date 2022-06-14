import sys
import math

sales_file_name = 'sales.csv'

start = 1
if len(sys.argv) >= 2:
    start = int(sys.argv[1])

end = math.inf
if len(sys.argv) == 3:
    end = int(sys.argv[2])

with open(sales_file_name, 'r', encoding='utf-8') as file:
    for i, l in enumerate(file):
        file_index = i + 1
        if start <= file_index <= end:
            print(l.strip())