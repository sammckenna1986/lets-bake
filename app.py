import os
from flask import Flask, render_template
from flask_pymongo import PyMongo, pymongo
import data.mongo_setup as mongo_setup
#import mongoengine

#def main():
#    mongo_setup.global_init()

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["Recipe_Book"]
mycol = mydb["Recipes"]

#recipes = ["Recipes"]

#alias_core = 'core'
#db = 'Recipe_Book'

#ongoengine.register_connection(alias=alias_core, name=db)


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