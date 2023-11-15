

# Değişken?
# Algoritma konusunu incelerken değişkenleri kutulara benzetmiştik. Kullanıcıdan gelen bilgileri içerlerine depoladığımızdan bahsetmiştik.
# Saklayacağımız değerin tipine göre değişkenler kullanıyoruz. Yani bu cümleden şunu anlamalıyız. Değişkenlerin tipleri vardır.
# Diğer programlama dillerinde değişken tanımlama yaparken ilk önce değişkenin tipini sonra adını ve tutacağı değeri yazarız.
# Örneğin:
# int x = 5
# string user_name = 'Burak Yılmaz'
# double pi = 3.14

# Python'da değişken tanımlama
# Python'da değişken tanımlarken diğer programlama dillerindeki gibi herhangi bir tip belirtmiyoruz. İçerisine attığımız değerin tipine otomatik olarak bürünüyor.
# x = 5
# print(type(x))
# x = 'Mike Tyson'
# print(type(x))


# Kullanıcıdan 2 adet sayı alalım. 4 İşlem yapalım

# x = int(input('Lütfen bir tam sayı giriniz:'))
# islem = input('Lütfen yapmak istediğiniz işlemi belirtin:')
# y = int(input('Lütfen bir tam sayı giriniz:'))
#
# if islem == '+':
#     sonuc = x + y
#     print(f'Toplam: {sonuc}')
# elif islem == '-':
#     sonuc = x - y
#     print('Çıkarma: {}'.format(sonuc))
# elif islem == '*':
#     sonuc = x * y
#     print('Çarpma:', sonuc)
# elif y != 0 and islem == '/':
#     sonuc = x / y
#     print(sonuc)
# else:
#     print('+, -, * ya da / işlemi yapabilirsiniz. İkinic sayı 0 olamaz')#


# Kullanıcıdan alınan kenar bilgisine göre bir karenin alanını ve çevresini hesaplayan uygulamayı geliştiriniz.

# x = int(input('Lütfen karenin kenar uzunluğunu giriniz:'))
# alan = x * x
# cevre = x * 4
# print(f'Karenin alanı: {alan}')
# print(f'Karenin çevresi: {cevre}')


# Kullanıcıdan alınan kısa ve uzun kenar bilgisine göre dikdörtgenin alan ve çevresini hesaplayan uygulamayı yazınız.

# kisa_kenar = int(input('Lütfen dikdörtgenin kısa kenar uzunluğunu giriniz: '))
# uzun_kenar = int(input('Lütfen dikdörtgenin uzun kenar uzunluğunu giriniz: '))
# print(f'Dikdörtgenin alanı: {kisa_kenar * uzun_kenar}')
# print(f'Dikdörtgenin çevresi: {2 * (kisa_kenar + uzun_kenar)}')


# Kullanıcıdan üçgenin taban ve yükseklik değerlerini alalım ve alanını hesaplayalım.

# yukseklik = int(input('Lütfen üçgenin yüksekliğini giriniz: '))
# taban = int(input('Lütfen üçgenin taban uzunluğunu giriniz: '))
# print(f'alan: {yukseklik * taban / 2}')