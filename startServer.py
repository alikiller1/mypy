import os
import re
import urllib
import logging
import logging.handlers
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class TestHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        templateStr = 'hello world'

        self.protocal_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header("Welcome", "Contect")
        self.end_headers()
        self.wfile.write(templateStr)


def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever();


print "serving at port", 8000
start_server(8000)

