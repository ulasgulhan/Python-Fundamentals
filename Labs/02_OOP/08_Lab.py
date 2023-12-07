# BaseBill sınıfımız var. bill_name, value_add_task, amount attribute. calculate_bill ve create_log fonksiyonlarımız olacak.
# loglar bill_info txt dosyasında tutulacak. bill_name ve total amountu yazdırmanız yeterli.
# water_bill, electricity_bill, natural_gas_bill sınıflarımız olacak.
# su faturasının mill diye bir özelliği olacak.
# elektrikte ise kw özelliği olacak.
# doğal gaz ise m3 özelliği olacak.
# Soyutlamayla beraber

from abc import ABC, abstractmethod
from datetime import datetime


class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount


class ElectricityBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw


class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill


class NaturalGasBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3


class BaseService(ABC):
    @abstractmethod
    def calculate_bill(self, bill: BaseBill) -> float: pass

    def create_log(self, bill: BaseBill, result: float):
        with open('abstract_bill_info.txt', 'a') as file:
            file.write(f'Bill Name: {bill.bill_name} ||'
                       f'Total Amount: {result} ||'
                       f'Create Date: {datetime.now()}\n')


class WaterBillService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.value_add_task * bill.amount * bill.mill


class ElectricBillService(BaseService):
    def calculate_bill(self, bill: ElectricityBill) -> float:
        return bill.value_add_task * bill.amount * bill.kw


class GasBillService(BaseService):
    def calculate_bill(self, bill: NaturalGasBill) -> float:
        return bill.value_add_task * bill.amount * bill.m3


water_bill = WaterBill('ISKI', 12.3, 34.5, 56.7)
electric_bill = ElectricityBill('Elektrik', 16.7, 45, 13.3)
gas_bill = NaturalGasBill('Gas', 10, 12.5, 22.4)

service = WaterBillService()
service2 = ElectricBillService()
service3 = GasBillService()

result = service.calculate_bill(water_bill)
result2 = service2.calculate_bill(electric_bill)
result3 = service3.calculate_bill(gas_bill)

service.create_log(water_bill, result)
service2.create_log(electric_bill, result2)
service3.create_log(gas_bill, result3)
