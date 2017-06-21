from flask import Flask
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
@app.route('/hello')
def HelloWorld():
    restaurant = session.query(Restaurant).first()
    menu = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output=''

    for items in menu:
        output+=items.name
        output+= "<br>/"
        return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)