import os
from flask import Flask, render_template



app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("DATABASE")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


class PyMongo(object):
    pass


mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run(debug=True)
