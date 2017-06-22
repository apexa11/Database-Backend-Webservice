#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# import database

@app.route('/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return render_template('menu.html', restaurant=restaurant,
                           menu=menu,restaurant_id = restaurant_id)


# NEW-MENU

@app.route('/restaurant/<int:restaurant_id>/new', methods=['GET', 'POST'
           ])
def newMenuItem(restaurant_id):

    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
                           restaurant_id=restaurant.id)
        session.add(newItem)
        session.commit()
        flash('new item created')
        return redirect(url_for('restaurantMenu',
                        restaurant_id=restaurant_id))
    else:
        return render_template('newmenu.html',
                               restaurant_id=restaurant_id)


# EDIT

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
        session.add(editItem)
        session.commit()
        flash('new item edited')
        return redirect(url_for('restaurantMenu',
                        restaurant_id=restaurant.id))
    else:
        return render_template('edititem.html',
                               restaurant_id=restaurant.id,
                               menu_id=menu_id, e=editItem)


# DELETE

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash('item deleted')
        return redirect(url_for('restaurantMenu',
                        restaurant_id=restaurant.id))
    else:
        return render_template('deleteitem.html', d=deleteItem)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
