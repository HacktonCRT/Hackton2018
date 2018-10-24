from scipy.io.wavfile import read
import numpy as np

class DecibelChecker:
    @staticmethod
    def GetMaxDecibels(fileName):
        samprate, wavdata = read(fileName)
        chunks = np.array_split(wavdata, 1024)
        dbs = [20*np.log10(np.sqrt(abs(np.mean(chunk**2)))) for chunk in chunks]
        max(dbs)