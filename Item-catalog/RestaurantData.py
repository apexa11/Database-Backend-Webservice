from sqlalchemy import create_engine
from database_Setup import Base,Restaurant,MenuItem
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///RestaurantMenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

restaurant1 = Restaurant(name = "BBQ")
session.add(restaurant1)
session.commit()

Menu1 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.50", course="Entree", restaurant=restaurant1)
session.add(Menu1)
session.commit()

Menu2 = MenuItem(name="French Fries", description="with garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)
session.add(Menu2)
session.commit()

Menu3 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$5.50", course="Entree", restaurant=restaurant1)
session.add(Menu3)
session.commit()

restaurant2 = Restaurant(name = "Apna Punjab")
session.add(restaurant2)
session.commit()

Menu1 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant2)
session.add(Menu1)
session.commit()

Menu2 = MenuItem(name="Sirloin Burger", description="Made with grade A beef",
                     price="$7.99", course="Entree", restaurant=restaurant2)
session.add(Menu2)
session.commit()

Menu3 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant2)
session.add(Menu3)
session.commit()

restaurant3 = Restaurant(name = "Taste")
session.add(restaurant3)
session.commit()

Menu1 = MenuItem(name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant3)

session.add(Menu1)
session.commit()

Menu2 = MenuItem(name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant3)

session.add(Menu2)
session.commit()

Menu3 = MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant3)

session.add(Menu3)

