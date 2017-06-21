from flask import Flask ,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

#import database
@app.route('/')
@app.route('/restaurant/<int:restaurant_id>/')
def restaurant():
    restaurant = session.query(Restaurant).first()
    menu = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output=''
        return render_template('menu.html',restaurant=restaurant,menu=menu)

# Task 1: Create route for newMenuItem function here

@app.route('restaurant/<int:restaurant_id>/new/', methods = ['GET','POST'])
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)