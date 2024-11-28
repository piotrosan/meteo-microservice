import pymongo
from pymongo.cursor import Cursor


class MongoOperations:
    client = None
    active_database = None
    active_collection = None

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://root:example@localhost:27017/?directConnection=true')

    def set_active_database(self, name: str):
        self.active_database = self.client[name]

    def set_active_collection(self, collection: str):
        self.active_collection = self.active_database.get_collection(collection)

    def _check_if_exist(self, data: dict) -> bool:
        exists = self.active_collection.find_one(data)
        return bool(exists)

    def save(self, data: dict) -> bool:
        if not self._check_if_exist(data):
            data_id = self.active_collection.insert_one(data).inserted_id
            return bool(data_id)
        return False

    def get_all(self) -> Cursor:
        return self.active_collection.find()
