# -*- coding: utf-8 -*-
import socket
import random
import sys
import pdb    
#from datetime import *
import time

matrix_file_name = "matriz.txt"

def create_matrix(matrix_size): 
	matrix = []
	for i in range(matrix_size):
		matrix.append([0]*matrix_size)

	matrix_file = open(matrix_file_name, 'a+')
	for i in range(0, matrix_size):
			for j in range(0, matrix_size):
					number = random.randint(0, 100)
					matrix[i][j] = number
					matrix_file.write((str(number) + "\t"))
			matrix_file.write("\n")
	matrix_file.close()
	return matrix

def print_matrix(matrix, matrix_size):
		for i in range(matrix_size):
			for j in range(matrix_size):
				print "%3d" % matrix[i][j],
			print

def delete_content():
	file = open(matrix_file_name, 'w')
	file.seek(0)
	file.truncate()


def read_server():
	buf = ""

	while True:
		data = sock.recv(1024)
		buf = buf + data
		if not data:
			break
	print buf

def send_matrix_size():
	#envia o tamanho da matriz ao servidor
	sent = sock.send(m)

	#trata erro no envio
	while (sent != len(m)):
		pdb.set_trace()
		sent = sock.send(m)

def send_server():
	file = open(matrix_file_name, 'r')
	#file.seek(0,0)
	while True:
		chunk = file.read(1024)
		sock.send(chunk)
		#EOF
		if chunk == '':
			sock.send("ACK")
			break
	file.close()

			
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#HOST, PORT
server_addr = ('127.0.0.1', 3000)
sock.connect(server_addr)

# tamanho da matriz
m = sys.argv[1]
matrix_size = int(m)

#apaga conteúdo do arquivo, caso haja
delete_content()

m1 = create_matrix(matrix_size)
m2 = create_matrix(matrix_size)
print "M1:\n"
print_matrix(m1, matrix_size)
print "\nM2:\n"
print_matrix(m2, matrix_size)


send_matrix_size()

while True:
	answer = sock.recv(1024)
	if "NACK" in answer:
		send_matrix_size()
	else:
		break

send_server()


read_server()


sock.close()