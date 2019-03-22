from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

port = input("Port: ")

class serverHanler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
            self.path="/index.html"
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            
            if sendReply == True:
                page = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(page.read())
                return
        
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

try:
    server = HTTPServer(('', port), serverHanler)
    print ('Started HTTPServer on', port)
    
    server.serve_forever()

except KeyboardInterrupt:
    print ('<CRTL-C> Shutdown server')
    server.socket.close