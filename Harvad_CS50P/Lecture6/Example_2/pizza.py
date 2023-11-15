import csv
import sys
from tabulate import tabulate

def argv_range(sys: int) -> bool:
    if len(sys) > 2:
        print('Too many command-line arguments')
    elif len(sys) < 2:
        print('Too few command-line arguments')
        return False
    else:
        return True
    

def pizza(file_name: str):
    table = []
    with open(f'{file_name}') as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        print(tabulate(table[1:], headers=table[0], tablefmt='grid'))



def main():
    length = argv_range(sys.argv)
    if length:
        if sys.argv[1].endswith('.csv'):
            try:
                pizza(sys.argv[1])
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a CSV file')
    else:
        sys.exit()



main()
    