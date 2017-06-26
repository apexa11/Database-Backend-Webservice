from flask import Flask
from sqlalchemy import create_engine
from database_Setup import Base,Restaurant,MenuItem
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///RestaurantMenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

@app.route('/restaurants')
def ShowRestaurants():
    restaurants = session.query(Restaurant).all()
    return "restaurants"

@app.route('/restaurant/<int:restaurant_id>/new')
def NewRestaurnt():
    return "newrestaurant"

@app.route('/restaurant/<int:restaurant_id>/edit')
def EditRestaurant():
    return "editrestaurant"

@app.route('/restaurant/<int:restaurant_id>/delete')
def DeleteRestaurant():
    return "deleterestaurant"

@app.route('/restaurant/<int:restaurant_id>/menu')
def ShowMenu():
    return "showmenu"

@app.route('/restaurant/<int:restaurant_id>/new')
def NewMenu():
    return "newmenu"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit')
def EditMenu():
    return "editmenu"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def DeleteMenu():
    return "deletemenu"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
