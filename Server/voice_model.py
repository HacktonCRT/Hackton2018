class VoiceModel(object):
    def __init__(self, blob):
        super(VoiceModel, self).__init__()
        self._voice_relation = None
        self._decibels_counter = None
        self._blob = blob

    @property
    def blob(self):
        return self._blob

    @property
    def voice_relation(self):
        return self._voice_relation

    @property
    def decibels_counter(self):
        return self._decibels_counter

    @voice_relation.setter
    def voice_relation(self, value):
        self._voice_relation = value

    @decibels_counter.setter
    def decibels_counter(self, value):
        self._decibels_counter = value



