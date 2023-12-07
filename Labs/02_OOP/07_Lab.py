
# Dünyanın farklı lokasyonlarından kahve çekirdeği ithal edeceğiz.
# Lakin kahve çekirdeklerinin lezzeti ve kalitesi açısından hasat zamanları gözönünde bulundurularak ithal edilmesi gerek
# 4-7 arasın Columbia'dan
# 8-11 arasında Sumatra
# 1 ya da 2 ya da 12 ay SouthAfrica
# 3 ayda hasat olmadığı için ithal gerçekleşmeyecek

from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def ship_from(self): pass


class SumatraService(BaseService):
    def ship_from(self):
        return 'from Sumatra Island'


class ColumbiaService(BaseService):
    def ship_from(self):
        return 'from Columbia'


class SouthAfricaService(BaseService):
    def ship_from(self):
        return 'from South Africa'


class DefaultService(BaseService):
    def ship_from(self):
        return 'shipment not avaliable'


# Creational Desing Pattern grubuna içerisinde olan factory desing pattern önerği var aşağıda

class Shipment:
    @staticmethod
    def shipment_method(month) -> BaseService:
        if 4 <= month <= 7:
            return ColumbiaService()
        elif 8 <= month <= 11:
            return SumatraService()
        else:
            if month == 1 or month == 2 or month == 12:
                return SouthAfricaService()
            else:
                return DefaultService()


def main():
    for month in range(1, 13):
        product_shipment = Shipment.shipment_method(month)
        print(f'Coffee beans shipment {product_shipment.ship_from()}')


main()
