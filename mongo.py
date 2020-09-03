import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('localhost', 27017)

cluster = pymongo.MongoClient(
    "mongodb+srv://claireroberts1403:M0ng0DB2020@letsbake.mizcn.mongodb.net/Recipe_Book?retryWrites=true&w=majority")
db = cluster["Recipe_Book"]
collection = db["Recipes"]


results = collection.find({"category_name": 'biscuits'})
# https://api.mongodb.com/python/current/tutorial.html
# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})


for x in results:
    print(x)

