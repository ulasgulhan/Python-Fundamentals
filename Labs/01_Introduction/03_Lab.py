
# While Loop
# Tekrarlı işlemleri yaptırmak istediğimizde tercih ettğimiz mekanizmadır.
# While loop bir sayaç ile birlikte karar mekanizması içermektedir. Sayaç arttırılarak ya da azaltılarak şartın sağlandığı sürece döngü dönmeye devam eder.

# region Example 1
# 0 ile 100 arasındaki sayıları ekrana yazdıralım

# counter = 0
#
# while counter <= 100:
#     print(counter)
#     counter += 1 # counter = counter + 1

# endregion

# region Example 2
# 1 ile 100 arasındaki sayıları toplayalım ve nihai sonucu ekrana yazdıralım

# counter = 1
# toplam = 0
#
# while counter <= 100:
#     toplam += counter
#     counter += 1
#
# print(f'Sonuc: {toplam}')

# endregion

# region Example 3
# 0 ile 100 arasında kaç tane çift kaç tane tek sayı var bulalım ve ekrana yazdıralım

# tek = 0
# cift = 0
# counter = 100
#
# while counter >= 0:
#     if counter % 2 == 0:
#         cift += 1
#     else:
#         tek += 1
#     counter -= 1
#
# print(f'Tek sayı: {tek}\nÇift sayı {cift}')

# endregion

# region Example 4
# 0 ile 100 arasındaki çift ve tek sayıların toplamları

# tek = 0
# cift = 0
# counter = 0
#
# while counter <= 100:
#     if counter % 2 == 0:
#         cift += counter
#     else:
#         tek += counter
#     counter += 1
#
# print(f'Tek sayı toplamı: {tek}\nÇift sayı toplamı: {cift}')

# endregion

# region Example 5
# Kullanıcıdan işlem türü alalım (e, + , -, vb) alınan bu işlem türüne göre ilgili işlemi yapıp sonucunu ekrana yazalım.

# while True:
#     process = input('Yapmak istediğiniz işlemi belirtin: ')
#
#     match process:
#         case 'e':
#             print('Uygulama kapatılıyor...')
#             break
#         case '+' | '-' | '*' | '/':
#             a = int(input('işlem yapmak istediğiniz sayıyı giriniz: '))
#             b = int(input('işlem yapmak istediğiniz 2.sayıyı giriniz: '))
#             match process:
#                 case '+':
#                     print(f'Sonuc: {a + b}')
#                 case '-':
#                     print(f'Sonuc: {a - b}')
#                 case '/':
#                     if b == 0:
#                         print('Bir sayı sıfıra bölünemez')
#                     else:
#                         print(f'Sonuc: {a / b}')
#                 case'*':
#                     print(f'Sonuc: {a * b}')
#                 case _:
#                     print('Hatalı işlem seçimi')
#         case _:
#             print('Hatalı giriş')

# endregion

# region Example 6
# Kullanıcıdan alınan sayı asal mı değil mi?

# sayi = int(input('Lütfen bir sayı giriniz: '))
#
# if sayi <= 0:
#     print('Sıfır ve negatif sayılar asal değildir')
# else:
#     is_prime = True
#     if sayi == 1:
#         is_prime = False
#
#     counter = 2
#     while counter < sayi:
#         if sayi % counter == 0:
#             is_prime = False
#             break
#         else:
#             counter += 1
#     if is_prime:
#         print(f'{sayi} asal sayıdır')
#     else:
#         print(f'{sayi} asal değildir.')

# endregion