import sys
import csv

def argv_range(sys: int) -> bool:
    if len(sys) > 3:
        print('Too many command-line arguments')
        return False
    elif len(sys) < 3:
        print('Too few command-line arguments')
        return False
    else:
        return True


def names(file_name: str) -> list:
    students = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})
    return students


def convert_names(students: list) -> list:
    new_students_list = []
    for name in students:
        full_name = name['name']
        last_name, first_name= full_name.split(',')
        new_students_list.append({'name':f'{first_name.replace(' ', '')}, {last_name}', 'house': name['house']})
    return new_students_list


def write_csv(new_students: list):
    with open('after.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'house'])
        writer.writeheader()
        for names in new_students:
            writer.writerow({'name': names['name'], 'house': names['house']})


def main():
    length = argv_range(sys.argv)
    if length == True:
        if sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv'):
            try:
                information = names(sys.argv[1])
                new_names_list = convert_names(information)
                write_csv(new_names_list)
            except FileNotFoundError:
                print(f'{sys.argv[1]} does not exist')
        else:
            print(f'{sys.argv[1]} or {sys.argv[2]} are not a CSV file')
    else:
        sys.exit()


main()