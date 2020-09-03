import datetime
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField, URLField

#https://alysivji.github.io/flask-part1-generating-html-pages-with-mongoengine-jinja2.html


class recipes(Document):
    name = StringField(required=True, max_length=50)
    category_name = StringField(required=True)
    prep_time = StringField(required=True)
    cooking_time = StringField(required=True)
    effort_level = StringField(required=True)
    serves = StringField(required=True)
    ingredients = StringField(required=True)
    method = StringField(required=True, max_length=1000)
    keywords = StringField(required=True)
    uploaded_date = DateTimeField(default=datetime.datetime.now)

    meta = {
        'collection': 'Recipes',  # collection name
        'ordering': ['date'],  # default ordering
        'auto_create_index': False,  # MongoEngine will not create index
        }