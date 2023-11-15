import sys

def argv_range(sys: int) -> bool:
    if len(sys) > 2:
        print('Too many command-line arguments')
        return False
    elif len(sys) < 2:
        print('Too few command-line arguments')
        return False
    else:
        return True
    

def counter(file_name: str):
    count = 0
    with open(f"{file_name}") as file:
        for row in file:
            if row.startswith('#'):
                pass
            elif row.isspace():
                pass
            else:
                count += 1
        print(count)


def main():
    lenght = argv_range(sys.argv)
    if lenght:
        if sys.argv[1].endswith('.py'):
            try:
                counter(sys.argv[1])
            except FileNotFoundError:
                print('File does not exist')
                sys.exit()
        else:
            print('Not a python file')
            sys.exit()
    else:
        sys.exit()


main()