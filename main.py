from flask import Flask, render_template, redirect, request, url_for
import mongo


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipes_page')
def recipes_page():
    return render_template("recipes_page.html", recipes=mongo.db.recipes.find())


@app.route('/Cake')
def cake():
    all_cakes = mongo.db.recipes.find({"category_name": 'cake'})
    return render_template('cake.html', recipes=all_cakes)


@app.route('/Biscuits')
def biscuits():
    all_biscuits = mongo.db.recipes.find({"category_name": 'biscuits'})
    return render_template('biscuits.html', recipes=all_biscuits)


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


if __name__ == '__main__':
    app.run(debug=True)

# def add_recipe(name, prep_time, cooking_time, effort_level, serves, ingredients, method):
#
#    recipe = Recipe(name=name, prep_time=prep_time, cooking_time=cooking_time, effort_level=effort_level, serves=serves, ingredients=ingredients, method=method)
#   recipe.save()


@app.route('/test')
def test():
    all_recipes = mongo.db.recipes.find({"__id"})
    return render_template('test.html', recipes=all_recipes)


print(name.count())

