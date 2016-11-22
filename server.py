#https://docs.python.org/2/library/socket.html
# -*- coding: utf-8 -*-
import pdb    
import socket
import threading
import random
from datetime import *



def print_matrix(matrix):
	for i in range(0, matrix_size):
			for j in range(0, matrix_size):
					print(str(matrix[i][j]) + "\t")

#função para multiplicar as matrizes e salvar em um arquivo multiplica.txt
def multiply_matrices(matrix_1, matrix_2):
	print "Iniciando multiplicação.."
	multiply_file = open('multiplica.txt', 'w')
	
	#inicio da execuçao
	start = datetime.now()
	start_time = start.strftime('%Hh%Mm%Ss%fus')
	print "Inicio multiplicação - "+start_time+"\n"
	multiply_file.write("Inicio multiplicação -"+start_time+'\n')

	#multiplica
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
	
	#Fim da execuçao
	end = datetime.now()
	end_time = end.strftime('%Hh%Mm%Ss%fus')
	print "Fim multiplicação - "+ end_time+"\n"
	multiply_file.write('Fim multiplicação - '+ end_time+'\n')
	multiply_file.close()


def add_matrices(m1, m2):
	print "Iniciando soma.."
	sum_file = open('soma.txt', 'w')

	#Inicio da execuçao
	start = datetime.now()
	start_time = start.strftime('%Hh%Mm%Ss%fus')
	print "Inicio soma - "+start_time+"\n"
	sum_file.write('Inicio soma - '+start_time+'\n')

	#soma
	matrix_size = len(m1)
	total = 0
	for i in range(matrix_size):
		for j in range(matrix_size):
			total = m1[i][j] + m2[i][j]
			sum_file.write(str(total) + "\t")
		sum_file.write("\n")

	sum_file.write("\n")

	#Fim da execuçao
	end = datetime.now()
	end_time = end.strftime('%Hh%Mm%Ss%fus')
	print "Fim soma - "+ end_time+"\n"
	sum_file.write('Fim soma - '+ end_time+'\n')

	sum_file.close()


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
		sent = conn.send(chunk)

		#EOF
		if chunk == '':
			break
		

def read_client(conn, client):
	print "Cliente:", client
	file = ""

	#recebe do servidor o tamanho da matriz
	m = conn.recv(1024)

	while not m.isdigit():
		pdb.set_trace()
		conn.send("NACK")
		m = conn.recv(1024)

	conn.send("ACK")

	matrix_size = int(m)

	while True:
		data = conn.recv(1024)
		file = file + data
		if "ACK" in data:
			break
		
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

	mult = threading.Thread(target = multiply_matrices, args = (matrix_1,matrix_2))
	soma = threading.Thread(target = add_matrices, args = (matrix_1,matrix_2))

	mult.start()
	soma.start()

 	mult.join()
 	soma.join()

	send_file("multiplica.txt", conn)
	send_file("soma.txt", conn)

	conn.close()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST, PORT
server_addr = ('127.0.0.1', 3000)

sock.bind(server_addr)
sock.listen(10)
print "Esperando conexões.."


while True:
	connection, client_addr = sock.accept()
	client = threading.Thread (target = read_client, args = (connection, client_addr))
	client.start()
	# thread.start_new_thread(read_client, tuple([connection, client_addr]))

sock.close()