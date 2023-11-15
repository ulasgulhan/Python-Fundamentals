
# Try-Except
# Try-Except bloklarıyla bazı istisnai durumları (exceptions) ele aldığımızı (handling) yapılardır.
# Try bloğu içerisine hata beklediğimiz kodları yazıyoruz. Exception'da ise beklediğimiz hatayı handle ediyoruz.

# Örneğin

# try:
#     bolunen = int(input('Bölünen sayıyı giriniz:'))
#     bolen = int(input('Bölen sayıyı giriniz:'))
#     x = bolunen / bolen
#     print(x)
# except ZeroDivisionError as err:
#     print(f'Bir tam sayı sıfıra bölünemez\n{err}')
# else:
#     print('Exception çalışmazsa çalışır')
# finally:
#     print(f'Ne olursa olsun çalışır.')


try:
    age = int(input('Please type into your age: '))
    print(age)
except ValueError as err:
    print(f'Invalid input!\n{err}')