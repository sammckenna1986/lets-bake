import datetime
import mongoengine

class Recipes(mongoengine.Document):
    name = mongoengine.StringField(required=True, max_length=50)
    prep_time = mongoengine.StringField(required=True)
    cooking_time = mongoengine.StringField(required=True)
    effort_level = mongoengine.StringField(required=True)
    serves = mongoengine.StringField(required=True)
    ingredients = mongoengine.StringField(required=True)
    method = mongoengine.StringField(required=True, max_length=1000)
    keywords = mongoengine.StringField()
    uploaded_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'recipes'
    }