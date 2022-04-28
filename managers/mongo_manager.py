from pymongo import MongoClient
from pymongo import cursor

from config import MONGO, DB_NAME

class MongoManager:

    client:MongoClient = None

    def __init__(self) :
        self.client = MongoClient(MONGO)
        self.db = self.client[DB_NAME]

    def add_data(self, collection_name : str, entry : dict) -> bool:

        try:
            self.db[collection_name].insert_one(entry)
        except:
            return False

        return True

    def get_all_data(self, collection_name : str, query : dict) -> cursor:

        try:
            result_cursor = self.db[collection_name].find(query)
        except:
            return None

        return result_cursor

    def get_documents_length(self, col_name : str, query : dict) -> int:
        count = self.db[col_name].count_documents(query)
        return count

    def remove_all_data(self, col_name : str, query : dict) -> bool:
        try:
            self.db[col_name].delete_many(query)
        except:
            return False

        return True

    def update_all_data(self, col_name : str, query : dict, updated_data: dict):
        self.db[col_name].update_many(query, {"$set" : updated_data})


manager = None

async def init_mongo():
    global manager

    try:
        manager = MongoManager()
    except Exception as e:
        return f"Error while loading database {e}"

    return "Connected to Database Successfully"