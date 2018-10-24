class VoicesHandler(object):
    def __init__(self, voice_filtering, voice_separator, voice_blamer):
        super(VoicesHandler, self).__init__()
        self._voice_filtering = voice_filtering
        self._voice_separator = voice_separator
        self._voice_blamer = voice_blamer

    def handle_voice(self, blob):
        voices = self._voice_separator(blob)

        for voice in voices:
            if self._voice_filtering.validate_voice(voice):
                user_name = self._voice_blamer.get_user_name_by_voice(voice)
            return None

