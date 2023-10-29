#!/usr/bin/python
import subprocess,os
from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 80

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

  #Handler for the GET requests
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    # Send the html message
    self.wfile.write("*** Python - Hello World ! ***<br />".encode('utf-8'))
    self.wfile.write("<br />".encode('utf-8'))
    self.wfile.write(("WELCOME_MSG : " + os.getenv('WELCOME_MSG', 'undef')).encode('utf-8') )
    self.wfile.write("<br />".encode('utf-8'))
    self.wfile.write("Hostname is : ".encode('utf-8'))
    self.wfile.write(subprocess.check_output("uname -n", shell=True))
    self.wfile.write("<br />".encode('utf-8'))
    self.wfile.write(("Process ID  : " + str(os.getpid())).encode('utf-8'))
    self.wfile.write("<br />".encode('utf-8'))
    return

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print('Started httpserver on port ' , PORT_NUMBER)

  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print('^C received, shutting down the web server')
  server.socket.close()