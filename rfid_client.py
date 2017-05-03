import socket
from serial import Serial

ser = Serial("/dev/ttyUSB1", 9600)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.0.107'
port = 12002

client_socket.connect((host, port))


while True:
	uid_tag = ser.readline().strip().decode("utf-8")                 
	client_socket.send(uid_tag.encode("utf-8"))
 
client_socket.close()
