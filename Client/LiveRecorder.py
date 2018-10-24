from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import time

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
MAX = 30000 #32767 is the max of my mic

class Recorder:
    def __init__(self, handler):
        self.__handler__ = handler

    def is_loud(self,snd_data):
        return max(snd_data) > MAX
    def CheckOngoing(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=2, rate=RATE,
                        input=True, output=True,
                        frames_per_buffer=CHUNK_SIZE)
        r = array('h')
        while 1:
            # little endian, signed short
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            if self.is_loud(snd_data):
                #print "TOO LOUD!!! - " + str(max(snd_data))
                self.__handler__(max(snd_data))

if __name__ == '__main__':
    print("please speak a word into the microphone")
    #Recorder().record_to_file('liron_reg_voice2.wav')
    Recorder().CheckOngoing()