import socket
import MySQLdb 
from subprocess import call            

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.0.107' //Need to change to get the IP of the system
port = 12348         

server_socket.bind((host, port))        
server_socket.listen(5)
c, addr = server_socket.accept()     
uid_tag=c.recv(1024).decode("utf-8")
print("The UID of the Scanned Person is " + uid_tag)

db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '1192001',db = 'nischal')
str = 'select * from details where id = ' + uid_tag
cur = db.cursor()
num = cur.execute(str)

if num!=0:
	print("Database identified")
	for row in cur.fetchall():
		print(row)

else:
	print("Not A Genuine Person")

c.close() 




               
