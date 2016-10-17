# -*- coding: utf-8 -*-
import socket
import random
import sys
from datetime import *

a = datetime.now()
timestamp = a.strftime('%H%M%S%f')
matrix_file_name = "matriz" + timestamp + ".txt"
print matrix_file_name

def create_matrix(matrix_size):
  
  matrix = []
  for i in range(matrix_size):
  	matrix.append([0]*matrix_size)

  print matrix

  matrix_file = open(matrix_file_name, 'a+')
  for i in range(0, matrix_size):
      for j in range(0, matrix_size):
          number = random.randint(0, 100)
          matrix[i][j] = number
          print(str(number) + "\t")
          matrix_file.write((str(number) + "\t"))
      print()
      matrix_file.write("\n")
  print()
  matrix_file.close()
  print matrix
  return matrix

def print_matrix(matrix):
  for i in range(0, matrix_size):
      for j in range(0, matrix_size):
          print(str(matrix[i][j]) + "\t")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST, PORT
server_addr = ('127.0.0.1', 3000)

sock.connect(server_addr)


# tamanho da matriz
m = sys.argv[1]

m1 = create_matrix(int(m))
m2 = create_matrix(int(m))
#print m

#envia o tamanho da matriz ao servidor
sock.send(m)

file = open(matrix_file_name, 'r')

file.seek(0,0)

while True:
	chunk = file.read(1024)
	print chunk
	sock.send(chunk)
	#EOF
	if chunk == '':
		break

file.close()

sock.close()