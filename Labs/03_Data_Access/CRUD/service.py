
from abc import ABC, abstractmethod
from settings import category_collection
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError
from pprint import pprint


class AbstractBaseService(ABC):
    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def update(self, filter_value: dict, set_value: dict): pass

    @abstractmethod
    def list(self): pass

    @abstractmethod
    def get_by_id(self, pk): pass


class CategoryService(AbstractBaseService):
    def create(self, item: dict):
        try:
            category_collection.insert_one(item)
            print('Category has been created..!')
        except PyMongoError as err:
            print(err.__doc__)

    def update(self, filter_value: dict, set_value: dict):
        result = category_collection.update_one(
            filter_value,
            {
                '$set': set_value
            }
        )

        print(f'{result.modified_count} adet kayıt etkilendi')

        pprint(self.get_by_id(filter_value['_id']))

    def list(self):
        result = category_collection.find({"_BaseEntity__status": {"$in": ["Active", "Modified"]}})

        for item in result:
            pprint(f'Category Name: {item["name"]} Description: {item["description"]}')

    def get_by_id(self, pk):
        return category_collection.find_one({
            '_id': ObjectId(pk),
            "_BaseEntity__status": {"$in": ["Active", "Modified"]}
        })
