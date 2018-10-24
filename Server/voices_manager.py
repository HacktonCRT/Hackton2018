import uuid
import os.path

class VoicesFolderManager(object):
    def __init__(self, folder_path):
        super(VoicesFolderManager, self).__init__()
        self.__folder_path = folder_path

    def store_voice(self, blob):
        voice_file = open(self.__folder_path + str(uuid.uuid4()), "w")