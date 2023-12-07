
# CRUD (Create - Read - Update - Delete)
# database = {} empty bir dictionary sınıftan bağımsız
# Category adında bir sınıfımız olsun. name, description, object attribute olsun
# Category_Service adında bir sınıfımız olsun. Bu sınıf içerisinde CRUD operasyonlarını yürütürken kullanacağım fonksiyonlarım olacak

from uuid import uuid4

database = {}


class Category:
    def __init__(self, name, description):
        self.id = uuid4()
        self.description = description
        self.name = name


class Category_Service:
    def create(self, category: Category):
        database[str(category.id)] = {
            'name': category.name,
            'description': category.description
        }
        print('Category has been created..!')

    def update(self, id: str, name: str, description: str):
        current_category = self.get_by_id(id)
        current_category.update({'name': name, 'description': description})

    def delete(self, id: str) -> None:
        current_category = self.get_by_id(id)
        if current_category != {}:
            del database[id]
            print('Category has been deleted..!')
        else:
            print("Category hasn't been deleted")
    def get_all(self, db: dict) -> None:
        print(db)

    def get_by_id(self, id: str):
        for i in database.keys():
            if i == id:
                return database[id]



def main():
    category_service = Category_Service()
    while True:
        process = input('Please type a transaction name: ').lower()

        match process:
            case 'exit':
                print('Application has been closing..!')
                break
            case 'create':
                category_name = input('Category Name: ')
                category_description = input('Description: ')
                category = Category(category_name, category_description)
                category_service.create(category)
            case 'update':
                id = input('Id: ')
                name = input('Name: ')
                description = input('Description: ')
                category_service.update(id, name, description)
                print(category_service.get_by_id(id))
            case 'delete':
                id = input('Id: ')
                category_service.delete(id)
            case 'get all':
                category_service.get_all(database)
            case 'get by id':
                print(category_service.get_by_id(input('Id: ')))
            case _:
                print('Please type a correct transaction name..!')


main()
