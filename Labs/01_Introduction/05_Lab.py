
# For Loop
# For loop geçmeden önce incelememiz gereken bir kaç tane yardımcı operatör ve fonskiyon bulunmaktadır. Bunlar "in" & "not in" ayrıca range() fonksiyonudur.

# in & not in operatörleri
# name = 'Mike Tyson'

# in
# print('b' in name)   Result => False
# print('m' in name)   Result => False
# print('M' in name)   Result => True


# not in
# print('M' not in name)   Result => False
# print('m' not in name)   Result => True


# range() fonksiyon for ile sıklıkla kullanılan bir yapıdır. Range bize içerisine verilen argümanlara göre bir sayı listesi döner.
# range() fonksiyonu bir tane argüman alırsa. Başlangıç değerini default olarak sıfır kabul eder. Bizim verdiğimiz değeri ise bitiş değeri olarak kabul eder.
# for i in range(10):
#     print(i)


# range() fonksiyonum 2 argüman alırsa, aldığı birinci argümanı başlanıç ikinci argümanı ise bitiş kabul eder.
# for i in range(6, 10):
#     print(i)


# range() fonksiyonu 3 argüman (parametre) alırsa, 1.argüman başlangıç, 2.argüman bitiş, 3.argüman ise adım miktarıdır.
# for i in range(10, 100, 5):
#     print(i)


# region Example 1
# 0 - 100 arasındaki çift ve tek sayıların toplamını ekrana yazdırın.
# cift = 0
# tek = 0
# for i in range(101):
#     if i % 2 == 0:
#         cift += i
#     else:
#         tek +=i
# print(f'Tek sayıların toplamı {tek}\nÇift sayıların toplamı {cift}')

# endregion

# region Example 2
# Kullanıcıdan başlangıç, bitiş ve artış miktarlarını alalım. Adım adım uğranılan sayıarın karelerini alarak ekrana yazalım. Lakin şu formatta yazdırılacak:
# 1. adımda ==> sonuç

# basla = int(input('Başlangıç değerini giriniz: '))
# bitis = int(input('Bitiş değerini giriniz: '))
# artis = int(input('Artış değerini giriniz: '))
# counter = 0
# for i in range(basla, bitis, artis):
#     counter += 1
#     print(f'{counter}.adımda ==> {i * i}')

# endregion


# Nested For Loop
# for i in range(3):
#     print(f'{i}.adım çalışıyor')
#     for j in range(3):
#         print(f'{j}.adım çalışıyor')


# region Example 1
# Çarpım tablosu

# for i in range (1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')
#     print('===============')

# endregion

# region Example 2
# 'x' sembolünü kullanarak içi dolu dikdörtgen yapın 4x6

# for i in range(4):
#     for j in range(6):
#         print('x', end=' ')
#     print(' ')

# endregion

# region Example 3
# Dik üçgen

# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print('X', end=' ')
#     print(' ')
#
# endregion