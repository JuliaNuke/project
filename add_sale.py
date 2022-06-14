import sys

sales_file_name = 'sales.csv'

if len(sys.argv) == 1:
    print('Price required')
    exit(1)

with open(sales_file_name, 'a', encoding='utf-8') as file:
    file.write(f'{sys.argv[1].strip()}\n')