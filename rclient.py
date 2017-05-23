import sys
import json
import requests
from serial import Serial

from datetime import datetime

ser = Serial("/dev/ttyACM0", 9600)
while True:
    uid_tag = ser.readline().strip().decode("utf-8")  
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conv = {'pino': 'x01', 'uid': uid_tag, 'time':t}
    s = json.dumps(conv)
    r = requests.post("http://192.168.0.106:5000/", json=s).json()
    print(r['result'])
