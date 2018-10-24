import os.path
import uuid
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import urlparse
import glob
import os
from random import randint
from time import sleep
import subprocess
import re

class VoicesObserver(object):
	def __init__(self):
		super(VoicesObserver, self).__init__()
		self._components = []
	
	def notify(self, blob):
		for component in self._components:
			component.get_voice(blob)

	def subscribe(self, component):
		self._components.add(component)

	def unsubscribe(self, component):
		self._components.remove(component)

class VoicesReciver(BaseHTTPRequestHandler):
	def __init__(self, *args):
		self._server = Server()
		BaseHTTPRequestHandler.__init__(self, *args)

	def do_POST(self):
		if self.path.endswith('store_record'):
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read(content_length) 
			self.return_http_ok()

	def return_http_ok(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("Correct Credentials")		

class VoicesFolderManager(object):
 	def __init__(self, folder_path):
 		super(VoicesFolderManager, self).__init__()
		self.__folder_path = folder_path

	def store_voice(self, blob):
		voice_file = open(self.__folder_path + str(uuid.uuid4()), "w")						


SERVER_URL = r'http://127.0.0.1:8892/'
PORT_NUMBER = 8892

if __name__ == "__main__":
	voices_folder_manager = VoicesFolderManager(r'\\ptnas1\\Home_Dirs\\omern\\Documents\\GitHub\\Hackton2018\\Server\\Voices\\')
	voices_folder_manager.store_voice("fewfeewfewfewfweewewgherg")