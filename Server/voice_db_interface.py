import sqlite3
import os

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

    def get_noisy_people(self):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute('SELECT * FROM NoisyUsers order by Datetime')
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    def insert_noise_times(self, reporting_pc, time, level):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute('INSERT INTO NoiseReports(Time, ReportingPc, Level) VALUES (%s, "%s", %s)' % (time,reporting_pc,level))
        conn.commit()
        conn.close()
