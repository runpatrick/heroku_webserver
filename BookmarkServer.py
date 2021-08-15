import http.server
import requests
import os
import threading
from socketserver import ThreadingMixIn
from urllib.parse import unquote, parse_qs

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
