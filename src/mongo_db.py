from pymongo import MongoClient
import config

def connect_mongo_db():
    client = MongoClient(config.mongo_connection_string)
    return client
