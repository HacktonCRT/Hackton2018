from Server import voices_manager
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class VoicesReceiver(BaseHTTPRequestHandler):
	def __init__(self, *args):
		BaseHTTPRequestHandler.__init__(self, *args)

	def do_POST(self):
		pass

	def return_http_ok(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("Correct Credentials")


SERVER_URL = r'http://127.0.0.1:8892/'
PORT_NUMBER = 8892

if __name__ == "__main__":
	voices_folder_manager = voices_manager.VoicesFolderManager(r'\\ptnas1\\Home_Dirs\\omern\\Documents\\GitHub\\Hackton2018\\Server\\Voices\\')
	voices_folder_manager.store_voice('')