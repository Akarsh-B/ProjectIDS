from flask import Flask,render_template
from flask import request
import json
import MySQLdb

app = Flask(__name__)
global data

@app.route('/', methods = ['POST'])
def determine_escalation(): #for rfid verification only
    jsondata = request.get_json()
    data = json.loads(jsondata)
    fd = open('authorize.log', 'a')
    uid_tag = data['uid']
    enc_tag = "".join("{:02x}".format(ord(c)) for c in uid_tag) #encoding the uid in a format readable by mysql
    db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '13sep95', db = 'project') #connect to database
    str = 'select name, age from rfid where uid = ' + enc_tag #the mysql query
    cur = db.cursor()
    num = cur.execute(str) #execute the query
    if num != 0: #checking if vaild details exist
        for row in cur.fetchall(): name = row[0]
        data['name'] = name
        r = {'result' : 'Authorized'}
    else:
        '''since rfid is invalid,
        the person is directly classified as an intruder
        and there will be no facial recognition phase '''
        data['auth'] = 'Unauthorized
        data['name'] = 'Unknown'
        r = { 'result' : 'Unauthorized'}
        lst = data['pino'] + ' ' + data['uid'] + ' ' + data['name'] + ' ' + data['time']+ ' ' + data['auth'] + '\n' #details of the failed rfid authentication phase
        fd.write(lst) #writing the details into the log file
        fd.close()
    db.close()

    return json.dumps(r)

@app.route('/facerec', methods = ['POST'])
def write_data():#for obtaining and processing the results of facial recognition
    fd = open('authorize.log', 'w')
    jsdata = request.get_json()
    d = json.loads(jsondata)
    if d['uid'] != data['uid']: #if uid of rfid card and face recognition phase do not match the person is an intruder
        #this step is to identify the intruder to check if he is someone known
        actual_uid = d['uid']
        data['auth'] = 'Unauthorized'
        enc_tag = "".join("{:02x}".format(ord(c)) for c in actual_uid)
        db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '13sep95', db = 'project')
        str = 'select name from rfid where uid = ' + enc_tag
        cur = db.cursor()
        num = cur.execute(str)
        if num != 0: #intruder identified
            for row in cur.fetchall(): name = row[0]
            data['name'] = name
            r = {'res': 'Authorized'}
        else: #unknown intruder
            data['name'] = 'Unknown'
            r = {'res': 'Unauthorized'}
        db.close()
        #now to write the final result of the operation in the log file
    lst = data['pino'] + ' ' + data['uid'] + ' ' + data['name'] + ' ' + data['time']+ ' ' + data['auth'] + '\n'
    fd.write(lst)
    fd.close()

    return json.dumps(r)

@app.route('/check')
def check(): #displays the log details in a webpage for system admin 
    fd = open('authorize.log', 'r')
    rd = fd.read()
    fd.close()
    return render_template('alert.html', result = rd)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5000,debug=True)
