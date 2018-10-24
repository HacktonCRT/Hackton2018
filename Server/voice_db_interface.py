import sqlite3

class VoiceDBInterface(object):
    def __init__(self, database_path):
        super(VoiceDBInterface, self).__init__()
        self._db_path = database_path

    def insert_voice(self, voice_model):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute('INSERT INTO Voices(DecibalsCounter, UserName, VoiceData) VALUES ("1", "1", "%s")' % (voice_model.blob))
        conn.commit()
        conn.close()