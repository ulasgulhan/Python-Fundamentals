
# File I/O
# Dosya açma, kapama ve varolan dosya üzerinde CRUD işlemleri yapabilirsiniz.

# Dosya açma
# Adı => new_file.txt
# Mode => yazılabilir
# Encoding => utf-8
# Yukarıdaki özelliklere sahip bir dosya yaratın

# file = open('new_file.txt', 'w', encoding='utf-8')
# file.write('Full Name: Burak Yılmaz\nOccupation: Dreamer\n')
#
# Yukarıda yaratılan dosyanın üzerine yeni bir kayıt eklemesi yapın
# Eklenecek kayıt => Programing Language: Python\n
#
# file = open('new_file.txt', 'a', encoding='utf-8')
# file.write('Programing Language: Python\n')
# file = open('new_file.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()


# region Task - 1

# exam_grades.txt dosyasını yaratın

def create_exam_grades() -> None:
    file = open('exam_grades.txt', 'w', encoding='utf-8')
    file.close()

# endregion


# region Task - 2

# Kullanıcıdan first name, last name, midterm, final, homework bilgilerini alarak exam_grades.txt dosyasına yazalım

# Burak Yılmaz: 30, 30, 30

def take_information(first_name: str, last_name: str, midterm: float, final: float, homework: float):
    with open('exam_grades.txt', 'a', encoding='utf-8') as file:
        file.write(f'{first_name} {last_name}: {midterm}, {final}, {homework}\n')

# endregion


# region Task - 3

# Harf notu hesaplayan fonksiyon yaratalım

def calculate_grade(read_row: str):
    cut = read_row.split(':')
    slashed = cut[1].strip()
    result = 0
    for grades in slashed.split(','):
        result += float(grades)
    grade = result/3
    print(grade)

calculate_grade('Burak Yılmaz:30,3,3')



# endregion
