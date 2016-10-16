#https://docs.python.org/2/library/socket.html
# -*- coding: utf-8 -*-
import socket
import thread


def read_client(conn, client):
	print "Cliente:", client

	while True:
		data = conn.recv(1024)
		if not data:
			break
		print data

	conn.close()
	thread.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST, PORT
server_addr = ('127.0.0.1', 3000)

sock.bind(server_addr)
sock.listen(1)

print "Esperando conexões.."

while True:
	connection, client_addr = sock.accept()
	thread.start_new_thread(read_client, tuple([connection, client_addr]))

sock.close()