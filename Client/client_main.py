import requests
from Recorder import TimeRecorder

if __name__ == "__main__":
    for i in range(1,3):
        #fileName = str(time.time())+".wav"
        fileName = "deen_" +str(i) + ".wav"
        TimeRecorder(fileName).Record()
    exit(0)
    #send http
    with open(fileName, 'rb') as f:
        r = requests.post('http://httpbin.org/post', files={fileName: f})
        print r.content
