from flask import Flask ,render_template ,request , url_for,redirect,flash
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
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).first()
    menu = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output=''
        return render_template('menu.html',restaurant=restaurant,menu=menu)

# Default Menu
@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id)
    menu = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
    output=''
        return render_template('menu.html',restaurant=restaurant,menu=menu)

# NEW-MENU

@app.route('restaurant/<int:restaurant_id>/new/', methods = ['GET','POST'])
def newMenuItem(restaurant_id):

    if request.method == 'POST':
        newItem = MenuItem(name = request.form = ['name'] , restaurant_id = restaurant.id)
        session.add (newItem)
        session.commit()
        flash("new item created")
        return redirect(url_for('restaurantMenu'restaurant_id = restaurant.id))
    else:
        return render_template('newmenu.html', restaurant_id = restaurant.id)



# EDIT
@app.route('restaurant/<int:restaurant_id>/<int:menu_id>/edit/' methods = ['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    editItem = session.query(MenuItem).filter_by(id = menu_id ).one()
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
        session.add(editItem)
        session.commit()
        flash("new item edited")
        return redirect(url_for('restaurantMenu'restaurant_id = restaurant.id))
    else:
        return render_template('edititem.html', restaurant_id = restaurant.id,
                                menu_id = menu_id , e = editItem)


# DELETE

@app.route('restaurant/<int:restaurant_id>/<int:menu_id>/delete/' methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id = menu_id ).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash("item deleted")
        return redirect(url_for('restaurantMenu'restaurant_id = restaurant.id))
    else:
        return render_template('deleteitem.html', d = deleteItem)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)