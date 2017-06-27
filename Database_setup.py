import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    picture = Column(String(250))
    email = Column(String(250), nullable = False)

       @property
    def serialize(self):
        # Return object data in serializeble format
        return {
            'name' : self.name,
            'id' : self.id,
            'picture' : self.picture,
            'email': self.email,
        }


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return object data in serializeble format
        return {
            'name' : self.name,
            'id' : self.id,
            'user_id' = self.user_id,
        }


class MenuItem(Base):
    __tablename__ = "menu_item"

    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price =Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        # Return object data in serializeble format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'course' : self.course,
            'price': self.price,
        }


engine = create_engine('sqlite:///restaurantmenuwithusers.db')


Base.metadata.create_all(engine)
