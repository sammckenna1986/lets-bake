import os
from flask import Flask, render_template
from flask_pymongo import PyMongo, pymongo




app = Flask(__name__)


MONGO_URI = os.environ.get(“MONGO_URI”)
mongo = PyMongo(app)


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
