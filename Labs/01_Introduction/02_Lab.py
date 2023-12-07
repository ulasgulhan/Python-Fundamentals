
# Karar Mekanizmaları
# If-Elif-Else

# region Example 1
# Kullanıcıdan 2 adet sayı alalım ve bu sayılardan büyük olanı ekrana yazalım

# x = int(input('Sayı 1:'))
# y = int(input('Sayı 2:'))
#
# if x > y:
#     print(f'{x} büyüktür..!')
# else:
#     print(f'{y} büyüktür..!')
# endregion

# region Example 2
# Kullanıcıdan alınan sayı çift mi tek mi?

# x = int(input('Bir sayı giriniz:'))
#
# if x % 2 == 0:
#     print(f'{x} çift sayıdır')
# else:
#     print(f'{x} tek sayıdır')

# endregion

# region Example 3
# Kullanıcıdan alınan sayı pozitif mi yoksa negatif mi yoksa nötr mü?

# x = int(input('Bir sayı giriniz:'))
#
# if x == 0:
#     print(f'{x} nötr bir sayıdır')
# elif x < 0:
#     print(f'{x} negatif bir sayıdır')
# else:
#     print(f'{x} pozitif bir sayıdır')

# endregion

# region Example 4
# Kullanıcıdan mevsim bilgisini alalım. Gelen mevsim bilgisine göre ayları ekrana yazalım

# mevsim = input('Mevsim giriniz:').lower()
#
# match mevsim:
#     case 'kış':
#         mesaj ='Aralık-Ocak-Şubat'
#     case 'ilkbahar':
#         mesaj = 'Mart-Nisan-Mayıs'
#     case 'yaz':
#         mesaj = 'Haziran-Temmuz-Ağustos'
#     case 'sonbahar':
#         mesaj = 'Eylül-Ekim-Kasım'
#     case _:
#         mesaj = 'Böyel bir mevsim bulunamamaktadır'
#
# print(mesaj)

# endregion

# region Example 5
# Kullanıcıdan alınan araç türü ve hız bilgisine göre aracın cezalı olup olmadığını söyleyen uygulamayı yazınız

# arac = input('Aracınızı giriniz:')
# hiz = int(input('Hızınızı giriniz:'))
#
# if arac == 'otomobil' or arac == 'motor' or arac == 'kamyon':
#     if arac == 'otomobil' and hiz > 60:
#         print('Cezalı')
#     elif arac == 'motor' and hiz > 60:
#         print('Cezalı')
#     elif arac == 'kamyon' and hiz > 30:
#         print('Cezalı')
#     else:
#         print('Cezalı değil')
# else:
#     print('Araç türü hatalı')

# endregion

# region Example 6
# Kullanıcıdan alınan araç türü ve hız bilgisine göre aracın cezalı olup olmadığını söyleyen uygulamayı yazınız versiyon 2

# arac = input('Aracınızı giriniz:')
# hiz = int(input('Hızınızı giriniz:'))
#
# if hiz > 0:
#     if arac == 'otomobil':
#         if hiz >= 60:
#             print('Cezalısın')
#         else:
#             print('Ceza yok')
#     elif arac == 'motor':
#         if hiz >= 60:
#             print('Cezalısın')
#         else:
#             print('Ceza yok')
#     elif arac == 'kamyon':
#         if hiz >= 40:
#             print('Cezalısın')
#         else:
#             print('Ceza yok')
#     else:
#         print('Lütfen doğru araç türü giriniz')
# else:
#     print('Hız bilgisi negatif olamaz')

# endregion

# region Example 7
# Kullanıcıdan tam adın
# endregion
