
# Soyutlama
# OOP yapıları arasında en önemlisidir.
# Üst seviyeli yazılım prensiplerine uymak istiyorsak ilk adım soyutlamadır.
# Tasarım destenleri içerisinde soyutlama neredeyse tüm desenlerde(patterns) kullanılmaktadır.


# Soyutlamaya geçmeden önce öğrenmemiz gereken 1-2 husus bulunmaktadır. Bunlardan 1.si decorator bir diğeri ise meta class yapısıdır



# region Decorator

# Decorator
# Python'da kullanılan keyworddür. Bir fonksiyou bir decorator ile onun varolan yeteneği üzerine bir yetenek daha eklenmesine olanak tanır. Methodlarmızı yoğun kod yazmadan yeni bir yetenek ile extend etmiş oluruz. Python gibi güçlü bir programlama dilinde built-in bulunan bir çok decorator vardır. Tabi ki custom decorator de yazılabilir.


# def uppercase_name(function):
#     def inner_func():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return inner_func()
#
#
# def get_fullname():
#     return 'mike tyson'


# print(uppercase_name(get_fullname))
#
#
# @uppercase_name
# def get_name():
#     return 'burak yılmaz'
#
#
# print(get_name)


# from math import pow, factorial
# from time import sleep, time
#
#
# def calculate_time_execute(func):
#     def inner_func(*args, **kwargs):
#         start_time = time()
#         sleep(10)
#         func(*args, **kwargs)
#         finish_time = time()
#         print(f'=================\n'
#               f'Transaction Name: {func.__name__}\n'
#               f'Start Time: {start_time}\n'
#               f'Finish Time: {finish_time}\n')
#
#     return inner_func
#
#
# @calculate_time_execute
# def us_alma(a: int, b: int):
#     print(f'Sonuç: {pow(a, b)}')
#
#
# @calculate_time_execute
# def faktoriyel_hesaplama(number: int):
#     print(f'Sonuç {factorial(number)}')
#
#
# @calculate_time_execute
# def toplama(x: int, y: int, z: int):
#     print(f'Sonuç: {x + y + z}')
#
#
# us_alma(2, 3)
# faktoriyel_hesaplama(5)
# toplama(2, 3, 5)

# endregion



# region Abstraction Example

from abc import ABC, abstractmethod

class BaseMuzikAleti:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand


class Gitar(BaseMuzikAleti):
    def __init__(self, brand, model, tel):
        super().__init__(brand, model)
        self.tel = tel


class Davul(BaseMuzikAleti):
    def __init__(self, brand, model, kasa):
        super().__init__(brand, model)
        self.kasa = kasa


class Muzisyen:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.caldigi_enstrumanlar = []


# ABC meta sınıfından kalıtım alan BaseServiceimiz ABC sınıfı vasıtasıyla soyut sınıf özelliğine kavuşur.
# Yazdığımız kodlarda üst seviyeli yazılım prensiplerine uymak istiyorsak fonksiyon içeren ata sınıfımızın soyut olması gerekmektedir. Örneğin OCP, LSP, DI, IoC prensiplerine uymak istiyorsak ata sınıflarımız soyut olmalı.

class BaseService(ABC):

    # Abstract bir sınıf içerisinde herhangi bir methodu "@abstractmethod" decoratorü ile işaretlersem bu methodu alt sınıflarda override etmek zorunda kalırım. Bu açıdan düşünürsek alt sınıf ile üst sınıf arasında bir sözleşme yapmış oluruz. "@abstractmethod" işaretlenmiş methodların gövdesi olmaz. Çünkü zaten alt sınıflarda ezip ona bir görev vereceğim yani her halükarda burada vereceğim gövde geçersiz kılınacak. Madem geçersiz kılınacak neden burada görev vereyim ki?
    @abstractmethod
    def call_sound(self) -> str: pass

    # Abstract sınıfı içerisinde normal abstract olmayan methodlarda yazabiliriz. Örnekte görüldüğü gibi bu methodları alt sınıflarda ihtiyaç duyarsak override ediyoruz.
    def hello_everyone(self):
        print('Hi')


class GitarService(BaseService):
    def call_sound(self) -> str:
        return 'Gitar sesi'

    def hello_everyone(self):
        print('Salve')

    # herhangi bir sınıfta kendisine has bir method ihtiyacı olursa onu yazabiliriz. İlla her şeyi ata sınıfa yazmaya gerek yok.
    # staticmethod vs instance method
    @staticmethod
    def harmonize():
        print('Akor edildi')


class DavulService(BaseService):
    def call_sound(self) -> str:
        return 'Davul sesi'


def main():
    gitar_service = GitarService()
    davul_service = DavulService()

    gitar = Gitar('Fender', 'Classical gitar', 'Kaliteli tel')
    davul = Davul('Sevilla', 'Classical', 'Meşe')

    muzisyen = Muzisyen('burak', 'yılmaz')
    muzisyen.caldigi_enstrumanlar.append(gitar)
    muzisyen.caldigi_enstrumanlar.append(davul)

    print(f'Ad: {muzisyen.first_name}\n'
          f'Soyadı: {muzisyen.last_name}\n'
          f'Çaldığı Enstruman Adı: {muzisyen.caldigi_enstrumanlar[0].brand}\n'
          f'Çaldığı Enstruman Model: {muzisyen.caldigi_enstrumanlar[0].model}\n'
          f'Çıkardığı Ses: {gitar_service.call_sound()}\n')

    print(f'Ad: {muzisyen.first_name}\n'
          f'Soyadı: {muzisyen.last_name}\n'
          f'Çaldığı Enstruman Adı: {muzisyen.caldigi_enstrumanlar[0].brand}\n'
          f'Çaldığı Enstruman Model: {muzisyen.caldigi_enstrumanlar[0].model}\n'
          f'Çıkardığı Ses: {davul_service.call_sound()}\n')

    GitarService.harmonize()


main()

# endregion