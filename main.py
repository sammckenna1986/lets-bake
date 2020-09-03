from flask import Flask, render_template, redirect, request, url_for
import mongo
from mongo import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipes_page', methods=['GET'])
def recipes_page():
    try:
        recipe = db.recipes.findone({})
        return render_template("recipes_page.html", recipes=recipe)
    except Exception as e:
        return render_template("page_not_found.html"), 404


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


@app.route('/Add your recipe', methods=["POST", "GET"])
def add_recipe():
    return render_template("add_recipe.html")


@app.route('/submit_recipe', methods=["POST", "GET"])
def upload_recipe(recipes=None):
    collection = mongo.db.recipes, recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipe.html'))


# @app.route('/<my_recipe>')
# def my_recipe():
#   return render_template("my_recipe.html")


# @app.route('/{% category % }')
# def category():
#    return render_template("categories.html", category_name=mongo.db.category_name.find())


@app.route('/Search_Results')
def recipe_display():
    return render_template("recipe_search_display.html", recipes=mongo.db.recipes.find())


@app.route('/Cake')
def cake():
    return render_template("cake.html", recipes=mongo.db.recipes.find("cake"))


@app.route('/Biscuits')
def biscuits():
    return render_template("biscuits.html", recipes=mongo.db.recipes.find("biscuits"))


if __name__ == '__main__':
    app.run(debug=True)

# def add_recipe(name, prep_time, cooking_time, effort_level, serves, ingredients, method):
#
#    recipe = Recipe(name=name, prep_time=prep_time, cooking_time=cooking_time, effort_level=effort_level, serves=serves, ingredients=ingredients, method=method)
#   recipe.save()
