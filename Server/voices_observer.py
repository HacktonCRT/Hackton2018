from voice_model import VoiceModel
from voice_db_interface import VoiceDBInterface

class VoicesHandler(object):
    def __init__(self, voice_decibels_recognizer, voice_separator, voice_blamer, voice_container):
        super(VoicesHandler, self).__init__()
        self._voice_decibels_recognizer = voice_decibels_recognizer
        self._voice_separator = voice_separator
        self._voice_blamer = voice_blamer
        self.__voice_db_handler = VoiceDBInterface('VoicesDB.db')
        self.__voice_container = voice_container

    def handle_voice(self, blob):
        voice_models = self._set_voice_properties(blob)

        for voice_model in voice_models:
            if voice_model.decibels_counter is None:
                self.__voice_db_handler.insert_voice(voice_model)

    def _set_voice_properties(self, blob):
        full_voices = []

        self.__voice_container.store_voice(blob)

        for voice in self._voice_separator(blob):
            voice_model = VoiceModel(voice)
            voice_model.decibels_counter = self._voice_decibels_recognize.get_decibels(blob)
            voice_model.voice_relation = self._voice_blamer.get_user_name_by_voice(voice)
            full_voices.append(voice)

        return full_voices


