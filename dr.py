import socket
import os

def sendfile(conn):
	print('I have file ,begin to send file')
	#rely = conn.recv(1024)							#get rely 
	#filename = rely.decode('utf - 8')				#turn into word
	#if rely == 'ready':
	#	conn.send(b'yes')
	size = 1024
	with open(filename,'rb') as f:
		while True:
			data = s.read(size)					#turn into 1024
			conn.send(data)						#send data
			if len(data)<size:
				break
	print('This file sending is successfully!')
	conn.close()



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.128.81.24',1110))								#connect
while True:
	filename = input('Which file do you need to send?')
	print('I want to send the file %s!'% filename)
	if os.path.exists(filename):							#do we have this file?
		s.send(filename.encode('utf-8'))					#send name in utf-8
		sendfile('10.128.81.24')								#begin send
	else:
		print('There is no file %s'% filename)
s.close()
print('connect is over!')
