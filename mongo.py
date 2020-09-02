import pymongo

cluster = pymongo.MongoClient(
    "mongodb+srv://claireroberts1403:M0ng0DB2020@letsbake.mizcn.mongodb.net/Recipe_Book?retryWrites=true&w=majority")
db = cluster["Recipe_Book"]
collection = db["Recipes"]


results = collection.find({})


for x in results:
    print(x)
