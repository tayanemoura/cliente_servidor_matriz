#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>

 #include <sys/types.h>
 #include <sys/socket.h>
 #include <sys/uio.h>

// socket(),connect(), send(), recv(), close()

int main(void) {


	int sock;
	struct sockaddr_in server_addr;
	char buffer[1024];

	//inicializando variáveis do arquivo
	FILE* file = NULL;
	int offset= 0;
	int already_sent =0;
	int file_d;



	//PF_INET = IPv4
	sock = socket(PF_INET, SOCK_STREAM, 0);	

	if(sock<0){
		perror("Erro na criação do socket");
	}

	memset(&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(3000);
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

	
	if(connect(sock, (struct sockaddr *) &server_addr, sizeof(server_addr))<0){
		perror("Problema na conexão");
	} 
	else{
		printf("Conectado\n");
	}

	//strcpy(buffer, "Hello Worl4\n");
	//int send(int sockfd, const void *msg, int len, int flags); 
	//send(sock, buffer, strlen(buffer), 0);
	
	file = fopen("example.txt", "rb");

	if(file == NULL){
		printf("Erro ao abrir o arquivo");
		exit(1);
	}

	

	fseek(file, 0L, SEEK_END);
	int file_size = (int) ftell(file);
	
	printf("%s\n", buffer);

	sprintf(buffer,"%d", file_size);
	strcat(buffer, "\n");
	if(send(sock, buffer, strlen(buffer), 0)==-1){
		perror("Problema no envio do tamanho");
		exit(1);
	}

	file_d = open("example.txt", O_RDONLY);

	if(file_d == -1){
		fprintf(stderr, "Erro: %s\n", strerror(errno) );
		exit(1);
	}

	// read == 0 significa EOF
	while (read(file_d, buffer, 1023)!=0) {
		strcat(buffer, "\n");
	    send(sock, buffer, 1024, 0); 
	}
	strcpy(buffer, "EOF\n");
	send(sock, buffer, 4, 0);

	close(sock);
	
}