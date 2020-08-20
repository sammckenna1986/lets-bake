import os
from flask import Flask

app = Flask(__name__)

app.secret_key = os.getenv("SECRET", "randomstring123")



@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run()