from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from voices_observer import  VoicesHandler

class VoicesReceiver(BaseHTTPRequestHandler):
    def __init__(self, *args):
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
        pass
       #if self.path.contains('handle_voice'):

    def return_http_ok(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Correct Credentials")


SERVER_URL = r'http://192.168.56.126:8892/'
PORT_NUMBER = 8892

if __name__ == "__main__":
    voices_handler = VoicesHandler()


