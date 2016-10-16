# -*- coding: utf-8 -*-
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST, PORT
server_addr = ('127.0.0.1', 3000)

sock.connect(server_addr)

#chunk = "Hello World!"

file = open('example.txt', 'r')

while True:
	chunk = file.read(1024)
	print chunk
	sock.send(chunk)
	#EOF
	if chunk == '':
		break



sock.close()