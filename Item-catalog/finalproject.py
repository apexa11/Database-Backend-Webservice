from flask import Flask
from sqlalchemy import create_engine
from database_Setup import Base,Restaurant,MenuItem
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///RestaurantMenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

@app.route()
def ShowRestaurants():
    return "restaurants"

@app.route()
def NewRestaurnt():
    return "newrestaurant"

@app.route()
def EditRestaurant():
    return "editrestaurant"

@app.route()
def DeleteRestaurant():
    return "deleterestaurant"

@app.route()
def ShowMenu():
    return "showmenu"

@app.route()
def NewMenu():
    return "newmenu"

@app.route()
def EditMenu():
    return "editmenu"

@app.route()
def DeleteMenu():
    return "deletemenu"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
