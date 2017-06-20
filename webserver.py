#!/usr/bin/python
# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CURD Operation

from Database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connection to database

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path.endswith('/restaurants'):

            restaurants = session.query(Restaurant).all()

            self.send_response(200)

            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ''
            output += '<html><body>'
            output += \
                "<a href = '/restaurants/new'> Make New Restaurant Here </a>"
            output += '<br/>'
            for restaurant in restaurants:
                output += restaurant.name
                output += '<br/>'
                output += \
                    "<a href = '/restaurants/%s/edit' > Edit </a>" \
                    % restaurant.id
                output += '<br/>'
                output += \
                    "<a href = '/restaurants/%s/delete' > Delete </a>" \
                    % restaurant.id
                output += '<br/>'

            output += '</body></html>'
            self.wfile.write(output)
            return

        if self.path.endswith('/restaurants/new'):

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ''
            output += '<html><body>'
            output += 'New Restaurant'
            output += \
                '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name="newRestaurantName" type="text" placeholder = "NewRestaurantName"><input type="submit" value="Create"> </form>'''
            output += ' </body></html>'
            self.wfile.write(output)
            print output
            return

        if self.path.endswith('/edit'):
            restaurantsIdPath = self.path.split('/')[2]
            myRestaurantQuery = \
                session.query(Restaurant).filter_by(id=restaurantsIdPath).one()
            if myRestaurantQuery:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ''
                output += '<html><body>'
                output += '<h1>'
                output += myRestaurantQuery.name
                output += '</h1>'
                output += \
                    "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" \
                    % restaurantsIdPath
                output += \
                    "<input name='newRestaurantName' type='text' placeholder = '%s'>" \
                    % myRestaurantQuery.name
                output += "<input type='submit' value='Rename'> </form>"
                output += '</body></html>'
                self.wfile.write(output)
                print output
                return

        if self.path.endswith('/delete'):
            restaurantsIdPath = self.path.split('/')[2]
            myRestaurantQuery = \
                session.query(Restaurant).filter_by(id=restaurantsIdPath).one()
            if myRestaurantQuery != []:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += ''
                output += '<html><body>'
                output += '<h1>Are you sure want to delete %s?' \
                    % myRestaurantQuery.name
                output += '</h1>'
                output += \
                    "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" \
                    % restaurantsIdPath
                output += \
                    "<input type = 'submit' value='Delete'> </form>"
                output += '</body></html>'
                self.wfile.write(output)
                print output
                return
        else:

            self.send_error(404, 'File Not Found %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith('/edit'):
                (ctype, pdict) = \
                    cgi.parse_header(self.headers.getheader('content-type'
                        ))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                restaurantsIdPath = self.path.split('/')[2]
                myRestaurantQuery = \
                    session.query(Restaurant).filter_by(id=restaurantsIdPath).one()
                if myRestaurantQuery != []:
                    myRestaurantQuery.name = messagecontent[0]
                    session.add(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith('/delete'):
                (ctype, pdict) = \
                    cgi.parse_header(self.headers.getheader('content-type'
                        ))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                restaurantsIdPath = self.path.split('/')[2]
                myRestaurantQuery = \
                    session.query(Restaurant).filter_by(id=restaurantsIdPath).one()
                if myRestaurantQuery != []:
                    session.delete(myRestaurantQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith('/restaurants/new'):

                (ctype, pdict) = \
                    cgi.parse_header(self.headers.getheader('content-type'
                        ))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')
                newRestaurant = Restaurant(name=messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()
        except:

            # self.send_response(301)
            # self.send_header('Content-type', 'text/html')
            # self.end_headers()
            # ctype, pdict = cgi.parse_header(
             #   self.headers.getheader('content-type'))
            # if ctype == 'multipart/form-data':
             #   fields = cgi.parse_multipart(self.rfile, pdict)
              #  messagecontent = fields.get('message')
            # output = ""
            # output += "<html><body>"
            # output += " <h2> Okay, how about this: </h2>"
            # output += "<h1> %s </h1>" % messagecontent[0]
            # output += '''<form method='POST' enctype='multipart/form-data' action='//restaurants/new'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            # output += "</body></html>"
            # self.wfile.write(output)
            # print output

            pass


def main():
    try:
        port = 2210
        server = HTTPServer(('', port), WebServerHandler)
        print 'web server running on %s' % port
        server.serve_forever()
    except KeyboardInterrupt:

        print '^C enter stopping webserver ...'
        server.socket.close()


if __name__ == '__main__':
    main()
