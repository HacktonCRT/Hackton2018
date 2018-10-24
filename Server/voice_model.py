class VoiceModel(object):
    def __init__(self, blob):
        super(VoiceModel, self).__init__()
        self._voice_relation = ""
        self._blob = blob

    @property
    def voice_relation(self):
        return self._voice_relation

    @voice_relation.setter
    def voice_relation(self, value):
        self._voice_relation = value

    @property
    def voice_relation(self):
        return self._blob