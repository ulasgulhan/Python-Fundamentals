
# Python programlama dilinde bir nesne yaratmak için "class" anahtar sözcüğünü kullanıyoruz. Class ile tanımladığımızı yapının içerisinde yaratacağımız ya da ihtiyaç duyduğumuz objenin özelliklerini tanımlıyoruz. Class'ları gerçek dünyadaki prototiplere benzetilebilir

# Örneğin bir araba nesnesi yaratmak için adım adım ilerleyelim
# Adım 1 ilgili nesnenin sahip olacağı özellikleri barındıran bir class tanımla
# Üretmek istediğimiz aracın özelliklerine sahip bir sınıf tanımlıyoruz.

# class Vehicle:
#     # Attribute (özellikler) tanımladık
#     door_number = 4
#     brand = ''
#     model = ''
#     engine_size = ''
#     torque = ''
#
#
# # Aşağıda, yukarıda yarattığımız class örneklem (instance) alıyoruz.
# x = Vehicle()
# x.brand = 'Mercedes'
# x.model = 'S60'
# x.engine_size = 5.4
# x.torque = 6.7
# x.door_number = 2
#
# print(f'Brand: {x.brand}\n'
#       f'Model: {x.model}\n'
#       f'Engine Size: {x.engine_size}\n'
#       f'Torque: {x.torque}\n'
#       f'Door Number: {x.door_number}')
#
#
# y = Vehicle()
# y.brand = 'Dodge'
# y.model = 'TRX 1500'
# y.engine_size = 'V8 SuperCharge 6.2 Liter'
# y.torque = 4.500
#
# print(f'Brand: {y.brand}\n'
#       f'Model: {y.model}\n'
#       f'Engine Size: {y.engine_size}\n'
#       f'Torque: {y.torque}\n'
#       f'Door Number: {y.door_number}')
#
#
# class Human:
#     height = 0
#     weight = 0
#     eye_color = ''
#     hair_color = ''
#
#
# z = Human()
# z.height = 1.75
# z.weight = 66
# z.eye_color = 'Hazel'
# z.hair_color = 'Black'
#
# print(f'Height: {z.height}\n'
#       f'Weight: {z.weight}\n'
#       f'Eye Color: {z.eye_color}\n'
#       f'Hair Color: {z.hair_color}')


# Bir sınıftan örneklem alınırken (instance) sınıf_adı() kullandık.
# Yukarıdaki örnekte 18, 32 ve 52.satırlara bakabilirsiniz.
# Örneklem alırken sınıfın içerisinde built-in olarak bulunan __init__() fonksiyonunu tetiklemiş oluyoruz.
# Bu fonksiyon diğer programlama dillerinde constructor olarak geçer. Bu fonskyionun görevi ilgili sınıfı başlatmaya (initialize) yarar.

# class Boxer:
#     # Class attribute
#     alias = ''
#
#     def __init__(self, first_name, last_name, age, record):
#         # Object attribute
#         self.adi = first_name
#         self.soyadi = last_name
#         self.yas = age
#         self.rekoru = record
#
#
# boxer_1 = Boxer(first_name='Mike', last_name='Tyson', age=57, record='56-4-1')
#
# print(dir(boxer_1))
# print(dir(Boxer))


# Circle isminde bir sınıf yaratalım
# pi adında bir class attribute olsun
# r adında bir object attribute olsun
# alan ve çevre hesaplama fonksiyonları olsun

# class Circle:
#     pi = 3.14
#
#     def __init__(self, r):
#         self.r = r
#
#     def calculate_area(self):
#         print(f'Area: {self.pi * self.r ** 2}')
#
#     def calculate_perimeter(self, r):
#         print(f'Perimeter: {2 * self.pi * self.r}')
#
#
# radius = float(input('Radius: '))
# c1 = Circle(r=radius)
# c1.calculate_area()
# c1.calculate_perimeter()


# Department adında bir sınıf oluşturalım
# department_name ve employee_count class attribute
# name, age object attribute
# show_information()
# show_employee_count(), her instance alındığında employee_count class attribute bir artırılacak

# class Department:
#     employee_list = []
#     department_name = 'Software Developer'
#     employee_count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Department.employee_list.append(f'Adı: {self.name}, Yaşı: {self.age}, Departmanı: {self.department_name}')
#         Department.employee_count += 1
#
#     def show_information(self):
#         return f'Adı: {self.name} Yaşı: {self.age}'
#
#     def show_employee_count(self):
#         return f'Çalışan sayısı: {Department.employee_count}'
#
#
# while True:
#     x = Department(input('Name: '), int(input('Age: ')))
#     print(x.show_information())
#     print(x.show_employee_count())
#     print(Department.employee_list)


# Software_Developer adında bir sınıf yaratalım
# first_name, last_name object attribute
# knowleadge_language = [] class attribute
# show_info()
# add_new_language() birden fazla dil de ekleyebilsin


# class Software_Developer:
#     knowleadge_language = []
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def show_info(self):
#         return f'Çalışan: {self.first_name} {self.last_name}\nBildiği Diller: {self.knowleadge_language}'
#
#     def add_new_language(self, language):
#         knowleadge = language.split(',')
#         for language in knowleadge:
#             self.knowleadge_language.append(language.lstrip())
#
#
# software_developer = Software_Developer(input('First Name: '), input('Last Name: '))
# software_developer.add_new_language(input('Language: '))
# print(software_developer.show_info())

from random import choice

class Character:
    def __init__(self, name: str, race: str, role: str, level: int, weapon: int, armour: int, hp: int ):
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.level = level
        self.role = role
        self.race = race
        self.name = name

    def attack(self):
        return self.level * self.weapon

    def defend(self):
        return self.level * self.armour

    def dodge(self):
        return (self.level * self.weapon) - (self.level * self.weapon)


def main():
    c1 = Character(name='Kara Murat', race='Turk', role='Raider', level=100, weapon=100, armour=20, hp=100)
    c2 = Character(name='Gostok', race='Bizans', role='Kral', level=50, weapon=20, armour=100, hp=100)

    while True:
        bot_actions = [c2.attack, c2.defend, c2.dodge]

        choice(bot_actions)

        # c1 için aksiyon alınır

        # if else ile kontrol edilir

        # oyuncuların hp'leri kontrol edilecek. Herhangi birinin canı 0 olduğunda oyun duracak