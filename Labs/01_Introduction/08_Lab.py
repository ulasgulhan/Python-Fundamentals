
# Dictionary (Sözlük)
# Sözlük objesi, list, tuple gibi geçici olarak verileri depolayabildiğimiz başka bir yapıdır.
# Sözlük 'key' & 'value' mantığında çalışırlar
# Anahtarlar herhangi bir değere erişmek için kullanılır.

# my_dict = {
#     'Full Name': 'Burak Yılmaz',
#     'Age': 34,
#     'Sports': ['Boxing', 'UFC', 'Wrestling', 'NBA', 'NFL'],
#     'User_names': ('beast', 'savage', 'crayz bear'),
#     'Favorite_books': {
#         'War History': 'Cambridge War History',
#         'Scientific': {
#             'Karl Poper': 'The Logic of Scientfic Discovry'
#         }
#     }
# }

# release_year_movie = {
#     'Fight Club': 1999,
#     'Matrix': 1999,
#     'Interstaller': 2014,
#     'Inception': 2010,
#     'Dune': 2021
# }
# Herhangi bir value ekrana basın
# Yol 1
# print(f'Interstaller Release Year: {release_year_movie.get("Interstaller")}')
# # Yol 2
# print(f'Interstaller Release Year: {release_year_movie["Interstaller"]}')

# Sözlüğün tüm anahtarlarını ekrana yazdırın

# for key in release_year_movie.keys():
#     print(key)
#
# # Sözlüğün tüm değerlerini ekrana yazdırın
#
# print([i for i in release_year_movie.values()])
#
# # Sözlüğün anahtar ve değerlerini ekrana yazdırın
#
# print(release_year_movie.items())

# products = [
#     {'name': 'Everlast Pro Boxing Gloves', 'price': 245},
#     {'name': 'Everlast Traing Gloves', 'price': 200},
#     {'name': 'Everlast Havy Bag', 'price': 445},
#     {'name': 'Iphone 15 Pro Max', 'price': 80000},
#     {'name': 'Samsung G23 Ultra', 'price': 65000},
#     {'name': 'Lenevo x1 Carbon', 'price': 49000}
# ]

# products listesindeki bütün toplayarak ekrana basın

# total_price = 0
# for product in products:
#     total_price += product.get('price')
#
# print(f'Total: {total_price}')

# products listesindeki ürün fiyatlarını 30000'den büyük büyük olan ürünlerin isimlerini ekrana yazdırın

# for product in products:
#     if product['price'] > 30000:
#         print(product['name'])

# ürün adı içerisinde Everlast geçen ve fiyat aralığı 240 ile 500 arasında olan ürünleri listeleyiniz.

# for product in products:
#     if 'Everlast' in product['name'] and 240 <= product['price'] <= 500:
#         print(product['name'])



# CRUD Operasyonları (Create - Read - Update - Delete)

# Boş bir students sözlüğü oluşturalım. Sözlüğün structure aşağıda gösterilmektedir

# students = {
#     'student_id': {
#         'first_name': 'fsfds',
#         'last_name': 'fasa',
#         'phone': 'fasdfasd'
#     }
# }

# Kullanıcı yapacağı işi seçebilmeli. Yani exit, create, read, update, delete olarak işlemleri seçmelidir
# id'ler uuid4() ile tanımlansın

import uuid

students = {}

while True:
    print('User Guide\n'
          '===========\n'
          'create\n'
          'read\n'
          'update\n'
          'delete\n'
          'exit\n')
    process = input('Yapmak istediğiniz işlem nedir? ').lower()
    if process == 'exit':
        print('Çıkış yapılıyor...')
        break
    elif process == 'create':
        student_id = str(uuid.uuid4())
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        phone = input('Phone Number: ')
        students[student_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone
        }
        print('Kullanıcı başarılı bir şekilde oluşturuldu.')
    elif process == 'read':
        for i in students:
            print(f'{i}: {students[i]}')
    elif process == 'update':
        key_1 = input('Güncellemek istediğiniz kişinin idsi: ')
        if key_1 in students:
            key_2 = input('Güncellemek istediğiniz kısım: ').replace(' ', '_')
            if key_2 in students[key_1]:
                students[key_1][key_2] = input('Yeni input: ') # student.update({student_id: {'first_name': first_name, ....}) fonksiyonu da var
            else:
                print('Böyle bir kısım yok')
        else:
            print('Böyle bir id yok')
    elif process == 'delete':
        delete = input('Silmek istediğiniz öğrencinin idsi: ')
        if delete in students:
            del students[delete]
            print('Kullanıcı başarıyla silinmiştir.')
        else:
            print('Böyle bir id yok')
    else:
        print('Böyle bir işlem türü bulunmamaktadır.')
