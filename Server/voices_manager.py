import os.path
import uuid

class voices_folder_manager(object):
 	def __init__(self, folder_path):
			self.__folder_path = folder_path

	def store_voice(self, blob):
		voice_file = open(self.__folder_path + uuid.uuid4(), "w")						