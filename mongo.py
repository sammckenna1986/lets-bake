import pymongo


cluster = pymongo.MongoClient("mongodb+srv://claireroberts1403:M0ng0DB2020@letsbake.mizcn.mongodb.net/Recipe_Book?retryWrites=true&w=majority")
db = cluster["Recipe_Book"]
collection = db["Recipes"]


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e



post = {"name": "Brilliant Birthday Cake"}

collection.insert_one(post)