from mongoengine import Document, StringField, IntField

class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()

class Register(Document):
    username = StringField()
    password = StringField()

class Bike(Document):
    model = StringField()
    fee = IntField()
    image = StringField()
    year = IntField()
    
    