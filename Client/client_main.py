import requests
from LiveRecorder import Recorder
import time
import json
import socket


results = []
def handler(data):
    #fill json
    json_data = {}
    json_data['time'] = time.time()
    json_data['level'] = data
    json_data['computer'] = socket.gethostname()
    #send request
    print json.dumps(json_data)
    r = requests.post('http://localhost:8892/handle_voice',json.dumps(json_data))


if __name__ == "__main__":
    Recorder(handler).CheckOngoing()
    #send http
    #with open(fileName, 'rb') as f:
     #   r = requests.post('http://httpbin.org/post', files={fileName: f})
      #  print r.content
