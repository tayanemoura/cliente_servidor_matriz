#https://docs.python.org/2/library/socket.html
# -*- coding: utf-8 -*-
import pdb    
import socket
import thread
import random
from datetime import *



def print_matrix(matrix):
	for i in range(0, matrix_size):
			for j in range(0, matrix_size):
					print(str(matrix[i][j]) + "\t")

#função para multiplicar as matrizes e salvar em um arquivo multiplica.txt
def multiply_matrices(matrix_1, matrix_2):
	print "Iniciando multiplicação.."
	a = datetime.now()
	#print a.strftime('%Hh%Mm%Ss%fus')
	#implementação
	multiply_file = open('multiplica.txt', 'a')
	matrix_size = len(matrix_1)

	for i in range(matrix_size):
		for j in range(matrix_size):
			number = 0
			for k in range(matrix_size):
				number += matrix_1[i][k] * matrix_2[k][j]
			multiply_file.write(str(number) + "\t")
		if i != matrix_size - 1:
			multiply_file.write("\n")

	multiply_file.write("\n")
	multiply_file.write("---------------------------------------------\n")

	multiply_file.close()


	thread.exit()

def add_matrices(m1, m2):
	print "Iniciando soma.."
	start = datetime.now()
	print start.strftime('%Hh%Mm%Ss%fus')

	sum_file = open('soma.txt', 'a')

	matrix_size = len(m1)
	total = 0
	for i in range(matrix_size):
		for j in range(matrix_size):
			total = m1[i][j] + m2[i][j]
			sum_file.write(str(total) + "\t")
		sum_file.write("\n")

	sum_file.write("\n")
	sum_file.write("---------------------------------------------\n")

	end = datetime.now()
	print end.strftime('%Hh%Mm%Ss%fus')

	sum_file.close()

	thread.exit()

#função para retornar uma matriz quadrada a partir de uma lista de elementos
def get_matrix(elements, matrix_size):
	#inicializa matriz
	matrix = []
	for i in range(matrix_size):
		matrix.append([0]*matrix_size)
	
	k=0
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			matrix[i][j] = int(elements[k])
			k+=1

	return matrix

def send_file(file_name, conn):
	file = open(file_name, 'r')
	while True:
		chunk = file.read(1024)
		conn.send(chunk)
		#EOF
		if chunk == '':
			break

def read_client(conn, client):
	print "Cliente:", client
	file = ""

	#recebe do servidor o tamanho da matriz
	m = conn.recv(1024)
	print m
	matrix_size = int(m)

	while True:
		print "read_client"
		data = conn.recv(1024)
		file = file + data
		if not data: 

			conn.send("ACK")
			print "break do read_client"
			break
		print "depois do while do read_client"
		
		#apaga os \n
		aux = file.replace("\n", "")
		# guarda na lista elements cada número
		elements = aux.split("\t")

		#passa a primeira metade da lista para retornar matriz 1
		matrix_1 = get_matrix(elements[:matrix_size*matrix_size], matrix_size)
		#passa a segunda metade da lista para retornar a matriz2
		matrix_2 = get_matrix(elements[matrix_size*matrix_size:], matrix_size)
		
		print matrix_1
		print matrix_2

		thread.start_new_thread(multiply_matrices, tuple([matrix_1,matrix_2]))
		thread.start_new_thread(add_matrices, tuple([matrix_1,matrix_2]))

		#send_file("multiplica.txt", conn)
		send_file("soma.txt", conn)

		conn.close()
		thread.exit()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST, PORT
server_addr = ('127.0.0.1', 3000)

sock.bind(server_addr)
sock.listen(10)
print "Esperando conexões.."


while True:
	connection, client_addr = sock.accept()
	thread.start_new_thread(read_client, tuple([connection, client_addr]))

sock.close()