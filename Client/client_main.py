import requests
from LiveRecorder import Recorder
import time
import json
import active_directory
import getpass


results = []
def handler(data):
    #fill json
    json_data = {}
    json_data['time'] = time.time()
    json_data['level'] = data
    json_data['computer'] = active_directory.find_user(getpass.getuser()).cn.replace(" ",".") + "@cellebrite.com"
    #send request
    print json.dumps(json_data)
    r = requests.post('http://localhost:8892/handle_voice',json.dumps(json_data))


if __name__ == "__main__":
    Recorder(handler).CheckOngoing()
    #send http
    #with open(fileName, 'rb') as f:
     #   r = requests.post('http://httpbin.org/post', files={fileName: f})
      #  print r.content
