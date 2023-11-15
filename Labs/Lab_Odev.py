# from math import sqrt

# region Example 1
# Linear bir doğrunun real köklerini hesaplayalım

# a = int(input('Bir sayı giriniz:'))
# b = int(input('Bir sayı giriniz:'))
# c = int(input('Bir sayı giriniz:'))
# delta = b ** 2 - 4 * a * c
#
# if delta > 0:
#     x1 = -b - sqrt(delta) / 2 * a
#     x2 = +b - sqrt(delta) / 2 * a
#     print(f'{x1} ve {x2} real kökleridir')
# elif delta == 0:
#     x1 = -b - sqrt(delta) / 2 * a
#     print(f'{x1} real köküdür')
# else:
#     print('Real kök bulunmamaktadır')

# endregion

# region Example 2
# Kullanıcıdan alınan 3 tane sayıyı büyüklük olarak karşılaştıralım

# sayi_1 = int(input('Lütfen bir sayı giriniz:'))
# sayi_2 = int(input('Lütfen bir sayı giriniz:'))
# sayi_3 = int(input('Lütfen bir sayı giriniz:'))
#
# if sayi_1 > sayi_2 and sayi_1 > sayi_3:
#     print(f'{sayi_1} en büyük sayıdır')
# elif sayi_2 > sayi_1 and sayi_2 > sayi_3:
#     print(f'{sayi_2} en büyük sayıdır')
# elif sayi_3 > sayi_1 and sayi_3 > sayi_2:
#     print(f'{sayi_3} en büyük sayıdır')
# else:
#     print('Sayılar birbirine eşittir')

# endregion

# region Example 3
# Kullanıcıdan username, password, boy ve kilo değerlerini alalım. Login işlemi yapalım ve vücut kitle indexini hesaplayalım

# ad = input('Tam adınızı giriniz: ')
# username = input('Kullanıcı adınızı giriniz: ')
# password = input('Parolanızı giriniz: ')
#
# if username == 'rite' and password == '123':
#     print(f'Welcome {ad}')
#     boy = int(input('Santim biçiminde boyunuzu giriniz: '))
#     kilo = float(input('Kilonuzu giriniz: '))
#     vki = kilo / (boy * 0.01)**2
#     if 0 < vki <= 18.5:
#         print(f'{ad} Zayıfsın')
#     elif 18.5 < vki <= 24.9:
#         print(f'{ad} Normal kilo')
#     elif 24.9 < vki <= 29.9:
#         print(f'{ad} Kilolu')
#     elif 29.9 < vki <= 39.9:
#         print(f'{ad} Obez')
#     elif vki > 40:
#         print(f'{ad} Çok Obez')
#     else:
#         print('Bilgilerinizi kontrol ediniz')
# else:
#     print('Hatalı kullanıcı girişi')

# endregion

# region Example 4
# Kullanıcıdan vize, final, ödev notları alıp ortalama hesaplıyoruz. Vize %30, final %60, ödev %10

# vize = float(input('Vize notunuzu giriniz: '))
# final = float(input('Final notunuzu giriniz: '))
# odev = float(input('Ödev notunuzu giriniz: '))
# ortalama = (vize * 0.3) + (final * 0.6) + (odev * 0.1)
#
# if ortalama >= 85:
#     print('AA')
# elif 65 <= ortalama < 85:
#     print('BB')
# elif 45 <= ortalama < 65:
#     print('CC')
# elif 35 <= ortalama < 45:
#     print('DD')
# elif 0 <= ortalama < 35:
#     print('FF')
# else:
#     print('Sınavlara girilemdi')

# endregion

# region Example 5
# Kullanıcıdan ürün bilgisi alıyoruz. Aldığımız ürünün hangi reyonda olduğunu kullanıcıya bildiriyoruz

# urun = input('İstediğiniz ürünü giriniz: ')
#
# match urun:
#     case 'muz' | 'elma' | 'üzüm':
#         print('Meyve reyonu')
#     case 'sabun' | 'şampuan' | 'saç boyası':
#         print('Kişisel bakım reyonu')
#     case 'tablet' | 'bilgisayar' | 'telefon':
#         print('Teknoloji reyonu')
#     case _:
#         print('Ürün bulunmamaktadır')

# endregion

# region Example 6
# Kullanıcıdan satın aldığı kitap sayısını istiyoruz. Bir kitap 5 TL. Satın alınan kitap sayısına göre:
# 20'den azsa %5, 21 ile 50 arasında ise %10, 51 ile 75 arasında ise %15, 76 ile 100 arasında ise %25 indirimç Kullanıcı ne öder?

# kitap = int(input('Kaç adet kitap aldığınızı giriniz: '))
#
# if 0 < kitap <=20:
#     print(f'Alınan kitap sayısı {kitap}\nÖdeyeceğiniz tutar {kitap * 5 * 0.95} TL')
# elif 20 < kitap <= 50:
#     fiyat = kitap * 5 * 0.90
#     print(f'Alınan kitap sayısı {kitap}\nÖdeyeceğiniz tutar {kitap * 5 * 0.90} TL')
# elif 50 < kitap <= 75:
#     fiyat = kitap * 5 * 0.85
#     print(f'Alınan kitap sayısı {kitap}\nÖdeyeceğiniz tutar {kitap * 5 * 0.85} TL')
# elif 75 < kitap <= 100:
#     fiyat = kitap * 5 * 0.75
#     print(f'Alınan kitap sayısı {kitap}\nÖdeyeceğiniz tutar {kitap * 5 * 0.75} TL')
# else:
#     print('O kadar da kitap okuma kral. Ya da hiç kitap almadın')

# endregion

# region Example 7
# Kullanıcıya dikdörtgenin alanını mı yoksa çevresini mi hesaplamak istediğini soralım

# kisa_kenar = float(input('Lütfen kısa kenarı giriniz: '))
# uzun_kenar = float(input('Lütfen uzun kenarı giriniz: '))
# hesaplama = input('Ne hesaplamak istiyorsun "alan" ya da "çevre": ')
#
# match hesaplama:
#     case 'alan':
#         alan = uzun_kenar * kisa_kenar
#         print(f'Dikdörtgenin alanı: {alan}')
#     case 'çevre':
#         cevre = 2 * (uzun_kenar + kisa_kenar)
#         print(f'Dikdörtgenin çevresi: {cevre}')
#     case _:
#         print('Hesaplamayı doğru girmediniz')

# endregion