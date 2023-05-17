from pymongo import MongoClient
from script.config import DBConf

mongo_uri=DBConf.MONGO_URI

class Mongo:
    client = MongoClient(mongo_uri)
    db = client.interns_b2_23
    myDB = db.Chinmoy