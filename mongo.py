import pymongo
import os

MONGODB_URI = os.getenv("mongodb://localhost:27017/myDatabase")
DBS_NAME = "Recipe_Book"
COLLECTION_NAME = "Recipes"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)
