
# Custom Function
# Bu zamana kadar python içerisinde built-in fonksiyonlardan faydalandık. Örneğin range(), print(), randit() vb. Bu fonksiyonlar onların üzerlerine atanmış işlerin bıkmadan usanmadan yerine getirir. Aldıkları argümanlara göre üzerine yüklenen işleri değişik versiyonlarını execute ederler. Örneğin range() fonksiyonu aldığı argümanların sayısına göre 3 farklı iş yapmaktadır.

# Fonksiyon tanımlarken

# def function_name():
    # Fonksiyonun gövdesi
    # Burada icra edeceği işlerin bussiness logic çözümleniyor.

# function_name()

# adım 1: fonksiyonumuzu defined ettik

# def greeting_people():
#     print('Hello...')
#
#
# # adım 2: yukarıda yarattığımız fonksiyonu call ediyoruz.

# greeting_people()
# greeting_people()
# greeting_people()

# Artık bu fonksiyonu istediğim yerde istediğim kadar call edebilirim.


# def greeting_person(full_name: str) -> None:
#     """
#     This funcion greeting people
#     :param full_name: This argumant type is str
#     :return: None
#     """
#     print(f'{full_name} salve..!')
#
#
# greeting_person('Ulaş Gülhan')


# Kullanıcıdan tam adını alalım.
# isim.soyisim@bilgeadam.com mail adresini oluşturalım
# Bir kişinin birden fazla ismi olabilir. Bu sebepten ötürü ilk adını ve soyadını kullanacağız

# def get_mail(full_name: str) -> None:
#     splited_name = full_name.lower().split(' ')
#     print(f"{splited_name[0]}.{splited_name[-1]}@bilgeadam.com")
#
#
# name = input('Tam adınızı giriniz: ')
# get_mail(name)


# Kullanıcıdan alınan sayı çift mi tek mi?

# def is_odd(integer: int) -> None:
#     if integer % 2 == 0:
#         print('Sayı çiftir')
#     else:
#         print('Sayı tektir')
#
#
# number = int(input('Bir sayı giriniz: '))
# is_odd(number)


# Kullanıcıdan alınan değerin faktöriyelini hesaplayın

# def faktoriyel(integer: int) -> None:
#     if integer < 0:
#         print('Sıfırdan küçük sayıların faktöriyeli hesaplanmaz')
#     else:
#         result = 1
#         if integer == 0 or integer == 1:
#             print(f'Sonuç: {result}')
#         else:
#             for i in range(integer, 1, -1):
#                 sonuc = result * i
#             print(f'Sonuç: {result}')
#
#
# number = int(input('Bir sayı giriniz: '))
# faktoriyel(number)


