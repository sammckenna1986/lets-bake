import os
from flask import Flask, render_template
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Recipe_Book"]
collection = db["Recipes"]


for x in mycol.find():
  print(x)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Recipes')
def recipes():
    return render_template("recipes.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


#@app.route('/Add your recipe')
#def upload():
#   return render_template("upload.html")

#@app.route('/Search Results')
#def search():
#   return render_template("search.html")


#app.route('/Categories{% categorie_name %}')
# def categories():
#   return render_template("categories.html")

def recipe_display:
    db.Recipe_Book.find({}, {"name": 1});


if __name__ == '__main__':
    app.run(debug=True)


#def add_recipe(name, prep_time, cooking_time, effort_level, serves, ingredients, method):
#
#    recipe = Recipe(name=name, prep_time=prep_time, cooking_time=cooking_time, effort_level=effort_level, serves=serves, ingredients=ingredients, method=method)
#   recipe.save()


#def search_recipes() -> List[Recipes]:
#    recipe_search_results = Recipes()
#    .keyword
#
#    return list(recipe_search_results)