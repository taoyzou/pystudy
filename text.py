import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('10.20.133.78',218))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
 data = mysock.recv(512)
 if(len(data) < 1):
 	break
 	print(data.decode(),end='')
 mysock.close()