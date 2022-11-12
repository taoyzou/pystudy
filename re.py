import socket
import os


def getfile(conn):
	strl = conn.recv(1024)							#get file name from client
	filename = strl.decode('utf - 8')				#turn into word
	print('Will get the file %s' % filename)
	#conn.send(b'ready!')
	#strl2 = conn.recv(1024)
	#rely = strl2.decode('utf - 8')
	#if rely == 'no':
	#	print('To get the file %s is failed!' % filename)
	#else:
	temp = filename.split('/')						#begin to deal word
	myname = 'my_' + temp[len(temp)-1]
	size = 1024
	with open(myname,'wb') as f:
		while True:
			data = conn.recv(size)					#turn into 1024
			conn.write(data)						#send data
			if len(data)<size:
				break
	print('The downloaded file is %s'% myname)

	
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.128.81.24',1110))						#connect
s.listen(1)											#only connect
print('Waiting for connecting...')
while True:
	(conn,addr)=s.accept()							#waiting connect
	getfile(conn)									#begin get file
s.close()
print('connect is over!')

