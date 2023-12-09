
from models import Category
from service import CategoryService
from bson.objectid import ObjectId


category_service = CategoryService()


# region Create

# name = input('Name: ')
# description = input('Description: ')
#
# new_category = Category(name, description)
#
# category_service.create(new_category.__dict__)

# endregion


# region Read All

# category_service.list()

# endregion


# region Read All

# print(category_service.get_by_id('65740f4bd9646d28c9926eec'))

# endregion


# region Update

# id = input('Id: ')
# name = input('Name: ')
# description = input('Description: ')
#
# set_values = {
#     'name': name,
#     'description': description,
#     '_BaseEntity__status': 'Modified'
# }
#
# filter_values = {
#     '_id': ObjectId(id)
# }
#
# category_service.update(filter_values, set_values)

# endregion


# region Delete

id = input('Id: ')

set_values = {
    '_BaseEntity__status': 'Passive'
}

filter_values = {
    '_id': ObjectId(id)
}

category_service.update(filter_values, set_values)

# endregion
