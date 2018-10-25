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

    def get_noisy_map(self, mail):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute('SELECT * FROM SeatingTable WHERE Email=("%s")' % (mail))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows[0][2]

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

    def isUserExist(self, username):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        lastHr = math.floor(time.time()) - 3600
        c.execute("select * from NoisyUsers Where Email LIKE \""+username+"\"")
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return len(rows) > 0

    def updateNoisyPerson(self, username, datetime):
        if self.isUserExist(username):
            conn = sqlite3.connect(self._db_path)
            c = conn.cursor()
            c.execute('Update NoisyUsers SET Datetime='+str(datetime)+' where Email="'+username+'"')
            conn.commit()
            conn.close()
        else:
            conn = sqlite3.connect(self._db_path)
            c = conn.cursor()
            c.execute('Insert into NoisyUsers(Email,Datetime) Values ("'+username+'",'+str(datetime)+')')
            conn.commit()
            conn.close()
