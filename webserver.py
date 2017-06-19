from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#import CURD Operation
from Database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#connection to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/restaurants"):
            restaurants = session.query(Restaurant).all()
            self.send_response(200)
            self.send_header('Content-type',     'text/html')
            self.end_headers()
            output=""
            output+="<html><body>"
            for restaurant in restaurants:
                output+= restaurant.name
                output+="<br/>"
            output+="</body></html>"
            self.wfile.write(output)
            return

        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            output=""
            output+="<html><body>Hola!<a href = '/hello'> Back to hello </a> </body></html>"
            self.wfile.write(output)
            print output
            return

        else:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass



def main():
    try:
        port=2210
        server = HTTPServer(('',port),WebServerHandler)
        print"web server running on %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C enter stopping webserver ..."
        server.socket.close()


if __name__ == '__main__':
    main()