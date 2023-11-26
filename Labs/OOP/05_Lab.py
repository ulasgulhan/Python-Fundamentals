
# Encapsulation (Veri Gizleme)
# Bir sınıfın her hangi bir üyesini encapsulation ettiğimiz zaman ilgili üyeye alt sınıflardan erişimini engellemiş oluruz. Bir başka değişle ilgili sınıf üyesine erişimi kapatmış oluyoruz. Bu bağlamda erişemediğimiz için üzerine değer yazamıyoruz. Lakin belirli şartlar doğrultusunda bu erişimi dolaylı yollar ile yapabiliyoruz.


from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.__id = ''
        self.__created_date = ''
        self.__created_computer_name = ''
        self.__created_ip_address = ''
        self.__status = ''

    def set_values_private_attribute(self):
        self.__id = uuid4()
        self.__created_date = datetime.now()
        self.__created_computer_name = gethostname()
        self.__created_ip_address = gethostbyname(gethostname())
        self.__status = Status.Active.name

    def show_info(self):
        return self.__dict__


class Product(BaseEntity):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = 0
        self.__stock = 0

    def set_values_product_attribute(self, price, stock):
        super().set_values_private_attribute()
        if price > 0 and stock > 0:
            self.__price = price
            self.__stock = stock
            print('Product has been created')
            pprint(self.__dict__)
        else:
            print('Invalid input..!\nProduct stock and price can not negative or zero..!')


p1 = Product('Boxing Gloves', 'Best boxing gloves')
p1.set_values_product_attribute(12, 5)
