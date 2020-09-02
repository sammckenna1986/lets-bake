from flask import Flask, render_template, redirect, request, url_for
import mongo


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Recipes_Page')
def recipes_page():
    return render_template("recipes_page.html", recipes)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/Add your recipe')
def upload_recipe():
   return render_template("upload_recipe.html")


#app.route('/Categories{% categorie_name %}')
# def categories():
#   return render_template("categories.html")


@app.route('/Search_Results')
def recipe_display():
    return render_template("recipe_search_display.html", recipes=mongo.db.recipes.find())


@app.route('/Keyword{% cake %}')
def cake_recipe_display():
    return render_template("recipe_search_display.html", recipes=mongo.db.recipes.find("cake"))


if __name__ == '__main__':
    app.run(debug=True)


#def add_recipe(name, prep_time, cooking_time, effort_level, serves, ingredients, method):
#
#    recipe = Recipe(name=name, prep_time=prep_time, cooking_time=cooking_time, effort_level=effort_level, serves=serves, ingredients=ingredients, method=method)
#   recipe.save()