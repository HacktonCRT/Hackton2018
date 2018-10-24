import sqlite3
import os
import time
import math

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

    def GetNoiseCountLastHr(self, username):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        lastHr = math.floor(time.time()) - 3600

        c.execute("select Time from NoiseReports Where ReportingPc LIKE \""+username+"\" and time >= "+str(lastHr))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return len(rows)

