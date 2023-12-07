
# Kalıtım (Inheritance)
# Biyolojide olduğu gibi bizler ebeveynlerimizden gen aktarımı vasıtasıyla özellikler kazanabiliyorsak yazılımda da ata sınıflardan alt sınıflar inheritance mantığı ile özellikler kazanmaktadır.

# class Human:
#     def __init__(self, height: float, weight: float, full_name: str):
#         self.height = height
#         self.weight = weight
#         self.full_name = full_name
#
#     def show_information(self):
#         print(f'Full Name: {self.full_name}\n'
#               f'Weight: {self.weight}\n'
#               f'Height: {self.height}')
#
#
# class Knight(Human):
#     pass
#
#
# k1 = Knight(1.75, 75, 'Ulaş Gülhan')
# k1.show_information()


# Employee CRUD operasyonları yapacağız
# BaseEntity => Projelerimizdeki tüm entitylere kalıtım veren ata sınıftır. Özellikle log işlemi için gerekli olan attributeleri bünyesinde barındırır. Bunun yanında projedeki entitylerin ortak özellikleri de bu sınıf içerisine yazılır.


from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum



# region Ben Yaptım

# database = {}
#
# class Status(Enum):
#     Active = 1
#     Modified = 2
#     Passive = 3
#
#
# class BaseEntity:
#     def __init__(self, first_name: str, last_name: str, department: str):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.department = department
#         self.id = uuid4()
#         self.status = Status.Active.name
#         self.created_date = datetime.now()
#         self.created_ip_address = gethostbyname(gethostname())
#         self.created_machine_name = gethostname()
#
#
# class Employee(BaseEntity):
#     pass
#
#
# class Employee_Service:
#     def create(self, employee: Employee):
#         if employee.first_name.strip() == '' or employee.last_name.strip() == '' or employee.department.strip() == '':
#             print('Inputs cannot be empty..!')
#         else:
#             database[str(employee.id)] = {
#                 'first_name': employee.first_name,
#                 'last_name': employee.last_name,
#                 'department': employee.department,
#                 'status': employee.status
#             }
#             print('Employee has been created..!')
#
#     def update(self, id: str, first_name: str, last_name: str, department: str):
#         current_employee = self.get_by_id(id)
#         if first_name.strip() == '' or last_name.strip() == '' or department.strip() == '':
#             print('Inputs cannot be empty')
#         else:
#             current_employee.update({
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'department': department
#             })
#
#     def delete(self, id):
#         current_employee = self.get_by_id(id)
#         if current_employee != {}:
#             del database[id]
#             print('Employee has been deleted')
#         else:
#             print('Employee cannot deleted')
#
#     def get_all(self):
#         print(database)
#
#     def get_by_id(self, id):
#         for i in database.keys():
#             if i == id:
#                 return database[id]
#
#     def get_active(self):
#         for id in database:
#             for status in database[id].values():
#                 if status == 'Active':
#                     print(database[id])
#
#
#     def get_by_full_name(self, name):
#         for id in database:
#             for names in database[id].values():
#                 if names == name:
#                     print(database[id])
#
#
#
# def main():
#     employee_service = Employee_Service()
#     while True:
#         process = input('Process: ').lower()
#         match process:
#             case 'exit':
#                 print('Application has been closing')
#             case 'create':
#                 first_name = input('First Name: ')
#                 last_name = input('Last Name: ')
#                 department = input('Department: ')
#                 employee = Employee(first_name, last_name, department)
#                 employee_service.create(employee)
#             case 'update':
#                 id = input('Id: ')
#                 first_name = input('First Name: ')
#                 last_name = input('Last Name: ')
#                 department = input('Department: ')
#                 employee_service.update(id, first_name, last_name, department)
#             case 'delete':
#                 employee_service.delete(input('Id: '))
#             case 'get all':
#                 employee_service.get_all()
#             case 'get by id':
#                 print(employee_service.get_by_id(input('Id: ')))
#             case 'get by full name':
#                 employee_service.get_by_full_name(input('Name: '))
#             case 'get active':
#                 employee_service.get_active()
#             case _:
#                 print('Error')
#
#
# main()

# endregion



# region Hocam yaptı

db = []

class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self, first_name: str, last_name: str, department: str):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.id = str(uuid4())
        self.status = Status.Active.name
        self.created_date = datetime.now()
        self.created_ip_address = gethostbyname(gethostname())
        self.created_machine_name = gethostname()


class Employee(BaseEntity):
    pass


class Employee_Service:
    def create(self, employee: Employee):
        db.append(employee)
        print(f'{employee.first_name} {employee.last_name} has been created..!')

    def update(self, id: str, first_name: str, last_name: str, department: str):
        employee = self.get_by_id(id)

        employee.status = 'Modified'
        employee.first_name = first_name
        employee.last_name = last_name
        employee.department = department

    def delete(self, id: str):
        employee = self.get_by_id(id)
        employee.status = 'Passive'

    def get_all(self):
        pass

    def get_by_id(self, id: str) -> Employee:
        for employee in db:
            if employee.id == id:
                return employee

    def get_active(self):
        for employee in db:
            if employee.status == 'Active' or employee.status == 'Modified':
                print(employee.__dict__)

    def get_by_full_name(self, full_name: str):
        for employee in db:
            if f'{employee.first_name} {employee.last_name}'.lower().__contains__(full_name):
                print(employee.__dict__)


def main():

    service = Employee_Service()

    while True:
        process = input('Type a process: ')

        match process:
            case 'e':
                break
            case 'create':
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                department = input('Department: ')
                employee = Employee(first_name, last_name, department)
                service.create(employee)
                service.get_active()
            case 'update':
                id = input('Id: ')
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                department = input('Department: ')
                service.update(id, first_name, last_name, department)
                service.get_active()
            case 'delete':
                id = input('Id: ')
                service.delete(id)
                service.get_active()
            case 'list':
                service.get_active()
            case 'get by full name':
                full_name = input('Full Name: ').lower()
                service.get_by_full_name(full_name)
            case 'get by id':
                id = input('Id: ')
                service.get_by_id(id)
            case _:
                pass


main()

# endregion
