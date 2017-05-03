import socket               

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        

host='192.168.0.107' //Need to change to get the IP of the system
port = 12301

uid_tag='2551'

client_socket.connect((host, port))
client_socket.send(uid_tag.encode("utf-8"))
client_socket.close
