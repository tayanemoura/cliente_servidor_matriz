# -*- coding: utf-8 -*-
import socket
import sys

def generate_matrix():
	pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST, PORT
server_addr = ('127.0.0.1', 3000)

sock.connect(server_addr)


# tamanho da matriz
m = sys.argv[1]

#print m

#envia o tamanho da matriz ao servidor
sock.send(m)

file = open('example.txt', 'r')

#file.seek(0,0)

while True:
	chunk = file.read(1024)
	print chunk
	sock.send(chunk)
	#EOF
	if chunk == '':
		break

file.close()

sock.close()