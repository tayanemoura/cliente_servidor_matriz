#https://docs.python.org/2/library/socket.html
# -*- coding: utf-8 -*-
import socket
import thread
from datetime import *

#TODO
#função para multiplicar as matrizes e salvar em um arquivo multiplica.txt
def multiply_matrices(m1, m2):
	print "Iniciando multiplicação.."
	a = datetime.now()
	print a.strftime('%Hh%Mm%Ss%fus')
	#implementação

	thread.exit()

#TODO
#função para somar as matrizes e salvar em um arquivo soma.txt
def add_matrices(m1, m2):
	print "Iniciando soma.."
	a = datetime.now()
	print a.strftime('%Hh%Mm%Ss%fus')
	#implementação

	thread.exit()

def read_client(conn, client):
	print "Cliente:", client
	file = ""

	#recebe do servidor o tamanho da matriz - ainda não sei se será necessária essa info
	m = conn.recv(1024)
	#print m

	while True:
		data = conn.recv(1024)
		file = file + data
		if not data:
			break
		#print data
		
	#TODO
	#separa as duas matrizes - considerando que cada matriz está em cada linha, mas vai depender de como faremos o arquivo 
	aux = file.split('\n')
	#print aux

	#TODO
	#como ainda não sei como faremos para ler a matriz coloquei assim por enquanto

	matrix_1 = aux[0]
	matrix_2 = aux[1]

	thread.start_new_thread(multiply_matrices, tuple([matrix_1,matrix_2]))
	thread.start_new_thread(add_matrices, tuple([matrix_1,matrix_2]))

	#TODO:
	#ainda precisamos enviar os arquivos multiplica.txt e soma.txt pro usuário

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