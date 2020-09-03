import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["Recipe_Book"] = 'Recipes'
app.config["MONGO_URI"] = "mongodb+srv://claireroberts1403:M0ng0DB2020@letsbake.mizcn.mongodb.net/Recipe_Book?retryWrites=true&w=majority"


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipes_page')
def recipes_page():
    return render_template("recipes_page.html", Recipes=mongo.db.Recipes.find())


@app.route('/Cake')
def cake():
    all_cakes = mongo.db.Recipes.find({"category_name": 'cake'})
    print(all_cakes.count())
    return render_template('cake.html', Recipes=all_cakes)


@app.route('/Biscuits')
def biscuits():
    all_biscuits = mongo.db.Recipes.find({"category_name": 'biscuits'})
    return render_template('biscuits.html', Recipes=all_biscuits)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


@app.route('/Add your recipe', methods=["POST", "GET"])
def add_recipe():
    return render_template("add_recipe.html")


@app.route('/submit_recipe', methods=["POST", "GET"])
def upload_recipe(Recipes=None):
    collection = mongo.db.Recipes, Recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipe.html'))


# @app.route('/<my_recipe>')
# def my_recipe():
#   return render_template("my_recipe.html")


# @app.route('/{% category % }')
# def category():
#    return render_template("categories.html", category_name=mongo.db.category_name.find())


@app.route('/Search_Results')
def recipe_display():
    return render_template("recipe_search_display.html", Recipes=mongo.db.Recipes.find())


if __name__ == '__main__':
    app.run(debug=True)

# def add_recipe(name, prep_time, cooking_time, effort_level, serves, ingredients, method):
#
#    recipe = Recipe(name=name, prep_time=prep_time, cooking_time=cooking_time, effort_level=effort_level, serves=serves, ingredients=ingredients, method=method)
#   recipe.save()


@app.route('/test')
def test():
    all_recipes = mongo.db.Recipes.find({"__id"})
    return render_template('test.html', Recipes=all_recipes)



