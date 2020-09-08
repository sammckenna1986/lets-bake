import os
from typing import List

from env import env
import time
from flask import Flask, render_template, request
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

env = env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# landing page featuring recipe of the week and recently added
@app.route('/')
def index():
    recipe_of_the_week = mongo.db.Recipes.find({"name": 'Chocolate orange brownies'})
    return render_template("index.html", Recipes=recipe_of_the_week)


# cake page displaying all recipes with the category name cake
@app.route('/Cake')
def cake():
    all_cakes = mongo.db.Recipes.find({"category_name": 'cake'})
    return render_template('cake.html', Recipes=all_cakes)


# biscuits page displaying all recipes with the category name biscuits
@app.route('/Biscuits')
def biscuits():
    all_biscuits = mongo.db.Recipes.find({"category_name": 'biscuits'})
    return render_template('biscuits.html', Recipes=all_biscuits)


# all recipes page displaying all recipes
@app.route('/All_Recipes')
def all_recipes():
    all_recipes = mongo.db.Recipes.find({})
    return render_template('all_recipes.html', Recipes=all_recipes)


# 404 error page personalised to site
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


# send user to add recipe page form
@app.route('/Add your recipe')
def add_recipe():
    return render_template("add_recipe.html")


# submit recipe page the RUD in crud, users can preview edit and delete recipes
@app.route('/submit_recipe', methods=["POST"])
def upload_recipe():
    add_recipe = mongo.db.Recipes

    name = request.form['name']
    category_name = request.form['category_name']
    prep_time = request.form['prep_time']
    cooking_time = request.form['cooking_time']
    effort_level = request.form['effort_level']
    serves = request.form['serves']
    ingredients = request.form['ingredients']
    method = request.form['method']
    recipe_image = request.files['recipe_image']

    add_recipe_form = {
        "name": name,
        "category_name": category_name,
        "prep_time": prep_time,
        "cooking_time": cooking_time,
        "effort_level": effort_level,
        "serves": serves,
        "ingredients": ingredients,
        "method": method,
        "recipe_image": recipe_image,
        "date_added": time.asctime(time.localtime(time.time()))
    }
    add_recipe.insert_one(request.form.to_dict())
    mongo.save_file(recipe_image.filename, recipe_image)
    return render_template("Message.html")


# Edit Recipe
@app.route("/recipe/<Recipes_id>/edit", methods=["GET", "POST"])
def edit_recipe(Recipes_id):
    Recipes = mongo.db.Recipes
    my_Recipe = mongo.db.Recipes.find_one({"_id": ObjectId(Recipes_id)})
    if request.method == "POST":
        Recipes.update({"_id": ObjectId(Recipes_id)}, {
            "name": request.form.get("name"),
            "category_name": request.form.get("category_name"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get('ingredients'),
            "method": request.form.get('method'),
            "image": request.form.get("image"),
        })
        return redirect(url_for('my_recipe', Recipes_id=Recipes_id))
    else:
        form = add_recipe_form()
        return render_template('add_recipe.html',
                               selected_recipe=selected_recipe, form=form)


# delete function
@app.route('/recipe/<Recipes_id>/delete')
def deleteRecipe(Recipes_id):
    mongo.db.Recipes.remove({'_id': ObjectId(Recipes_id)})
    return render_template("index.html")

#test to see recipe image returning from mongodb
@app.route('/image/<recipe_image>')
def image(recipe_image):
    return mongo.send_file(recipe_image)

# recipes page display entire recipe with 3 you may like cards
@app.route('/my_recipe/<name>')
def my_recipe(name):
    my_recipe = mongo.db.Recipes.find_one_or_404({"name": name})
    return render_template("my_recipe.html", my_recipe=my_recipe)


# search results page to display search results containing keywords
@app.route('/search_results')
def recipe_display():
    user_search = request.form("user_search")
    search_results = mongo.db.Recipes.find(user_search)
    return render_template("recipe_search_display.html", Recipes=mongo.db.Recipes.find(search_results))


if __name__ == '__main__':
    app.run(debug=True)


# page to complete mongo tests
@app.route('/test')
def test():
    all_recipes = mongo.db.Recipes.find({"_id"})
    return render_template('test.html', Recipes=all_recipes)
