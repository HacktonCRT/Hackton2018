from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from voices_observer import  VoicesHandler
import time
import base64

from Common.decibels_filter import DecibelsRecognizer
from Common.seperate_voice import SeprateVoice
from Common.voice_blamer import VoiceBlamer
from voices_container import VoicesFolderManager
from voice_db_interface import VoiceDBInterface

voice_decibels_recognizer = DecibelsRecognizer()
voice_separator = SeprateVoice()
voice_blamer = VoiceBlamer()
voice_container = VoicesFolderManager()

voices_handler = VoicesHandler(voice_decibels_recognizer, voice_separator, voice_blamer, voice_container)

class VoicesReceiver(BaseHTTPRequestHandler):
    def do_POST(self):
        print "request received"
        if 'handle_voice' in self.path:
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = self.rfile.read(content_len)
            voices_handler.handle_voice(base64.b64encode(post_body))

    def do_GET(self):
        if 'getNoisyPeople' in self.path:
            voice_database = VoiceDBInterface('VoicesDB.db')
            noisy_people = voice_database.get_noisy_people()
            print noisy_people 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(noisy_people)
            self.wfile.write('\n')
            return

    def return_http_ok(self, s=''):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        if s!= '':
            self.wfile.write(s)
        else:
            self.wfile.write("Correct Credentials")


SERVER_URL = r'localhost'
PORT_NUMBER = 8894

if __name__ == "__main__":
    httpd = HTTPServer((SERVER_URL, PORT_NUMBER), VoicesReceiver)
    print time.asctime(), "Server Starts - %s:%s" % (SERVER_URL, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (SERVER_URL, PORT_NUMBER)

