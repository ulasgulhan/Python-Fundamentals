
# MongoDB Server ile iletişime geçmek için pymongo modülüne ihtiyacımız var

from pymongo import MongoClient
from pprint import pprint


# Connection String oluşturduk. Server ile bağlantı sağladık.
conn = MongoClient('mongodb://localhost:27017')

# Server üzerinde bir veritabanı yarattık
db = conn['app_db']

# Veri tabanı içerisinde bşr koleksiyon yaratıyoruz
collection = db['products']

# region Insert One Record

# product_name = input('Name: ')
# price = input('Price: ')
#
# product = {
#     'name': product_name,
#     'price': price
# }
#
# result = collection.insert_one(product)
# print(result)

# endregion


# region Insert Many

# product_list = [
#     {'_id': 1, 'name': 'Lenovo X1 Carbon', 'price': 74.999},
#     {'_id': 2, 'name': 'Macbook Pro M3', 'price': 149.999},
#     {'_id': 3, 'name': 'Asus Zenbook 5', 'price': 142.999},
#     {'_id': 4, 'name': 'HP Pavillion', 'price': 46.999},
#     {'_id': 5, 'name': 'Monster Alba', 'price': 33.999},
# ]
#
# collection.insert_many(product_list)

# endregion


# region Read

# Tüm kayıtları ekrana basın

# for item in collection.find():
#     pprint(item)


# Fiyatı 100 binden fazla olan ürünleri listeleyin

# filter_input = {
#     'price': {
#         '$gt': 100.000
#     }
# }
#
# for item in collection.find(filter_input):
#     pprint(item)


# Fiyatı 80 bine eşit ve aşağı olan ürünleri listeleyiniz

# filter_input = {
#     'price': {
#         '$lte': 80.000
#     }
# }
#
# for item in collection.find(filter_input):
#     pprint(item)


# Fiyatı 46.999'a eşit olan ürünleri listeleyiniz

# for item in collection.find({'price': 46.999}):
#     pprint(item)


# Ürün adı içerisinde L harfi geçen ürünleri listeleyiniz. Bu işlemi yaparken özel keyword olarak '$regex' kullanın

# for item in collection.find({'name': {'$regex': 'L.'}}):
#     pprint(item)

# endregion


# region Update Record

# result = collection.update_one(
#     # Güncellemek istediğimiz kaydı yakalıyoruz
#     {'name': 'Monster Alba'},
#     # Yeni değerleri yukarıda yakaladığımız kayda set ediyoruz.
#     {'$set': {'name': 'Dell Vega 1.1', 'price': 69.99}}
# )
#
# print(f'{result.modified_count} adet kayıt güncellendi')

# endregion


# region Delete record

collection.delete_one({'name': 'Dell Vega 1.1'})

# endregion
