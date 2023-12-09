
from pymongo import MongoClient
from models import Category


# region Connection DB

conn = MongoClient('mongodb://localhost:27017')

db = conn['CRUD']

category_collection = db['categories']

# endregion

# region Seed Data
# Proje ilk çalıştırıldığında veri tabanı ile ilk bağlantı kurulduğunda collection yaratılacak ve bu yaratılan collection içerisine "sample data" insert etme işlemine tohumlama diyoruz. Burada amaç projedeki read operasyonlarını hızlıca yapabilmektir.
# Uyarı : Seed data bir kez yapılır. İşlem başarılı olduktan sonra buradaki kodları yoruma almayı unutmayın.

# category_seed_data = [
#     Category('Boxing Gloves', 'Everlast produce best boxing gloves').__dict__,
#     Category('Punching Bags', 'Everlast produce best punching bags').__dict__,
#     Category('Protective Equipment', 'Everlast produce best protective equipment').__dict__,
# ]
#
# category_collection.insert_many(category_seed_data)


# endregion
