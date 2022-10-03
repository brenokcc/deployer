#!/usr/bin/env python
import os
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        data = urllib.parse.parse_qs(self.path[2:])
        self.wfile.write('{}'.format(data).encode())
    def do_POST(self):
        output = ''
        self.send_response(200)
        self.end_headers()
        data = json.loads(self.rfile.read(int(self.headers.get('Content-Length'))).decode())
        print(data)
        with open('keys.yaml') as file:
            action = 'deploy' if 'deploy' in data else 'undeploy'
            key = data[action]
            for line in file.readlines():
                tokens = line.strip().split(': ')
                if tokens[0] == key:
                    url = tokens[1]
                    output = os.popen('./{}.sh {} {}'.format(action, url, key)).read()
        print(output)
        with open('server.log', 'a') as file:
            file.write('{}\n\n'.format(output))
        self.wfile.write('{}'.format(output).encode())

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()