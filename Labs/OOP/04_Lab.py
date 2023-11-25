
# Method Overriding
# Ata sınıflarda bulunan methodların alt sınıflarda ezilerek onlara yeni yetenekler ya da işler kazandırılmasına yahut ezilen methodun yeteneğine ek iş kazandırılması method overriding diyoruz

from enum import Enum
from socket import gethostname, gethostbyname
from datetime import datetime
from uuid import uuid4


# Bu çalışmada category ve product olmak üzere iki tane entity yani varlığımız var


# class Status(Enum):
#     Active = 1
#     Modified = 2
#     Passive = 3
#
#
# class BaseEntity:
#     def __init__(self, name: str, description: str):
#         self.id = str(uuid4())
#         self.status = Status.Active.name
#         self.created_date = datetime.now()
#         self.created_ip_address = gethostbyname(gethostname())
#         self.created_machine_name = gethostname()
#         self.name = name
#         self.description = description
#
#     def show_info(self):
#         print(f'Id: {self.id}\n'
#               f'Name: {self.name}\n'
#               f'Description: {self.description}')
#
#
# class Category(BaseEntity):
#     pass
#
#
# class Product(BaseEntity):
#     def __init__(self, name: str, description: str, price: float, stock: float):
#         super().__init__(name, description)
#         self.stock = stock
#         self.price = price
#
#     def show_info(self):
#         super().show_info()
#         print(f'Stock: {self.stock}\n'
#               f'Price: {self.price}')
#
#
# c1 = Category('asd', 'asdasd')
# c1.show_info()
# p1 = Product('qwe', 'qwe', 2.5, 3.4)
# p1.show_info()



# BasePhone adında bir ata sınıf oluşturalım. phone_id, brand, model, price attributeleri olsun
# BasePhone içerisinde show_info(), phone_ring_sound() fonksiyonları olsun. phone_ring_sound() fonksiyonu string olarak 'genel telefon sesi' değerini retun etsin
# Samsung adında bir sınıf oluşturalım. operating_system attribute olsun. phone_ring_sound() 'samsung telefon sesi' retrun etsin.
# Iphone => adında bir sınıf oluşturalım. camera attribute olsun. phone_ring_sound() 'iphone telefon sesi' retrun etsin.
# Nokia => anten attribute olsun. phone_ring_sound() 'nokia telefon sesi' return etsin

#
# class BasePhone:
#     def __init__(self, brand: str, model: str, price: str):
#         self.phone_id = str(uuid4())
#         self.brand = brand
#         self.model = model
#         self.price = price
#
#     def phone_ring_sound(self):
#         return 'genel telefon sesi'
#
#     def show_info(self):
#         print(f'Id: {self.phone_id}\n'
#               f'Brand: {self.brand}\n'
#               f'Model: {self.model}\n'
#               f'Price: {self.price}\n'
#               f'Phone Ring: {self.phone_ring_sound()}')
#
#
# class Samsung(BasePhone):
#     def __init__(self, brand: str, model: str, price: float):
#         super().__init__(brand, model, price)
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.operating_system = 'Android'
#
#     def phone_ring_sound(self):
#         return 'samsung telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Operating System: {self.operating_system}')
#
#
# class Iphone(BasePhone):
#     def __init__(self, brand: str, model: str, price: float):
#         super().__init__(brand, model, price)
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.camera = '20mp'
#
#     def phone_ring_sound(self):
#         return 'iphone telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Camera: {self.camera}')
#
#
# class Nokia(BasePhone):
#     def __init__(self, brand: str, model: str, price: float):
#         super().__init__(brand, model, price)
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.anten = 'Var'
#
#     def phone_ring_sound(self):
#         return 'nokia telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Anten: {self.anten}')
#
#
# samsung = Samsung('samsung', 's20', 2500)
# iphone = Iphone('Iphone', '15', 3000)
# nokia = Nokia('Nokia', 'CD', 500)
# samsung.show_info()
# iphone.show_info()
# nokia.show_info()



# BaseBill sınıfımız var. bill_name, value_add_task, amount attribute. calculate_bill ve create_log fonksiyonlarımız olacak.
# loglar bill_info txt dosyasında tutulacak. bill_name ve total amountu yazdırmanız yeterli.
# water_bill, electricity_bill, natural_gas_bill sınıflarımız olacak.
# su faturasının mill diye bir özelliği olacak.
# elektrikte ise kw özelliği olacak.
# doğal gaz ise m3 özelliği olacak.


class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount

    def calculate_bill(self):
        return self.value_add_task * self.amount

    def create_log(self):
        with open('bill_info.txt', 'a') as file:
            file.write(f'Bill Name: {self.bill_name} ||'
                       f'Total Amount: {self.calculate_bill()} ||'
                       f'Create Date: {datetime.now()}\n')


class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill

    def calculate_bill(self):
        return super().calculate_bill() * self.mill



class ElectricityBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw

    def calculate_bill(self):
        return super().calculate_bill() * self.kw


class NaturalGasBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3

    def calculate_bill(self):
        return super().calculate_bill() * self.m3


water_bill = WaterBill('Water Bill 1', 5, 10, 2)
water_bill.create_log()
electricity_bill = ElectricityBill('Electricity Bill 1', 2, 10, 4)
electricity_bill.create_log()
natural_gas_bill = NaturalGasBill('Natural Gas Bill 1', 10, 10, 4)
natural_gas_bill.create_log()
